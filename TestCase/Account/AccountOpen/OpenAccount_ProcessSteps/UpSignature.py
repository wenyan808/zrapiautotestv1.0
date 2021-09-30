import requests

from Business.IdentityInformation import signature_imgname
from Business.OpenAccount_conmmonPath import path_signature
from Common.OSS import oss_img
from Common.get_payload_headers import get_payload

from glo import HTTP


def Up_Signature(headers, userId, catalog, url_oss, witnessSignatureUrl=None):
    """上传个人签名

    :param headers: 请求头headers（带token）
    :param userId: 用户id
    :param catalog: 存放目录
    :param url_oss: 上传到阿里云oss url地址
    :param witnessSignatureUrl   见证人电子签名url(港澳地区+其他地区开户时需要)，默认为空
    :return:
    """
    url_signature = HTTP + path_signature
    img_name = signature_imgname
    signatureUrl = list(oss_img("open", img_name, userId, catalog, url_oss, headers))[-1]
    paylo_signature = {
        "signatureUrl": signatureUrl,
        "witnessSignatureUrl": witnessSignatureUrl  # 见证人电子签名url(港澳地区+其他地区开户时需要)
    }
    payload_signature = get_payload(paylo_signature)
    r_signature = requests.session().post(
        url=url_signature, headers=headers, data=payload_signature
    )

    j_signature = r_signature.json()

    # print(j_signature)

    return j_signature
