import requests

from Business.IdentityInformation import Derivative
from Business.OpenAccount_conmmonPath import path_select_account
from Common.get_payload_headers import get_payload
from glo import HTTP


def Select_account(headers, identityTypes):
    """账户选择

    :param headers: 请求头headers（带token）
    :param identityTypes: 身份类型 1-大陆居民 2-我是港澳地区居民 3-我是其他地区居民
    :return:
    """
    url_select_account = HTTP + path_select_account
    if identityTypes == [1]:
        identityType = 1  # 身份类型 1-大陆居民 2-我是港澳地区居民 3-我是其他地区居民
    elif identityTypes == [2]:
        identityType = 2
    else:
        identityType = 3

    cashAccounts = ['1', '2', '3']  # 现金账户 1-港股 2-美股 3-陆股通
    marginAccounts = ['1', '2', '3']  # 融资账户 1-港股 2-美股 3-陆股通
    complianceInfos = [{'option': '1',
                        'select': True},
                       {'option': '2',
                        'select': True},
                       {'option': '3',
                        'select': True},
                       {'option': '4',
                        'select': True,
                        'name': ''},
                       {'option': '5',
                        'select': True,
                        'number': ''},
                       {'option': '6',
                        'select': True,
                        'number': ''},
                       {'option': '7',
                        'select': True,
                        'name': '',
                        'companyName': ''},
                       {'option': '8',
                        'select': True}]  # 合规信息
    if Derivative == "false":  # 是否投资衍生品
        derivative = False
        derivativeInfos = [{"option": "1", "select": False}, {"option": "2", "select": False},
                           {"option": "3", "select": False}]
    else:
        derivative = True
        derivativeInfos = [{"option": "1", "select": True}, {"option": "2", "select": True},
                           {"option": "3", "select": True}]
    paylo_select_account = {
        "identityType": identityType,
        "cashAccounts": cashAccounts,
        "marginAccounts": marginAccounts,
        "complianceInfos": complianceInfos,
        "derivative": derivative,
        "derivativeInfos": derivativeInfos

    }

    payload_select_account = get_payload(paylo_select_account)
    r_select_account = requests.session().post(
        url=url_select_account, headers=headers, data=payload_select_account
    )

    j_select_account = r_select_account.json()
    return j_select_account
