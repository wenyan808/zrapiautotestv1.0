import requests

from Business.OpenAccount_conmmonPath import path_live_body_count
from Common.get_payload_headers import get_payload
from glo import HTTP


def LiveBodyCount(headers):
    """获取活体校验次数

    :param headers: 请求头headers（带token）
    :return:
    """
    url = HTTP + path_live_body_count
    paylo_live_body_count = {}
    payload_live_body_count = get_payload(paylo_live_body_count)
    r_live_body_count = requests.session().post(
        url=url, headers=headers, data=payload_live_body_count, title="获取活体校验次数"
    )

    j_live_body_count = r_live_body_count.json()
    # print(j_live_body_count)
    return j_live_body_count
