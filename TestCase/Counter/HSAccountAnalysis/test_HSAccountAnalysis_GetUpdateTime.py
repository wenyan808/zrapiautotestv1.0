# test_HSAccountAnalysis_GetUpdateTime    账户分析、新股盈亏-数据更新完时间点获取    /as_trade/api/analysis_tm/v1/get_update_time
"""
@File  ：test_HSAccountAnalysis_GetUpdateTime.py
@Author: yishouquan
@Time  : 2020/7/28
@Desc  :  柜台app_账户分析、新股盈亏-数据更新完时间点获取
"""
import json

import allure
import pytest
from Common.sign import get_sign
from Common.requests_library import Requests
from Common.Accountcommon.accountAuth import AccountAuth


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_账户分析、新股盈亏-数据更新完时间点获取')
class TestHSAccountAnalysisGetUpdateTime():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSAccountAnalysis_GetUpdateTime(self):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/analysis_tm/v1/get_update_time"
        # 拼装参数
        headers = list(AccountAuth())[1]

        paylo = {}

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload2 = json.dumps(dict(payload1))

        r_info = Requests(self.session).post(
            url=url, headers=headers, data=payload2, title="账户分析、新股盈亏-数据更新完时间点获取"
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
