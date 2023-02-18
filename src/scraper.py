import asyncio
import json
from datetime import datetime, timedelta
from typing import Dict

from playwright.async_api import async_playwright

from config.configer import Config
from src.db import ScraperDB


class Scraper:
    urls_list = Config.get_list("urls", "urls")
    urls_list = list(map(lambda x: Config.get("urls", "base_url") + x, urls_list))

    @staticmethod
    def _round_time(dt=None, date_delta=timedelta(minutes=1), to='down'):
        """
        Round a datetime object to a multiple of a timedelta
        dt : datetime.datetime object, default now.
        dateDelta : timedelta object, we round to a multiple of this, default 1 minute.
        """
        round_to = date_delta.total_seconds()
        if dt is None:
            dt = datetime.now()
        seconds = (dt - dt.min).seconds
        if seconds % round_to == 0 and dt.microsecond == 0:
            rounding = (seconds + round_to / 2) // round_to * round_to
        else:
            if to == 'up':
                rounding = (seconds + dt.microsecond / 1000000 + round_to) // round_to * round_to
            elif to == 'down':
                rounding = seconds // round_to * round_to
            else:
                rounding = (seconds + round_to / 2) // round_to * round_to

        return dt + timedelta(0, rounding - seconds, - dt.microsecond)

    @classmethod
    async def _request_http(cls, url: str) -> Dict[str, list]:
        """
        http request with playwright rendering
        """
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(url, timeout=10000)
            data = await page.inner_text(selector="pre")
            data = json.loads(data)
            output = {
                url.strip(): data
            }
            await browser.close()
            return output

    @classmethod
    async def _do_all_requests(cls) -> dict:
        """
        do request on list of url with method request_http
        """
        print("sending http requests ...")
        tasks = list()
        for url in cls.urls_list:
            tasks.append(cls._request_http(url))
        result = asyncio.gather(*tasks)
        final_data = {'data': await result,
                      "datetime": cls._round_time(dt=datetime.now(),
                                                  date_delta=timedelta(minutes=1),
                                                  to='down')}
        return final_data

    @classmethod
    def run(cls):
        """main function of the class"""
        data = asyncio.run(cls._do_all_requests())
        ScraperDB.add(data)
