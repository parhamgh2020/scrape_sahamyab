import configparser
from datetime import time


class Config:
    config = configparser.ConfigParser(interpolation=None)
    config.read('config/config.ini')

    @classmethod
    def get(cls, *args):
        return cls.config.get(*args)

    @classmethod
    def get_bool(cls, *args):
        return cls.config.getboolean(*args)

    @classmethod
    def get_list(cls, *args):
        lst = cls.config.get(*args)
        return lst.replace('\n', '').split(',')

    @classmethod
    def get_int(cls, *args):
        return cls.config.getint(*args)

    @classmethod
    def get_time(cls, *args):
        t: str = cls.config.get(*args)
        hour, minute = map(int, t.split(':'))
        return time(hour=hour, minute=minute)
