import json

import requests

from Common.OSS import oss_file
from Common.sign import get_sign
from glo import console_HTTP


def add_ConTopic(headers: dict, name: str):
    """新增专题

    :param headers: 带token的headers
    :param name: 专题的名称
    :return:返回新增专题是否成功的json数据
    """
    url = console_HTTP + "/api/con_topic/v1/add"
    url1 = console_HTTP + "/api/con_sts/v1/token"

    # name = "自动化测试专题"
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
    return j_add


def add_category(headers: dict, name: str):
    """新增专题分类

    :param headers: 带token的headers参数
    :param name: 分类名称
    :return:返回新增专题分类的结果是否成功的json数据
    """
    url = console_HTTP + "/api/con_topic/v1/add_category"

    paylo = {
        "name": name
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
    return j_add
