from time import ctime
import ntplib
from lxml import html
from lxml import etree
import requests

page = requests.get('https://dph.georgia.gov/covid-19-daily-status-report')
root = html.fromstring(page.content)
tree = root.getroottree()
print(tree)
c = ntplib.NTPClient()
response = c.request('us.pool.ntp.org', version=3)
print(ctime(response.tx_time))


lab_header = etree.fromstring(
    r'<tr><th scope="col">Lab</th><th scope="col">Number of Positive Tests</th><th scope="col">Total Tests</th></tr>')
print(lab_header)
# print(tree.getpath(lab_header))
print(root.xpath('//thead'))
# print(etree.tostring(root, pretty_print=True))
tables = root.xpath('//table')
deaths = tables[0]
tests = tables[1]
counties = tables[2]


def print_element(ele):
    print(etree.tostring(ele))


print_element(deaths)
print_element(tests)
print_element(counties)
