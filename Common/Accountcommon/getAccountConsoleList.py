import json

import requests

from Common.sign import get_sign
from glo import console_HTTP


def getAccountConsoleList(headers: dict, identityTypes: list, status: int = None, phone: str = None):
    """获取开户console列表（根据状态status获取相应的列表）

    :param headers:请求参数带token
    :param identityTypes:   身份类型 1-大陆居民 2-我是港澳地区居民 3-我是其他地区居民 海外居民，传入2,3 如：[2, 3]海外
    :param status:状态，为空时查询所有数据 1、待客户修改 2、初审列表 3、终审列表 4、已通过 5、已拒绝
    :param phone:手机号,为空时查询所相应的列表数据
    :return:返回相应的列表
    """
    url = console_HTTP + "/api/con_open/v1/list"

    paylo = {
        "currentPage": 1,
        "pageSize": 20,
        "identityTypes": identityTypes,
        "status": status,
        "phone": phone
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
    # print(j)
    return j
