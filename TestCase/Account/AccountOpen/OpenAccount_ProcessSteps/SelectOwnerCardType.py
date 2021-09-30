import requests

from Business.OpenAccount_conmmonPath import path_select_witness_card_type
from Common.get_payload_headers import get_payload
from glo import HTTP


def Select_OwnerCard_Type(headers, ownerCardType):
    """个人证件选择(海外开户)

    :param headers: 请求头headers（带token）
    :param ownerCardType: 开户人证件类型
    :return:
    """
    url_select_witness_card_type = HTTP + path_select_witness_card_type
    paylo_select_witness_card_type = {
        "ownerCardType": ownerCardType
    }

    payload_select_witness_card_type = get_payload(paylo_select_witness_card_type)

    r_select_witness_card_type = requests.session().post(
        url=url_select_witness_card_type, headers=headers, data=payload_select_witness_card_type
    )

    j_select_witness_card_type = r_select_witness_card_type.json()

    # print(j_select_witness_card_type)
    return j_select_witness_card_type
