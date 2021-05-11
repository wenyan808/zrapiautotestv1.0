import json

import requests

from Common.OSS import oss_file
from Common.getConsoleLogin import getConsoleLogin_token
from Common.sign import get_sign
from glo import console_HTTP, console_JSON


def get_ConTopicID():
    url = console_HTTP + "/api/con_topic/v1/add"
    url1 = console_HTTP + "/api/con_sts/v1/token"
    url2 = console_HTTP + "/api/con_topic/v1/list"
    header = console_JSON
    header = header

    headers = {}
    headers.update(header)

    token = {"token": getConsoleLogin_token()}
    headers.update(token)  # 将token更新到headers
    name = "自动化测试专题"
    description = "本次接口已测试为主，不可胡乱添加到前端，请谨慎添加或者关联到前端"
    categoryId = 0
    catalog = "/Business/Img/"
    headImg = list(oss_file("information", "img01.jpg", catalog, url1, headers))[-1]
    backgroundImg = list(oss_file("information", "img02.jpg", catalog, url1, headers))[-1]
    paylo = {
        "name": name,
        "description": description,
        "categoryId": categoryId,
        "headImg": headImg,
        "backgroundImg": backgroundImg
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r_add = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j_add = r_add.json()

    paylo = {
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url2, headers=headers, data=payload
    )

    j_list = r.json()
    return j_list.get("data").get("list")[0].get("id"), headers, j_list

# print(get_ConTopicID())
