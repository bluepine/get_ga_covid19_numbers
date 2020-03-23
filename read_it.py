from time import ctime
import pandas as pd
import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["gacovid19"]
# collection
govnumbers = db["govnumbers"]
for record in govnumbers.find():
    time = record['time']
    df = pd.DataFrame(record["data"])
    print(ctime(time))
    print(df)
