#抓包签到软件TOEKN，'LATITUD''LONGITUDE'填写自己实习地址的经纬度
import requests
import uuid
def send_pushplus_notification(token, title, content):
    pushplus_url = f'http://www.pushplus.plus/send?token={token}&title={title}&content={content}'
    response = requests.get(pushplus_url)
    return response
headers = {
    'Token': 'TOKEN',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}
data = {
    'lat': 'LATITUDE',
    'lng': 'LONGITUDE',
    'phoneUuid': uuid.uuid4().hex,
    'taskId': '89',
    'type': '1',
}
url = 'http://sx.bymu.cn/api/sign/signIn'
response = requests.post(url, headers=headers, data=data)
response_data = response.json()
msg = response_data.get('msg')
# 替换'PUSHPLUS_TOKEN'为你在PushPlus获取的Token
pushplus_token = 'PUSHPLUS_TOKEN'

send_pushplus_notification(pushplus_token, '签到结果', msg)
print(msg)
