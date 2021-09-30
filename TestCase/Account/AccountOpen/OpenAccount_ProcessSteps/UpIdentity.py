import requests

from Business.IdentityInformation import cardNo, cardBirth, bankCard, cardName, cardLastNamePinyin, cardNamePinyin, \
    address, mailbox, bankCardNo, bankCardName, bankCardPhone, nationality, sex, homeAddress_img_Name
from Business.OpenAccount_conmmonPath import path_identity
from Common.OSS import oss_img
from Common.get_payload_headers import get_payload
from glo import HTTP, phoneArea


def Up_Identity(headers, userId, catalog, url_oss, identityTypes):
    """

    :param headers: 请求头headers（带token）
    :param userId: 用户id
    :param catalog: 存放目录
    :param url_oss: 上传到阿里云oss url地址
    :param identityTypes:身份类型 1-大陆居民 2-我是港澳地区居民 3-我是其他地区居民 海外居民，传入2,3
    :return:
    """
    url_identity = HTTP + path_identity
    taxation = phoneArea + cardNo
    birth = cardBirth
    # catalog = "/Business/UserFileUp/"
    if identityTypes == [1]:
        img_name_bankCard = bankCard
        bankCardUrl = list(oss_img("open", img_name_bankCard, userId, catalog, url_oss, headers))[-1]
        # sex = 0  # 用户性别    1-男 0-女
        paylo_identity = {
            "cardName": cardName,
            "cardNo": cardNo,
            "cardLastNamePinyin": cardLastNamePinyin,
            "cardNamePinyin": cardNamePinyin,
            "address": address,
            "mailbox": mailbox,
            "bankCardNo": bankCardNo,
            "bankCardName": bankCardName,
            "bankCardUrl": bankCardUrl,
            "bankCardPhone": bankCardPhone,
            "taxation": taxation,
            "nationality": nationality,
            "sex": sex,
            "birth": birth
        }
    else:
        homeAddress = address  # 同通讯地址

        img_name = homeAddress_img_Name

        homeAddressUrl = list(oss_img("open", img_name, userId, catalog, url_oss, headers))[-1]
        # sex = 0  # 用户性别    1-男 0-女
        paylo_identity = {
            "cardName": cardName,
            "cardNo": cardNo,
            "cardLastNamePinyin": cardLastNamePinyin,
            "cardNamePinyin": cardNamePinyin,
            "address": address,
            "mailbox": mailbox,
            "taxation": taxation,
            "homeAddress": homeAddress,
            "homeAddressUrl": homeAddressUrl,
            "nationality": nationality,
            "sex": sex,
            "birth": birth
        }

    payload_identity = get_payload(paylo_identity)

    r_identity = requests.session().post(
        url=url_identity, headers=headers, data=payload_identity, title="上传身份信息"
    )

    j_identity = r_identity.json()

    # print(j_identity)
    return j_identity
