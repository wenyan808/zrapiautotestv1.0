import json

import requests

from Common.sign import get_sign


def send_code(url: str, headers: dict, payload: dict):
    """发送短信

    :param url: url
    :param headers: 带token的headers请求报文（部分headers不传入token）
    :param payload: 不带sign的body参数（payload)
    :return:
    """
    sign1 = {"sign": get_sign(payload)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(payload)
    payload1.update(sign1)

    data = json.dumps(dict(payload1))
    response_getcode = requests.session().post(url=url, headers=headers, data=data)
    # print(response_getcode.json())
    return response_getcode
