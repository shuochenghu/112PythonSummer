import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-063'
P = {}
P['Authorization'] = 'CWB-80B8FFEA-FFCC-4931-B91C-C38CD577ACD7'
r = requests.get(URL, params=P)
t = r.json()

#print(t['records']['locations'][0]['location'][0]['weatherElement'][0]['description']+ ':')
n = len(t['records']['locations'][0]['location'])
for i in range(n):
    print(t['records']['locations'][0]['location'][i]['locationName'], 
          t['records']['locations'][0]['location'][i]['weatherElement'][1]['time'][1]['elementValue'][0]['value'])
