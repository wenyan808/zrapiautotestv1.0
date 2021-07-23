import requests

from Common.sign import get_sign
from Common.tools.md5 import get_md5
from glo import HTTP, JSON, loginAccount_phone, Accountlogin_password, phoneArea


def GetLoginAccountToken():
    """
    测试环境开户登录账号
    :return: token
    """
    loginAccount = loginAccount_phone
    password = Accountlogin_password
    url = HTTP + "/as_user/api/user_account/v1/user_login_pwd"
    headers = JSON

    # 拼装参数
    paylo = {
        "phone": f"{loginAccount}",
        "loginPassword": f"{get_md5(password)}",
        "phoneArea": phoneArea
    }
    sign1 = {"sign": get_sign(paylo)}
    paylo.update(sign1)

    rlogintoken = requests.session().post(
        url=url, headers=headers, json=paylo
    )

    j = rlogintoken.json()
    # print(j)
    token = j.get("data").get("token")
    return token


# print(GetLoginAccountToken())


def getLoginAccountToken(phone: str, password: str):
    """
    测试环境开户登录账号
    :param phone:   手机号
    :param password:   未加密的密码
    :return: token
    """
    loginAccount = phone
    password = password
    url = HTTP + "/as_user/api/user_account/v1/user_login_pwd"
    headers = JSON

    # 拼装参数
    paylo = {
        "phone": f"{loginAccount}",
        "loginPassword": f"{get_md5(password)}",
        "phoneArea": phoneArea
    }
    sign1 = {"sign": get_sign(paylo)}
    paylo.update(sign1)

    rlogintoken = requests.session().post(
        url=url, headers=headers, json=paylo
    )

    j = rlogintoken.json()
    # print(j)
    token = j.get("data").get("token")
    return token
