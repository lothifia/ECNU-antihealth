# -*-coding:utf-8-*-
import requests
import json
import time
from getToken import get_token
import config
LOGIN_URL = 'https://face-reg.ecnu.edu.cn/api/v3/login/ecnu'
REC_URL = 'https://anti-epidemic.ecnu.edu.cn/clock/mini/record'
QRY_URL = 'https://anti-epidemic.ecnu.edu.cn/clock/mini/user/v2/'
TOK_URL = f'https://anti-epidemic.ecnu.edu.cn/clock/mini/wx/new?open_key={config.open_key}'
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type': 'application/json',
    'Referer': 'https://servicewechat.com/wxfcaebbc17bdc154b/27/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br'
}

s = requests.session()


def HealthRecord():
    regData = {
        'number': config.user['stuID'],
        'password': config.user['password'],
        'unionId': config.user['unionID'],
    }
    # login_req = s.post(LOGIN_URL, data=json.dumps(regData), headers=headers)
    # login_resp = json.loads(login_req.content)
    # print(f"{login_resp=}")
    tok_req = s.get(TOK_URL, headers=headers)
    tok_resp = json.loads(tok_req.content)
    print(f"{tok_resp=}")
    headers['MiniToken'] = tok_resp['message']
    postData = {
        'number': config.user['stuID'],
        'location': '在上海不在校',
        'health': '健康，未超过37.3',
        'recordTime': int(round(time.time() * 1000)),
        'token': get_token(
            tok_resp['result']['name'],  # just your chinese name
            config.user['stuID'],
        )
    }
    # print(f"{postData=}")
    # print(f"{headers['MiniToken']=}")
    rec_req = s.put(REC_URL, data=json.dumps(postData), headers=headers)
    rec_resp = json.loads(rec_req.content)
    # print(f"{rec_resp=}")
    qry_req = s.get(QRY_URL + config.user['stuID'], headers=headers)
    qry_resp = json.loads(qry_req.content)
    print(f"{qry_resp['result'][0]['lastRecord']['date']=}")
    return rec_resp['code'], rec_resp['message']


if __name__ == '__main__':  # test
    print(f"{HealthRecord()=}")
