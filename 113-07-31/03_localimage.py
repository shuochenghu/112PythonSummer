#LINENOTIFY傳送本機圖片
import requests

URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer BTDDX4o74wYf3F0krPAVkW7ieCZg44mKzB5rZu5sqA7'
P['message'] = '本機圖片'
#F['imageFile'] = open(r'C:\Users\m303\Pictures\harris.jpg', 'rb')#圖檔絕對路徑
#F['imageFile'] = open('trump.png', 'rb')
F['imageFile'] = open('./pictures/vans.jpg', 'rb') #圖檔相對路徑
requests.post(URL, headers=H, params=P, files=F)