#抓包自己账号TOEKN，'LATITUD''LONGITUDE'填写自己实习地址的经纬度

import requests
import uuid
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
print(response_data.get('msg'))
