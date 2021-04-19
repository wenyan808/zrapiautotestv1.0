"""console用户登录"""
import re

import requests

from Common.tools.md5 import get_md5

from glo import console_HTTP, console_JSON, loginAccount, password, consoledev_HTTP, consoledev_JSON, loginAccountdev, \
    passworddev


def getConsoleLogin_token():
    """测试环境   获取console登录token

    :return: 返回console登录token
    """
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

def getConsoleLogin_token01(consoleloginAccount, consolepwd):
    """测试环境   获取console登录token

    :param consoleloginAccount: console登录账户
    :param pwd: console密码
    :return: 返回console登录token
    """
    url = console_HTTP + "/api/sys_user/v1/login"
    headers = console_JSON

    loginAccount = consoleloginAccount
    password = consolepwd
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


def getConsoledevLogin_token():
    """开发环境   获取console登录token

    :return: 返回console登录token
    """
    url = consoledev_HTTP + "/api/sys_user/v1/login"
    headers = consoledev_JSON

    # 拼装参数
    paylo = {
        "loginAccount": f"{loginAccountdev}",
        "password": f"{get_md5(passworddev)}"
    }

    rlogindevtoken = requests.session().post(
        url=url, headers=headers, json=paylo
    )

    j = rlogindevtoken.json()
    # print(j)
    token = j.get("data").get("token")
    return token
