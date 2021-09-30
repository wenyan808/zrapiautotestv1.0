import requests

from Business.IdentityInformation import img_filename
from Business.OpenAccount_conmmonPath import path_live_body
from Common.OSS import oss_img
from Common.get_payload_headers import get_payload
from glo import HTTP


def Live_Body(headers, userId, catalog, url_oss):
    """活体人脸核身

    :param headers: 请求头headers（带token）
    :param userId: 用户id
    :param catalog: 存放目录
    :param url_oss: 上传到阿里云oss url地址
    :return:
    """
    url_live_body = HTTP + path_live_body
    img_name = img_filename
    videoUrl = list(oss_img("open", img_name, userId, catalog, url_oss, headers))[-1]

    paylo_live_body = {
        "videoUrl": videoUrl
    }

    payload_live_body = get_payload(paylo_live_body)

    r_live_body = requests.session().post(
        url=url_live_body, headers=headers, data=payload_live_body
    )

    j_live_body = r_live_body.json()

    # print(j_live_body)
    return j_live_body