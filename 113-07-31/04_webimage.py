import requests

#IMG = 'https://www.shu.edu.tw/BBS/Ann_Spotlight/28311/20210503%E6%A0%A1%E9%96%802.jpg'
IMG = 'https://today-obs.line-scdn.net/0hr8F7QP38LRd7TgS084dSQEEYLnhIIj4UH3h8FDggcyMBLG9IQyA2eVhIdXcEdmpJFXpmeVdHNiYDf2sRFSE2/w1200'
URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer BTDDX4o74wYf3F0krPAVkW7ieCZg44mKzB5rZu5sqA7'
P['message'] = '網路圖片'
F['imageFile'] = requests.get(IMG).content
response = requests.post(URL, headers=H, params=P, files=F)

print(response.status_code)
print(response.text)