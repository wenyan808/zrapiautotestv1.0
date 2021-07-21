# Add_Voucher_ParentCard
import json

import requests

from Common.ConsoleEventManagement.ImportConUserGroup import ImportConUserGroup
from Common.get_time_stamp import getTimeTostamp
from Common.sign import get_sign
from glo import console_HTTP


def Add_Voucher(headers: dict):
    """新增权益"""
    url = console_HTTP + "/api/con_voucher/v1/add"
    paylo = {
        "voucherName": "高级行情-美股LV1权益",
        "type": 1,
        "description": "高级行情-美股LV1活动卡券",
        "usedType": 1,
        "voucherTotalNum": 1000
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url, headers=headers, data=payload
    )
    j = r.json()
    # print(j)
    return j


def Add_ParentCard(headers: dict, voucherIds: list):
    """新增母卡券

    :param headers:请求头
    :param voucherIds:权益ids string[]
    :return:
    """
    url = console_HTTP + "/api/con_parent_card/v1/add"

    activationStartTime = int(getTimeTostamp(1))  # 激活开始时间
    activationEndTime = int(getTimeTostamp(20))  # 激活结束时间
    validStartTime = int(getTimeTostamp(5))
    # 权益时间段开始时间
    alidEndTime = int(getTimeTostamp(30))
    # 权益时间段结束时间
    paylo = {
        "parentCardName": "开通美股账户即可赠送一年VIP服务",
        "groupId": list(ImportConUserGroup("user_group", "groupid_phone.xlsx", headers))[0],
        "type": 1,
        "voucherIds": voucherIds,
        "parentCardTotalNum": 1000,
        "activationType": 1,
        "activationStartTime": activationStartTime,
        "activationEndTime": activationEndTime,
        "validType": 2,
        "validDays": 30,
        "validStartTime": validStartTime,
        "validEndTime": alidEndTime,
        "receiveType": 2,
        "receiveMode": 1,
        "receiveNum": 1,
        "receiveInterval": 1

    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url, headers=headers, data=payload
    )
    j = r.json()
    # print(j)
    return j


def add_activity(headers: dict, parentCardId: str):
    """新增活动

    :param headers:带token的headers
    :param parentCardId: 母卡券id
    :return:
    """
    url = console_HTTP + "/api/con_activity/v1/add"

    publishStartTime = int(getTimeTostamp(1))  # 活动发布开始时间
    publishEndTime = int(getTimeTostamp(30))  # 活动发布结束时间

    paylo = {
        "activityName": "新用户开通美股账户即可赠送一年VIP服务",
        "virtual": 1,
        "activityType": 1,
        "groupId": list(ImportConUserGroup("user_group", "groupid_phone.xlsx", headers))[0],
        "ad": 0,
        "publishStartTime": publishStartTime,
        "publishEndTime": publishEndTime,
        "activityParentCard": [{
            "parentCardId": parentCardId,
            "totalNum": 1000,
        }],
    }
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url, headers=headers, data=payload
    )
    j = r.json()
    # print(j)
    return j
