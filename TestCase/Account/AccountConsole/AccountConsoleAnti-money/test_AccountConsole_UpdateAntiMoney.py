# test_AccountConsole_UpdateAntiMoney          修改反洗钱          /api/con_open/v1/update_anti_money
"""
@File  ：test_AccountConsole_UpdateAntiMoney.py
@Author: yishouquan
@Time  : 2020/8/11
@Desc  :  获取反洗钱信息
"""
import json
import time

import allure
import pytest

from Business.IdentityInformation import identityTypes
from Business.global_ossurl import oss_consoleurl
from Common.Accountcommon.getAccountConsoleList import getAccountConsoleList, getAntiMoney, getAccountConsoleDetail
from Common.OSS import oss_img
from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import get_time_stamp13

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_json import get_json

from glo import console_HTTP, console_JSON, BASE_DIR, loginAccount_phone


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('修改反洗钱')
class TestAccountConsoleUpdateAntiMoney():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        # login()  # 调用登录接口通过token传出来
        cls.url = console_HTTP + "/api/con_open/v1/update_anti_money"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info', get_json(BASE_DIR +
                                              r"/TestData/AccountConsoledata/test_AccountConsole_UpdateAntiMoney.json"))
    def test_AccountConsole_UpdateAntiMoney(self, info):

        headers = {}
        headers.update(console_JSON)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        # url = console_HTTP + "/as_market/api/server_info/v1/now"
        supplierType = info.get("supplierType")  # 信息供应商 1.其他
        investigationTime = get_time_stamp13()  # 调查时间(时间戳)
        # print(investigationTime)
        investigationResultType = info.get("investigationResultType")  # 调查结果 1.Others 2.No Matches
        # 3.All matches resolved 4.Confirm unmatched via phone 5.Confirm matched via phone
        # investigationFiles = "[{\"name\": \"文件名称\", \"url\": \"文件url\"}]"  # 调查文件[{"name":"文件名称",   "url":"文件url"}]
        remark = info.get("remark")  # 备注
        riskLevel = info.get("riskLevel")  # 反洗钱风险级别1.低 2.中 3.高
        supplierOtherDesc = info.get("supplierOtherDesc")  # 信息供应商为1.其他，手动输入
        investigationResultOtherDesc = info.get("investigationResultOtherDesc")  # 调查结果为1.Others，手动输入

        phone = loginAccount_phone
        # identityTypes = [1]  # 身份类型 1-大陆居民 2-我是港澳地区居民 3-我是其他地区居民 海外居民，传入2,3
        status = 3  # 状态，为空时查询所有数据 1、待客户修改 2、初审列表 3、终审列表 4、已通过 5、已拒绝
        # print(getAccountConsoleList(headers, identityTypes, status, phone))

        openOrderId = getAccountConsoleList(headers, identityTypes, status).get("data").get("list")[0].get(
            "openOrderDTO").get("openOrderId")
        # print(openOrderId)
        openId = getAccountConsoleDetail(headers, openOrderId).get("data").get("openInfoDTO").get("openId")  # 开户id
        url2 = console_HTTP + oss_consoleurl
        userId = openId
        catalog = "/Business/UserFileUp/"
        # Files_name = "zhanghupingzheng2.JPG"
        # 将图片上传至oss阿里云中返回url
        Files_url = list(oss_img("open", Files_name, userId, catalog, url2, headers))[-1]
        investigationFiles = f"[{'name': '{Files_name}', 'url':'{Files_url}'}]"  # 调查文件[{"name":"文件名称",   "url":"文件url"}]
        amlId = getAntiMoney(headers, openOrderId).get("data")[0].get("amlId")  # 反洗钱记录id
        # print(amlId)
        paylo = {
            "supplierType": supplierType,
            "investigationTime": investigationTime,
            "investigationResultType": investigationResultType,
            "investigationFiles": investigationFiles,
            "remark": remark,
            "riskLevel": riskLevel,
            "supplierOtherDesc": supplierOtherDesc,
            "investigationResultOtherDesc": investigationResultOtherDesc,
            "amlId": amlId
        }

        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=self.url, headers=headers, data=payload, title="修改反洗钱"
        )
        j = r.json()
        # print(f"\n请求地址：{self.url}"
        #       f"\nbody参数：{payload}"
        #       f"\n请求头部参数：{headers}"
        #       f"\n返回数据结果：{j}")
        assert r.status_code == 200
        try:
            assert j.get("msg") == "ok"
            assert j.get("code") == "000000"


        except:
            raise AssertionError(
                f"\n请求地址：{self.url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}")
