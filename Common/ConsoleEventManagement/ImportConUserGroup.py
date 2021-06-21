# ImportConUserGroup      用户组导入      /api/con_user_group/v1/import
import json

import requests

from Common.OSS import oss_file
from Common.getConsoleLogin import getConsoleLogin_token
from Common.sign import get_sign
from glo import console_HTTP, console_JSON


def ImportConUserGroup(uploads: str, group_name: str, headers: dict):
    """

    :param uploads: 存放目录   如 user_group
    :param group_name:文件名 如 groupid_phone.xlsx
    :param headers
    :return:url
    """
    url = console_HTTP + "/api/con_user_group/v1/import"
    url1 = console_HTTP + "/api/con_sts/v1/token"

    checkColumn = 1
    groupName = group_name
    catalog = "/Business/Img/"
    url2 = list(oss_file(uploads, group_name, catalog, url1, headers))[-1]

    paylo = {
        "url": url2,
        "checkColumn": checkColumn,
        "groupName": groupName,
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    payload = json.dumps(dict(payload1))

    r_import = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j_import = r_import.json()

    return j_import.get("data").get("groupId"), headers, j_import
