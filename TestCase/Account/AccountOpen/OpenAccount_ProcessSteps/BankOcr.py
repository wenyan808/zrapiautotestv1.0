import requests

from Business.IdentityInformation import bankCard
from Business.OpenAccount_conmmonPath import path_bank_ocr
from Common.OSS import oss_img
from Common.get_payload_headers import get_payload
from glo import HTTP


def BankOcr(headers, userId, catalog, url_oss):
    """上传银行卡

    :param headers: 请求头headers（带token）
    :param userId: 用户id
    :param catalog: 存放目录
    :param url_oss: 上传到阿里云oss url地址
    :return:
    """
    url_bank_ocr = HTTP + path_bank_ocr
    img_name = bankCard
    # catalog = "/Business/UserFileUp/"
    bankCardUrl = list(oss_img("open", img_name, userId, catalog, url_oss, headers))[-1]
    paylo_bank_ocr = {
        "bankCardUrl": bankCardUrl
    }
    payload_bank_ocr = get_payload(paylo_bank_ocr)

    r_bank_ocr = requests.session().post(
        url=url_bank_ocr, headers=headers, data=payload_bank_ocr
    )

    j_bank_ocr = r_bank_ocr.json()
    return j_bank_ocr
