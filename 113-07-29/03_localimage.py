#LINENOTIFY傳送本機圖片
import requests

URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer BTDDX4o74wYf3F0krPAVkW7ieCZg44mKzB5rZu5sqA7'
P['message'] = '本機圖片'
#F['imageFile'] = open(r'C:\Users\Chuckhu\OneDrive - Shih Hsin University\Pictures\Tom Cruise\OIP(3).jpg', 'rb')
F['imageFile'] = open('fsd.jpg', 'rb')
#F['imageFile'] = open('./pictures/logo.jpg', 'rb')
requests.post(URL, headers=H, params=P, files=F)