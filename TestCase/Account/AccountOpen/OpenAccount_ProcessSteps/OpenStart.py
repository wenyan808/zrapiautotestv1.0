import requests

from Business.OpenAccount_conmmonPath import path_start
from Common.get_payload_headers import get_payload
from glo import HTTP


def Open_start(headers: dict):
    """开户准备

    :param headers: 请求头headers（带token）
    :return: 开户准备请求接口的返回josn数据
    """
    url_start = HTTP + path_start
    paylo = {}
    payload = get_payload(paylo)
    r_start = requests.session().post(
        url=url_start, headers=headers, data=payload)

    j_start = r_start.json()
    return j_start
