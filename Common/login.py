import requests

import glo
from Common.sign import get_sign


def login():

    json1 = {
        "phone": "18379204795",
        "password": "33791626cdcbbf5b0b834f9d808f3188",
        "phoneArea": "86",
        "clientId": "b1e009f1e947c306668b962579fbc498"
    }
    sign1 = {"sign": get_sign(json1)}
    json1.update(sign1)
    session = requests.session()
    response_login = session.post("http://192.168.1.241/as_user/api/user_account/v1/user_login_pwd", headers={
            "Content-Type": "application/json;charset=utf-8",
            "lang": "zh_CN",
            "osType": "android",
            "osVersion": "8.1.0",
            "appVersion": "1.0.0",
            "deviceId": "d5744d9b2be20e91"
        }, json=json1)

    res = response_login.json().get("data").get("token")
    with open(glo.BASE_DIR + r'/TestData/token.yaml', 'w') as file:
        file.write("token: " + res)
    # print(glo.TOKEN)

# login()