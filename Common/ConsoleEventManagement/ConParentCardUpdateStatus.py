import json

import requests

from Common.sign import get_sign
from glo import console_HTTP


def UpdateStatus_conparentcard(headers: dict, parentCardId: str, status: int):
    """

    :param headers: 请求头
    :param parentCardId: 母卡券id
    :param status:修改状态
    :return:
    """
    url = console_HTTP + "/api/con_parent_card/v1/update_status"

    paylo = {"parentCardId": parentCardId,
             "status": status}
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
