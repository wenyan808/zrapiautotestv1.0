# 新增绑定银行卡    /as_trade/api/bank/v1/save
import json

import requests

from Business.IdentityInformation import add_bankname_list
from Common.sign import get_sign


def add_save_bank(HTTP: str, headers: dict, bankAccountDocument: str, bindBankId: str, i: int, j: int):
    """新增绑定银行卡

    :param HTTP:环境地址
    :param headers:交易获取headers（包含交易登录token）
    :param bankAccountDocument: 上传银行账户凭证url 多张照片以|隔开   string
    :param bindBankId:银行id
    :param i :下标
    :param j :下标
    :return:
    """
    url = HTTP + "/as_trade/api/bank/v1/save"
    bankRegion = add_bankname_list.get("YHXX_list")[i].get("bankRegion")
    bankName = add_bankname_list.get("YHXX_list")[i].get("bankRegion").get("list")[j].get("bankName")
    supportMoneyType = add_bankname_list.get("YHXX_list")[i].get("bankRegion").get("list")[j].get("supportMoneyType")
    bankAccount = add_bankname_list.get("YHXX_list")[i].get("bankRegion").get("list")[j].get("bankAccount")
    rtgsCode = add_bankname_list.get("YHXX_list")[i].get("bankRegion").get("list")[j].get("rtgsCode")
    swift = add_bankname_list.get("YHXX_list")[i].get("bankRegion").get("list")[j].get("swift")
    bankAddress = add_bankname_list.get("YHXX_list")[i].get("bankRegion").get("list")[j].get("bankAddress")
    payeeAddress = add_bankname_list.get("YHXX_list")[i].get("bankRegion").get("list")[j].get("payeeAddress")

    paylo = {
        "bankRegion": bankRegion,
        "bankName": bankName,
        "supportMoneyType": supportMoneyType,
        "bankAccount": bankAccount,
        "rtgsCode": rtgsCode,
        "swift": swift,
        "bankAddress": bankAddress,
        "payeeAddress": payeeAddress,
        "bankAccountDocument": bankAccountDocument,
        "bindBankId": bindBankId
    }

    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r_add = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j_add = r_add.json()
    return j_add
