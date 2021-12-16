# test_HSChuRuJin_FundDeposit      存入资金    /as_trade/api/fund/v1/deposit
import json
import random

import allure
import pytest

from Business.Urlpath.UrlPath_AccountCounter import UrlPath_fund_deposit, UrlPath_remit_bank_list
from Business.global_ossurl import oss_appurl
from Common.Accountcommon.accountAuth import AccountAuth
from Common.HSchurujincommon.get_Fund_Account import get_fund_account
from Common.HSchurujincommon.get_Fund_Withdraw import get_remit_bank_list
from Common.OSS import oss_img
from Common.getTestLoginToken import gettestLoginToken
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_json import get_json

from glo import JSON_dev, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_存入资金')
class TestHSChuRuJinFundDeposit():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/HSChurujindata/test_HSChuRuJinFundDeposit.json"))
    def test_HSChuRuJinFundDeposit(self, info):
        login_list = list(AccountAuth())
        http = login_list[-1]
        headers = login_list[1]
        # url_remit_bank_list = http + UrlPath_remit_bank_list
        url_fund_deposit = http + UrlPath_fund_deposit
        url2 = http + oss_appurl
        """交易入金汇款银行查询"""
        k = get_remit_bank_list(http, headers)

        transferType = info.get("transferType")  # 转账方式 1-网银汇款 2-ATM转账 3-柜台汇款 4-支票 5-FPS转数快
        occurBalance = random.randint(10000, 10000000)  # 存入资金 (随机取1000到1亿间的整数)
        moneyType = info.get("moneyType")  # 币种类别:HKD,CNY,USD

        bankId = k.get("data")[0].get("id")  # 银行id
        # print(bankId)
        # 如果转账方式为FPS转数快时，bankId取返回数据data列表下标为1的id
        if transferType == 5:
            bankId = k.get("data")[1].get("id")
        userId = login_list[0].get("data").get("userId")
        img_name = "huikuanpingzheng.png"
        img_name2 = "huikuanpingzheng2.jpg"
        img_name3 = "zhanghupingzheng.jpg"
        img_name4 = "zhanghupingzheng2.JPG"
        catalog = "/Business/UserFileUp/"
        # 将图片上传至oss阿里云中返回url
        a1_imgurl = list(oss_img("open", img_name, userId, catalog, url2, headers))[-1]
        a2_imgurl = list(oss_img("open", img_name2, userId, catalog, url2, headers))[-1]

        paymentDocument = f"{a1_imgurl}|{a2_imgurl}"  # 上传汇款凭证url 多张图片以|分隔
        # print(paymentDocument)
        b1_imgurl = list(oss_img("open", img_name3, userId, catalog, url2, headers))[-1]
        b2_imgurl = list(oss_img("open", img_name4, userId, catalog, url2, headers))[-1]
        bankAccountDocument = f"{b1_imgurl}|{b2_imgurl}"  # 上传银行账户凭证url 多张图片以|分隔
        # print(bankAccountDocument)
        fundAccount = get_fund_account(http, headers).get("data")[0].get("fundAccount")  # 资金账号
        # print(fundAccount)
        boby = {
            "moneyType": moneyType,
            "transferType": transferType,
            "occurBalance": occurBalance,
            "bankId": bankId,
            "paymentDocument": paymentDocument,
            "bankAccountDocument": bankAccountDocument,
            "fundAccount": fundAccount
        }
        headers2 = list(AccountAuth())[1]
        sign1 = {"sign": get_sign(boby)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(boby)
        payload1.update(sign1)

        payload3 = json.dumps(dict(payload1))
        r = Requests(self.session).post(
            url=url_fund_deposit, headers=headers2, data=payload3, title="资金存取"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == 'ok'
            assert j.get("code") == "000000"
        except:
            raise AssertionError(j)
