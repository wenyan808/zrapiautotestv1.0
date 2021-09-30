import requests

from Business.OpenAccount_conmmonPath import path_risk_score_confirm
from Common.get_payload_headers import get_payload
from glo import HTTP


def RiskScoreConfirm(headers):
    """确定评估结果

    :param headers: 请求头headers（带token）
    :return:
    """
    url_risk_score_confirm = HTTP + path_risk_score_confirm
    paylo_risk_score_confirm = {}

    payload_risk_score_confirm = get_payload(paylo_risk_score_confirm)

    r_risk_score_confirm = requests.session().post(
        url=url_risk_score_confirm, headers=headers, data=payload_risk_score_confirm
    )

    j_risk_score_confirm = r_risk_score_confirm.json()

    # print(j_risk_score_confirm)
    return j_risk_score_confirm
