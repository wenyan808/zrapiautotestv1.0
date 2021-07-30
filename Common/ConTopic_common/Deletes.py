import json

import requests

from Common.getConsoleLogin import getConsoleLogin_token
from Common.sign import get_sign
from glo import console_HTTP, console_JSON


def delete_ConTopicID(ID: int):
    """删除专题

    :param ID:专题id
    :return:
    """
    url = console_HTTP + "/api/con_topic/v1/delete"

    header = console_JSON


    headers = {}
    headers.update(header)

    token = {"token": getConsoleLogin_token()}
    headers.update(token)  # 将token更新到headers

    paylo = {
        "id": ID
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r_delete = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j_delete = r_delete.json()
    return j_delete


# print(delete_ConTopicID())


def delete_ConTopiccategory(categoryId: int):
    """删除专题分类

    :param categoryId:专题分类id
    :return:
    """
    url = console_HTTP + "/api/con_topic/v1/delete"

    header = console_JSON


    headers = {}
    headers.update(header)

    token = {"token": getConsoleLogin_token()}
    headers.update(token)  # 将token更新到headers

    paylo = {
        "categoryId": categoryId
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r_delete = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j_delete = r_delete.json()
    return j_delete


# print(delete_ConTopiccategory())


def delete_AddConNews(newsId: int):
    """删除新增资讯

    :param newsId: 资讯id
    :return:
    """
    url = console_HTTP + "/api/con_news/v1/disable"

    header = console_JSON


    headers = {}
    headers.update(header)

    token = {"token": getConsoleLogin_token()}
    headers.update(token)  # 将token更新到headers
    status = 1  # 启用禁用(0,正常1,屏蔽)
    paylo = {
        "newsId": newsId,
        "status": status
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r_delete = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j_delete = r_delete.json()
    return j_delete


def list_connews(title):
    """查询资讯列表

    :param title:标题 模糊查询
    :return:资讯id
    """
    url = console_HTTP + "/api/con_news/v1/list"

    header = console_JSON


    headers = {}
    headers.update(header)

    token = {"token": getConsoleLogin_token()}
    headers.update(token)  # 将token更新到headers
    pageSize = 20
    currentPage = 1
    status = 0
    paylo = {
        "pageSize": pageSize,
        "currentPage": currentPage,
        "status": status,
        "title": title,
        "code": None
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r_list = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j_list = r_list.json()
    if len(j_list.get("data").get("list")) != 0:
        return j_list.get("data").get("list")[0].get("newsId")
    else:
        raise ValueError(f'{j_list.get("data").get("list")}')