import json

import requests

from Common.sign import get_sign
from glo import console_HTTP


def first_audit_reject(userId: str, auditFails: list, headers: dict, remark: str = None):
    """初审驳回

    :param userId:
    :param remark:
    :param auditFails:
    :param headers:
    :return:
    """
    url1 = console_HTTP + "/api/con_open/v1/first_audit_reject"
    paylo = {
        "userId": f"{userId}",
        "remark": remark,
        "auditFails": auditFails
    }

    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r1 = requests.session().post(
        url=url1, headers=headers, data=payload
    )

    k = r1.json()
    return k


def end_audit_back(headers: dict, userId: str, auditFails: list, remark: str = None):
    """打回初审

    :param userId:用户id
    :param remark:备注
    :param auditFails:审核不通过状态
    :param headers:请求头
    :return:
    """
    url1 = console_HTTP + "/api/con_open/v1/end_audit_back"
    paylo = {
        "userId": f"{userId}",
        "remark": remark,
        "auditFails": auditFails
    }

    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r1 = requests.session().post(
        url=url1, headers=headers, data=payload
    )

    k = r1.json()
    return k


def apply_ca(openId: str = None, headers: dict = None):
    """申请ca认证

    :param userId:用户id
    :param headers:带token的请求头
    :return:
    """
    url1 = console_HTTP + "/api/con_cn_open/v1/apply_ca"
    paylo = {
        "openId": f"{openId}"
    }

    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r1 = requests.session().post(
        url=url1, headers=headers, data=payload
    )

    j1 = r1.json()
    # print(j1)
    return j1
