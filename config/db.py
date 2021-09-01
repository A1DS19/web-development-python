import pymongo
import os
import certifi

db_name = os.environ["DB_NAME"]
user = os.environ["USER"]
password = os.environ["PASSWORD"]


try:
    client = pymongo.MongoClient(
        f"mongodb+srv://{user}:{password}@cluster0.cvx1o.mongodb.net/{db_name}?retryWrites=true&w=majority",
        tlsCAFile=certifi.where(),
    )
    print("DB CONNECTED")
except Exception as err:
    print(err)

db = client[db_name]
