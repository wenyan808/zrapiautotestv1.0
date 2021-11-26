# 查询当前用户的审核数据
import json

import requests

from Business.IdentityInformation import phone6, pwd, phoneArea
from Business.OpenAccount_conmmonPath import path_get_open_status, path_get_open_audit, path_get_audit_item

from Common.getTestLoginToken import getlogintoken
from Common.get_payload_headers import get_headers
from Common.sign import get_sign
from glo import HTTP, JSON2, console_HTTP


def get_open_status(headers):
    """查询开户状态（app使用）

    :param headers:
    :return:
    """
    url = HTTP + path_get_open_status

    # phone = phone6
    # headers = JSON2
    # token = {"token": getlogintoken(phone, pwd, phoneArea)}
    # headers.update(token)
    # # headers=get_headers(JSON2,token)  # 将token更新到headers
    # # print(headers)

    paylo = {
    }
    # print(paylo)
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j = r.json()
    # print(f"\n返回数据结果：{j}")
    return j

# print(get_open_status())


# 查询审核数据
def get_open_audit(headers):
    """查询审核数据

    :param headers: 传入headers带token
    :return:
    """
    url = HTTP + path_get_open_audit
    paylo = {}
    # print(paylo)
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r_audit = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j_audit = r_audit.json()
    # print(f"\n返回数据结果：{j_audit}")
    return j_audit


# 查询审核项
def get_audit_item(headers):
    """查询审核项

    :param headers: console端的headers
    :return:
    """
    url = console_HTTP + path_get_audit_item
    paylo = {}
    # print(paylo)
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r_audit_item = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j_audit_item = r_audit_item.json()
    # print(f"\n返回数据结果：{j_audit}")
    return j_audit_item
