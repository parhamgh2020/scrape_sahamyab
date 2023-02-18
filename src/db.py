from pymongo import MongoClient

from config.configer import Config

uri = Config.get("mongo", "uri")
uri_compose = Config.get("mongo", "uri_compose")

try:
    client = MongoClient(uri)
    MongoClient(uri).server_info()
except Exception as err:
    client = MongoClient(uri_compose)


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
