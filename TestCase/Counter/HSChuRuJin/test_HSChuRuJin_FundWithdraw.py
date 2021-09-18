# test_HSChuRuJin_FundWithdraw             提取资金        /as_trade/api/fund/v1/withdraw
import json

import allure
import pytest

from Business.global_ossurl import oss_appurl
from Common.Accountcommon.accountAuth import AccountAuth
from Common.HSchurujincommon.add_save_bank import add_save_bank
from Common.HSchurujincommon.get_Fund_Account import get_fund_account
from Common.HSchurujincommon.get_Fund_Withdraw import get_fund_withdraw
from Common.OSS import oss_img

from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_json import get_json

from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_提取资金')
class TestHSChuRuJinFundWithdraw():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/HSChurujindata/test_HSChuRuJinFundWithdraw.json"))
    def test_HSChuRuJinFundWithdraw(self, info):
        login_list = list(AccountAuth())
        http = login_list[-1]
        headers = login_list[1]

        url = http + "/as_trade/api/fund/v1/withdraw"
        url2 = http + oss_appurl
        userId = login_list[0].get("data").get("userId")
        withdrawType = info.get("withdrawType")  # 出金方式 1-普通出金 2-银证转账
        occurBalance = info.get("occurBalance")  # 提款金额
        moneyType = info.get("moneyType")  # 货币类型 HKD/USD/CNY

        if len(get_fund_withdraw(http, headers).get("data")) != 0:
            clientBankId = get_fund_withdraw(http, headers).get("data")[0].get("id")  # 用户绑定银行账户id
        else:
            img_name3 = "zhanghupingzheng.jpg"
            img_name4 = "zhanghupingzheng2.JPG"
            catalog = "/Business/UserFileUp/"
            b1_imgurl = list(oss_img("open", img_name3, userId, catalog, url2, headers))[-1]
            b2_imgurl = list(oss_img("open", img_name4, userId, catalog, url2, headers))[-1]
            bankAccountDocument = f"{b1_imgurl}|{b2_imgurl}"  # 上传银行账户凭证url 多张图片以|分隔
            bindBankId = get_fund_withdraw(http, headers).get("data")[0].get("bindBankId")
            # 新增银行卡
            add_save_bank(http, headers, bankAccountDocument, bindBankId, 0, 0)
            # 获取用户绑定银行id
            clientBankId = get_fund_withdraw(http, headers).get("data")[0].get("id")
        # print(clientBankId)
        fundAccount = get_fund_account(http, headers).get("data")[0].get("fundAccount")  # 资金账号
        paylo = {
            "clientBankId": clientBankId,
            "fundAccount": fundAccount
        }
        paylo1 = {
            "withdrawType": withdrawType,
            "occurBalance": occurBalance,
            "moneyType": moneyType
        }
        paylo.update(paylo1)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload2, title="提取资金"
        )

        j = r.json()

        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("msg") == 'ok'
            assert j.get("code") == "000000"
        except:
            raise AssertionError(j)
