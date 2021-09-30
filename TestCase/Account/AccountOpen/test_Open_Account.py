"""开户的整体流程"""
import json
import logging
import random

import allure
import pytest

from Business.IdentityInformation import phone6, pwd, identityTypes, ownerCardType, cardType
from Business.global_ossurl import oss_appurl
from Common.OSS import oss_img
from Common.show_sql import showsql
from Common.Accountcommon.getLoginAccountToken import getLoginAccountToken
from Common.get_payload_headers import get_headers

from Common.requests_library import Requests
from TestCase.Account.AccountOpen.OpenAccount_ProcessSteps.BankOcr import BankOcr
from TestCase.Account.AccountOpen.OpenAccount_ProcessSteps.CardOcr import Card_Ocr
from TestCase.Account.AccountOpen.OpenAccount_ProcessSteps.LiveBody import Live_Body
from TestCase.Account.AccountOpen.OpenAccount_ProcessSteps.LiveBodyCount import LiveBodyCount
from TestCase.Account.AccountOpen.OpenAccount_ProcessSteps.OpenStart import Open_start
from TestCase.Account.AccountOpen.OpenAccount_ProcessSteps.RiskDisclosure import Risk_Disclosure
from TestCase.Account.AccountOpen.OpenAccount_ProcessSteps.RiskScoreConfirm import RiskScoreConfirm
from TestCase.Account.AccountOpen.OpenAccount_ProcessSteps.SelectAccount import Select_account
from TestCase.Account.AccountOpen.OpenAccount_ProcessSteps.SelectOwnerCardType import Select_OwnerCard_Type
from TestCase.Account.AccountOpen.OpenAccount_ProcessSteps.UpIdentity import Up_Identity
from TestCase.Account.AccountOpen.OpenAccount_ProcessSteps.UpSignature import Up_Signature
from TestCase.Account.AccountOpen.OpenAccount_ProcessSteps.Up_WitnessInfo import Up_Witness_Info
from TestCase.Account.AccountOpen.OpenAccount_ProcessSteps.UpdateFs import UpdateFs
from TestCase.Account.AccountOpen.OpenAccount_ProcessSteps.UpdateInvest import Update_Invest

from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('开户app_开户流程')
class TestOpenAccount():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_OpenAccount(self):
        url_oss = HTTP + oss_appurl
        catalog = "/Business/UserFileUp/"
        userId1 = showsql(
            '192.168.1.237', 'root', '123456', "user_account",
            f"select user_id from t_user_account where `phone`= '{phone6}';"
        )
        userId = list(list(userId1)[0])[0]
        # 未开户账号登录成功获取headers
        token = {"token": getLoginAccountToken(phone6, pwd)}
        headers = get_headers(JSON, token)
        # print(headers)
        # 第一步:准备开户
        Open_start(headers)
        # 第二步：账户选择
        Select_account(headers, identityTypes)
        # 第三步：财务状况
        UpdateFs(headers)
        # 第四步：投资经验
        Update_Invest(headers)
        # 第五步：确定评估结果
        RiskScoreConfirm(headers)
        # 第六步：风险披露
        Risk_Disclosure(headers)

        # print(j_risk_disclosure)
        if identityTypes == [1]:
            # 第七步：证件照OCR(v2)
            # cardType = "0101"
            """证件类型： 
                中国内地居民（01） 
                    内地身份证(0101)
    
                香港永久居民（02）
                    香港永久居民身份证（0201）
    
                香港非永久居民(03)
                    香港临时居民身份证（0301）
                    大陆身份证（0302）
                    签证身份书（0303）
                    特区护照（0304）
    
                澳门永久居民（04）	 
                    澳门永久居民身份证（0401）
    
                澳门非永久居民(05)	
                    澳门临时居民身份证(0501)
                    大陆身份证(0502)
                    澳门旅游证(0503)
                    特区护照(0504)
    
                其他（06）
                    护照（0601）
    
                见证人信息（07）
                    内地(0701)
                    香港(0702)
                    澳门(0703)
                    其他地区(0704)
            """
            Card_Ocr(headers, userId, catalog, url_oss, cardType)
            # 第八步1：上传身份信息
            Up_Identity(headers, userId, catalog, url_oss, identityTypes)
            # 第八步2：银行卡OCR
            BankOcr(headers, userId, catalog, url_oss)
            # 活体人脸核身
            Live_Body(headers, userId, catalog, url_oss)
            # 获取活体校验次数
            LiveBodyCount(headers)
            # 个人签名
            Up_Signature(headers, userId, catalog, url_oss)

        else:
            pass
            # 个人信息
            # 1.个人证件选择(海外开户)
            Select_OwnerCard_Type(headers, ownerCardType)
            # 核对信息(上传身份信息,住宅证明)
            Up_Identity(headers, userId, catalog, url_oss, identityTypes)
            # 见证人信息
            Up_Witness_Info(headers, userId, catalog, url_oss)
            # 个人签名
            img_name1 = witnessSignaturename
            witnessSignatureUrl = list(oss_img("open", img_name1, userId, catalog, url_oss, headers))[-1]
            Up_Signature(headers, userId, catalog, url_oss, witnessSignatureUrl)
