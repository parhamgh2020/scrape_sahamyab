from pymongo import MongoClient

from config.configer import Config

uri = Config.get("mongo", "uri")
uri_compose = Config.get("mongo", "uri_compose")

try:
    print("checking database takes 30 seconds ...")
    client = MongoClient(uri_compose)
    client.server_info()
except Exception as err:
    client = MongoClient(uri)
    print(client)

print("database:", client)

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
