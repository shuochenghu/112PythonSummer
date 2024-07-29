import requests

URL = 'https://notify-api.line.me/api/notify'
H, P = {}, {}
H['Authorization'] = 'Bearer BTDDX4o74wYf3F0krPAVkW7ieCZg44mKzB5rZu5sqA7'
P['message'] = '貼圖測試'
P['stickerPackageId'] = 6325
P['stickerId'] = 10979907
requests.post(URL, headers=H, params=P)
