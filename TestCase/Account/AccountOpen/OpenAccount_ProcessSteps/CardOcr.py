import requests

from Business.IdentityInformation import img_name01, img_name02
from Business.OpenAccount_conmmonPath import path_card_ocr
from Common.OSS import oss_img
from Common.get_payload_headers import get_payload
from glo import HTTP


def Card_Ocr(headers, userId, catalog, url_oss, cardType):
    """上传身份证件照片正反面

    :param headers: 请求头headers（带token）
    :param userId: 用户id
    :param catalog: 存放目录
    :param url_oss: 上传到阿里云oss url地址
    :param cardType:证件类型
    :return:
    """
    url_card_ocr = HTTP + path_card_ocr
    # 上传证件照OCR-正面(v2)
    img_name0 = img_name01
    # catalog = "/Business/UserFileUp/"
    url0 = list(oss_img("open", img_name0, userId, catalog, url_oss, headers))[-1]
    cardSide0 = 1  # 1-正面 2-反面
    paylo_card_ocr_1 = {
        "url": url0,
        "cardType": cardType,
        "cardSide": cardSide0
    }

    payload_card_ocr_1 = get_payload(paylo_card_ocr_1)

    r0 = requests.session().post(
        url=url_card_ocr, headers=headers, data=payload_card_ocr_1
    )

    j_card_ocr_1 = r0.json()
    # 上传证件照OCR-反面(v2)
    img_name1 = img_name02
    # catalog = "/Business/UserFileUp/"
    url1 = list(oss_img("open", img_name1, userId, catalog, url_oss, headers))[-1]
    cardSide1 = 2
    paylo_card_ocr_2 = {
        "url": url1,
        "cardType": cardType,
        "cardSide": cardSide1
    }

    payload_card_ocr_2 = get_payload(paylo_card_ocr_2)

    r1 = requests.session().post(
        url=url_card_ocr, headers=headers, data=payload_card_ocr_2
    )

    j_card_ocr_2 = r1.json()
    return j_card_ocr_1, j_card_ocr_2
