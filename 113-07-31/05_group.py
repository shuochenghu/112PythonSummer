import requests

#IMG = 'https://www.shu.edu.tw/BBS/Ann_Spotlight/28311/20210503%E6%A0%A1%E9%96%802.jpg'
IMG = 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/01/25/ce/47/moraine-lake.jpg?w=1400&h=1400&s=1'
URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer BLJxO0Y8dDcWMukYMFBD36b54wNB4GR2bEPCCSLPiKc'
P['message'] = '群組網路圖片'
F['imageFile'] = requests.get(IMG).content
response = requests.post(URL, headers=H, params=P, files=F)

print(response.status_code)
print(response.text)