import os

from pymongo import MongoClient

from config.configer import Config

uri = os.environ.get('mongo_uri', Config.get("mongo", "uri"))
print(uri)

client = MongoClient(uri)

# client = MongoClient("mongodb://localhost:27017")


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
