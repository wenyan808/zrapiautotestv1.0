import requests

from Business.OpenAccount_conmmonPath import path_risk_disclosure
from Common.get_payload_headers import get_payload
from glo import HTTP


def Risk_Disclosure(headers):
    """风险披露

    :param headers: 请求头headers（带token）
    :return:
    """
    url_risk_disclosure = HTTP + path_risk_disclosure
    paylo_risk_disclosure = {}

    payload_risk_disclosure = get_payload(paylo_risk_disclosure)

    r_risk_disclosure = requests.session().post(
        url=url_risk_disclosure, headers=headers, data=payload_risk_disclosure
    )

    j_risk_disclosure = r_risk_disclosure.json()

    # print(j_risk_disclosure)
    return j_risk_disclosure
