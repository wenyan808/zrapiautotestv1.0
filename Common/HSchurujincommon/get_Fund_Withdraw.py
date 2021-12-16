# get_fund_withdraw    用户绑定银行列表查询    /as_trade/api/bank/v1/list
import json

import requests

from Business.Urlpath.UrlPath_AccountCounter import UrlPath_remit_bank_list, UrlPath_banklist
from Common.sign import get_sign


def get_fund_withdraw(HTTP: str, headers: dict):
    """用户绑定银行列表查询

    :param HTTP:环境地址
    :param headers:交易获取headers（包含交易登录token）
    :return:
    """
    url = HTTP + UrlPath_banklist

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



def get_remit_bank_list(HTTP: str, headers: dict):
    """交易入金汇款银行查询

    :param HTTP:环境地址
    :param headers:交易获取headers（包含交易登录token）
    :return:
    """
    url = HTTP + UrlPath_remit_bank_list

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
