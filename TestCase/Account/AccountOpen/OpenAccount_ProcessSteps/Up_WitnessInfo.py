import requests

from Business.IdentityInformation import witnessPracticeimgname, witnessPracticePerson_imgname, witnessCardNo, \
    witnessCardName, witnessPracticeType, witnessPracticeOther, witnessPracticeNo, witnessLastNamePinyin, \
    witnessNamePinyin
from Business.OpenAccount_conmmonPath import path_witness
from Common.OSS import oss_img
from Common.get_payload_headers import get_payload
from glo import HTTP


def Up_Witness_Info(headers, userId, catalog, url_oss):
    """见证人信息（海外开户）

    :param headers: 请求头headers（带token）
    :param userId: 用户id
    :param catalog: 存放目录
    :param url_oss: 上传到阿里云oss url地址
    :return:
    """
    url_witness = HTTP + path_witness
    img_name = witnessPracticeimgname
    witnessPracticeFrontUrl = list(oss_img("open", img_name, userId, catalog, url_oss, headers))[-1]
    # witnessPracticeFrontUrl = witnessPracticeFrontUrl  # 见证人执业证书正面url
    img_name1 = witnessPracticePerson_imgname
    witnessPracticePersonUrl = list(oss_img("open", img_name1, userId, catalog, url_oss, headers))[-1]
    # witnessPracticePersonUrl = witnessPracticePersonUrl  # 见证人执业证书人像面url
    paylo_witness = {
        "witnessCardNo": witnessCardNo,
        "witnessCardName": witnessCardName,
        "witnessPracticeType": witnessPracticeType,
        "witnessPracticeOther": witnessPracticeOther,
        "witnessPracticeNo": witnessPracticeNo,
        "witnessPracticeFrontUrl": witnessPracticeFrontUrl,
        "witnessPracticePersonUrl": witnessPracticePersonUrl,
        "witnessLastNamePinyin": witnessLastNamePinyin,
        "witnessNamePinyin": witnessNamePinyin
    }

    payload_witness = get_payload(paylo_witness)

    r_witness = requests.session().post(
        url=url_witness, headers=headers, data=payload_witness
    )

    j_witness = r_witness.json()

    # print(j_witness)
    return j_witness
