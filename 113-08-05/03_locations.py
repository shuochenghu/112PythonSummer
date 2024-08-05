import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {}
P['Authorization'] = 'CWB-80B8FFEA-FFCC-4931-B91C-C38CD577ACD7'
r = requests.get(URL, params=P)
t = r.json()

n = len(t['records']['Station'])
print(f"n = ", n)
for i in range(n):
    print(i, t['records']['Station'][i]['StationName'])
