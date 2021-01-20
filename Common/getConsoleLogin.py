"""console用户登录"""
import re

import requests

from Common.tools.md5 import get_md5

from glo import console_HTTP, console_JSON, loginAccount, password


def getConsoleLogin_token():
    url = console_HTTP + "/api/sys_user/v1/login"
    headers = console_JSON

    # 拼装参数
    paylo = {
        "loginAccount": f"{loginAccount}",
        "password": f"{get_md5(password)}"
    }

    rlogintoken = requests.session().post(
        url=url, headers=headers, json=paylo
    )

    j = rlogintoken.json()
    # print(j)
    token = j.get("data").get("token")
    return token


# print(getConsoleLogin_token())
