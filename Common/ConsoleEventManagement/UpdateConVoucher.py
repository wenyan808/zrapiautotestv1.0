import json

import requests

from Common.getConsoleLogin import getConsoleLogin_token
from Common.sign import get_sign
from glo import console_HTTP, console_JSON


def updateconvoucher(voucherId: str, applyType: int, applyNum: int, stop: bool):
    """修改权益状态

    :param voucherId:卡券ID
    :param applyType:申请类型:1、增加库存 2、减少库存
    :param applyNum:申请数量
    :param stop:是否停用权益(true-停用权益)
    :return:返回相应的修改/停用权益
    """
    url = console_HTTP + "/api/con_voucher/v1/update"
    header = console_JSON
    headers = {}
    headers.update(header)
    token = {"token": getConsoleLogin_token()}
    headers.update(token)  # 将token更新到headers

    paylo = {
        "voucherId": voucherId,
        "applyType": applyType,
        "applyNum": applyNum,
        "stop": stop
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
    return j
