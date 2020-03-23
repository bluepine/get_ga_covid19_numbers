import pandas
import ntplib
import pymongo
from pymongo import MongoClient

def get_time():
    c = ntplib.NTPClient()
    response = c.request('us.pool.ntp.org', version=3)
    return response.tx_time

tables = pandas.read_html('https://dph.georgia.gov/covid-19-daily-status-report')
time = get_time()


records = []
for t in tables:
    t.columns = t.columns.str.replace(".", "_") # mongo doesn't like . in keys
    records.extend(t.to_dict('records'))


client = MongoClient("mongodb://localhost:27017/")

db = client["gacovid19"]
# collection
govnumbers = db["govnumbers"]
govnumbers.insert_one({'time': time, 'data': records})

