import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-063'
P = {}
P['Authorization'] = 'CWB-80B8FFEA-FFCC-4931-B91C-C38CD577ACD7'
r = requests.get(URL, params=P)
t = r.json()

n = len(t['records']['locations'][0]['location'][0]['weatherElement'])
for i in range(n):
    print(i, t['records']['locations'][0]['location'][0]['weatherElement'][i]['description'])
