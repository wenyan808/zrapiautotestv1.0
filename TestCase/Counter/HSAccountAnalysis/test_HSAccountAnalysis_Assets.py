# test_HSAccountAnalysis_Assets     资产走势          /as_trade/api/analysis/v1/assets
"""
@File  ：test_HSAccountAnalysis_Assets.py
@Author: yishouquan
@Time  : 2020/7/28
@Desc  :  柜台app_资产走势
"""
import json

import allure
import pytest

from Common.Accountcommon.accountAuth import AccountAuth

from Common.get_time_stamp import timetostamp13
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json

from glo import BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_资产走势')
class TestHSAccountAnalysisAssets():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR + r"/TestData/HSAccountAnalysis/test_HSAccountAnalysis_Assets.json"))
    def test_HSAccountAnalysis_Assets(self, info):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/analysis/v1/assets"
        # 拼装参数
        headers = list(AccountAuth())[1]
        if info.get("startDate") == None and info.get("endDate") == None:
            market = info.get("market")  # 市场类型，（1-港 2-美 3-A，不传查询综合账户分析）
            moneyType = info.get(
                "moneyType")  # moneyType货币类型(当market为空时为查询综合账户则须指定货币)   币种类别:HKD(港股市场) USD(美股市场) CNY(A股市场)
            paylo = {
                "market": market,
                "moneyType": moneyType
            }
            sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
            payload1 = {}
            payload1.update(paylo)
            payload1.update(sign1)

            payload2 = json.dumps(dict(payload1))
        elif info.get("endDate") == None:
            startDate = timetostamp13(
                info.get("startDate"))  # (查询年初至今，仅传startDate即可；查询开户至今startDate和endDate都不需要传）传日期时间戳格式
            market = info.get("market")  # 市场类型，（1-港 2-美 3-A，不传查询综合账户分析）
            moneyType = info.get(
                "moneyType")  # moneyType货币类型(当market为空时为查询综合账户则须指定货币)   币种类别:HKD(港股市场) USD(美股市场) CNY(A股市场)
            paylo = {
                "startDate": startDate,
                # "endDate": endDate,
                "market": market,
                "moneyType": moneyType
            }

            sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
            payload1 = {}
            payload1.update(paylo)
            payload1.update(sign1)

            payload2 = json.dumps(dict(payload1))
        else:
            startDate = timetostamp13(
                info.get("startDate"))  # (查询年初至今，仅传startDate即可；查询开户至今startDate和endDate都不需要传）传日期时间戳格式
            endDate = timetostamp13(info.get("endDate"))  # endDate结束日期（传日期时间戳格式 13位），不传查至今
            market = info.get("market")  # 市场类型，（1-港 2-美 3-A，不传查询综合账户分析）
            moneyType = info.get(
                "moneyType")  # moneyType货币类型(当market为空时为查询综合账户则须指定货币)   币种类别:HKD(港股市场) USD(美股市场) CNY(A股市场)
            paylo = {
                "startDate": startDate,
                "endDate": endDate,
                "market": market,
                "moneyType": moneyType
            }

            sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
            payload1 = {}
            payload1.update(paylo)
            payload1.update(sign1)

            payload2 = json.dumps(dict(payload1))

        r_info = Requests(self.session).post(
            url=url, headers=headers, data=payload2, title="资产走势"
        )

        j = r_info.json()
        # print(j)
        assert r_info.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == 'ok'
        except:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload2}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}"
            )
