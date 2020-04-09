import urllib.request
import pandas
import ntplib
import pymongo
from lxml import etree
from pymongo import MongoClient

def get_time():
    c = ntplib.NTPClient()
    response = c.request('us.pool.ntp.org', version=3)
    return response.tx_time

response = urllib.request.urlopen('https://dph.georgia.gov/covid-19-daily-status-report')
html = response.read()
response.close()
print(html)
dom = etree.HTML(html)

iframe_url = dom.xpath('//*[@id="covid19dashdph"]/iframe/@src')
print(iframe_url)
#tables = pandas.read_html('https://dph.georgia.gov/covid-19-daily-status-report')
tables = pandas.read_html(iframe_url)
time = get_time()


records = []
for t in tables:
    print(t)
    t.columns = t.columns.astype(str)
    t.columns = t.columns.str.replace(".", "_") # mongo doesn't like . in keys
    records.extend(t.to_dict('records'))


client = MongoClient("mongodb://localhost:27017/")

db = client["gacovid19"]
# collection
govnumbers = db["govnumbers"]
govnumbers.insert_one({'time': time, 'data': records})

