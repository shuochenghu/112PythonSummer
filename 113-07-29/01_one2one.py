import requests

URL = 'https://notify-api.line.me/api/notify'
H, P = {}, {}
H['Authorization'] = 'Bearer BTDDX4o74wYf3F0krPAVkW7ieCZg44mKzB5rZu5sqA7'
P['message'] = '今天是星期五晚上'
response = requests.post(URL, headers=H, params=P)

print(response.status_code)
print(response.text)
