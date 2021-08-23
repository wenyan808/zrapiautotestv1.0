import requests

from Common.getTestLoginToken import gettestLoginToken
from Common.sign import get_sign
from glo import JSON


def getsecurityToken(url: str, header: dict):
    """

    :param url: url地址
    :param header: header参数
    :return: 返回securityToken的data
    """
    url = url
    headers = header
    body = {}
    json = {
        "sign": get_sign(body)
    }
    # print(json)
    response = requests.session().post(url, headers=headers, json=json)

    res = response.json().get("data")
    # print(res)
    return res


# url = "http://192.168.1.241/as_common/api/sts/v1/token"
# header = {} header.update(JSON)
# # body = {}
# token = {"token": gettestLoginToken()}
# header.update(token)
#
# print(getsecurityToken(url,header))
