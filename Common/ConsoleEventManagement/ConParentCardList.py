import json

import requests

from Common.sign import get_sign
from glo import console_HTTP


def get_ConParentCardId(headers: dict, n: int):
    """获取parentCardId

    :param headers:请求头
    :param n: 从列表中获取parentCardId的下标值，一般从0开始
    :return: 返回parentCardId
    """
    url = console_HTTP + "/api/con_parent_card/v1/list"
    paylo = {}
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
    return j.get("data").get("list")[n].get("parentCardId")


# print(ConParentCardList())


def get_distributeIdlist(headers, n: int):
    """获取distributeId

    :param headers: 请求头带token
    :param n: 从列表中获取distributeId的下标值，一般从0开始
    :return: 返回distributeId
    """
    url = console_HTTP + "/api/con_distribute/v1/list"
    paylo = {}
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
    return j.get("data").get("list")[n].get("distributeId")


def getconCardid(headers: dict, n: int):
    """获取子卡券id

    :param headers: 请求头带token
    :param n: 从列表中获取distributeId的下标值，一般从0开始
    :return: 返回子卡券id
    """
    url = console_HTTP + "/api/con_card/v1/list"
    paylo = {}
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
    return j.get("data").get("list")[n].get("cardId")


def get_voucherId(headers: dict, voucherName: str, n: int):
    """获取voucherId（权益ID）

    :param headers: 请求头带token
    :param voucherName: 权益名称
    :param n: 从列表中下标值，一般从0开始
    :return: voucherId
    """
    url = console_HTTP + "/api/con_voucher/v1/list"
    paylo = {"voucherName": voucherName}
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
    return j.get("data").get("list")[n].get("voucherId")


def get_activityId(headers: dict, activityName: str, showStatus: int, n: int):
    """获取活动id

    :param headers:带token的headers
    :param activityName:活动名称
    :param showStatus:状态（全部-0  等待中-1 执行中-2 已结束-3 已停用-4 终止派发-5）
    :param n:下标
    :return:活动id
    """
    url = console_HTTP + "/api/con_activity/v1/list"

    paylo = {
        "activityName": activityName,
        "showStatus": showStatus
    }
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
    return j.get("data").get("list")[n].get("activityId")
