import requests

from Business.IdentityInformation import investLossScope, investReserveFund, investAmount, investTime, investTarget, \
    investRate, investOther, investWarrants, investFixed, investFund, investBond
from Business.OpenAccount_conmmonPath import path_update_invest
from Common.get_payload_headers import get_payload
from glo import HTTP


def Update_Invest(headers):
    """投资经验

    :param headers: 请求头headers（带token）
    :return:
    """
    url_update_invest = HTTP + path_update_invest
    paylo_update_invest = {
        "investBond": investBond,
        "investFund": investFund,
        "investFixed": investFixed,
        "investWarrants": investWarrants,
        "investOther": investOther,
        "investRate": investRate,
        "investTarget": investTarget,
        "investTime": investTime,
        "investAmount": investAmount,
        "investReserveFund": investReserveFund,
        "investLossScope": investLossScope
    }

    payload_update_invest = get_payload(paylo_update_invest)

    r_update_invest = requests.session().post(
        url=url_update_invest, headers=headers, data=payload_update_invest
    )

    j_update_invest = r_update_invest.json()
    return j_update_invest
