import json

import requests

from Common.get_time_stamp import gettoday
from Common.sign import get_sign
from glo import console_HTTP


def add_conVoucher(header: dict):
    """新增权益

    :return:
    """
    url = console_HTTP + "/api/con_voucher/v1/add"
    headers = header

    paylo = {
        "voucherName": "新增高级行情-美股LV1权益" + str(gettoday()),
        "type": 1,
        "description": "高级行情-美股LV1活动卡券",
        "usedType": 1,
        "voucherTotalNum": 1000
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
