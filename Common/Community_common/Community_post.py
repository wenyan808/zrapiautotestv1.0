import json

import requests

from Common.sign import get_sign


# 社区发帖公共代码部分
def Communityaddpost(url: str, headers: dict, paylo: dict):
    """

    :param url: 社区发帖url
    :param headers: 请求头
    :param paylo: 请求参数
    :return: 返回结果数据
    """
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url, headers=headers, data=payload
    )
    j = r.json()
    # print(j)
    return j


def Communitypostdelete(url: str, headers: dict, body: dict):
    """

    :param url: 社区帖子删除url
    :param headers: 请求头部（带token）
    :param body: 请求参数body
    :return: 返回结果数据
    """
    sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(body)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url, headers=headers, json=payload
    )
    j = r.json()
    # print(j)
    return j
