from datetime import datetime
from enum import Enum
from time import sleep

from config.configer import Config
from src.scraper import Scraper


class Weekday(Enum):
    monday = 0
    tuesday = 1
    wednesday = 2
    thursday = 3
    friday = 4
    saturday = 5
    sunday = 6


def main(start_time,
         end_time,
         sleep_time,
         working_days):
    """ main function of app"""
    now = datetime.now()
    print(f'start webscraping data at {now} ...')
    weekday = now.weekday()
    time = now.time()
    work_days = map(lambda day: Weekday[day].value, working_days)
    if weekday in work_days and start_time <= time <= end_time:
        Scraper.run()
    print(f"next webscraping will be started {sleep_time} seconds later", end='\n\n')
    sleep(sleep_time)


if __name__ == '__main__':
    print('app started', end='\n\n')
    start_time = Config.get_time("working_time", "start_time")
    end_time = Config.get_time("working_time", "end_time")
    sleep_time = Config.get_int("working_time", "every_minutes") * 60
    working_days = Config.get_list("working_time", "days")
    while True:
        try:
            main(start_time,
                 end_time,
                 sleep_time,
                 working_days)
        except Exception as err:
            print("error:", err)
            sleep(60)
