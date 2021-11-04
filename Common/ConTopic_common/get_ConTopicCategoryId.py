import json

import requests

from Common.sign import get_sign
from glo import console_HTTP


def get_ConTopicCategoryId(headers: dict, n: int):
    """获取专题分类id

    :param headers: 带token的headers的参数
    :param n: 下标
    :return: 返回专题id
    """
    url1 = console_HTTP + "/api/con_topic/v1/category_list"

    paylo = {
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url1, headers=headers, data=payload
    )

    j_list = r.json()
    # print(j_list)
    return j_list.get("data").get("list")[n].get("id")

# print(get_ConTopicCategoryId())
