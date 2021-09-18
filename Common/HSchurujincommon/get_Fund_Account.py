# /as_trade/api/fund/v1/get_fund_account                    获取用户资金账户列表
import json

import requests

from Common.sign import get_sign


def get_fund_account(HTTP: str, headers: dict):
    """获取用户资金账户列表

    :param HTTP:环境地址
    :param headers:交易获取headers（包含交易登录token）
    :return:
    """
    url = HTTP + "/as_trade/api/fund/v1/get_fund_account"

    paylo = {

    }

    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r_list = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j_list = r_list.json()
    return j_list
