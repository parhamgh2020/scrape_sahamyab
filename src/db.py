import os

from pymongo import MongoClient

from config.configer import Config

try:
    uri = os.environ.get['mongo_uri']
except:
    uri = Config.get("mongo", "uri")
client = MongoClient(uri)


class ScraperDB:
    db = client[Config.get("mongo", "db")]
    collection = db[Config.get("mongo", "collection")]

    @classmethod
    def add(cls, data: dict):
        """
        add data to mongo database
        """
        print("adding data to database ...")
        res = cls.collection.insert_one(data)
        return res.acknowledged
