import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('查询资金统计')
class TestCandleMinute:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('按时间查询资金统计数据_USetf10天')
    def test_getCapitalFlowTime_US_Tendays(self):
        response = zhuorui('查询资金统计', '按时间查询资金统计数据_USetf10天')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('按时间查询资金统计数据_SH10天')
    def test_getCapitalFlowTime_SH_Tendays(self):
        response = zhuorui('查询资金统计', '按时间查询资金统计数据_SH10天')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('按时间查询资金统计数据_SZ10天')
    def test_getCapitalFlowTime_SZ_Tendays(self):
        response = zhuorui('查询资金统计', '按时间查询资金统计数据_SZ10天')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('按时间查询资金统计数据_US10天')
    def test_getCapitalFlowTime_US_Tendays(self):
        response = zhuorui('查询资金统计', '按时间查询资金统计数据_US10天')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('按时间查询资金统计数据_HK10天')
    def test_getCapitalFlowTime_HK_Tendays(self):
        response = zhuorui('查询资金统计', '按时间查询资金统计数据_HK10天')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('按时间查询资金统计数据_USetf10天')
    def test_getCapitalFlowTime_US_Tendays(self):
        response = zhuorui('查询资金统计', '按时间查询资金统计数据_USetf10天')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('按时间查询资金统计数据_USetf10天')
    def test_getCapitalFlowTime_US_Tendays(self):
        response = zhuorui('查询资金统计', '按时间查询资金统计数据_USetf10天')
        assert_data(response, '000000', 'ok')
        # print(response.text)



