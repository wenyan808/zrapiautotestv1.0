import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestCandleMinute1Min:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('蜡烛图1分钟查询_优化版本 Version 2.0_HK')
    def test_candleMinute_1min_HK(self):
        response = zhuorui('k线', '蜡烛图1分钟查询_优化版本 Version 2.0_HK')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('蜡烛图1分钟查询_优化版本 Version 2.0_US')
    def test_candleMinute_1min_US(self):
        response = zhuorui('k线', '蜡烛图1分钟查询_优化版本 Version 2.0_US')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('蜡烛图1分钟查询_优化版本 Version 2.0_SH')
    def test_candleMinute_1min_SH(self):
        response = zhuorui('k线', '蜡烛图1分钟查询_优化版本 Version 2.0_SH')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('蜡烛图1分钟查询_优化版本 Version 2.0_SZ')
    def test_candleMinute_1min_SZ(self):
        response = zhuorui('k线', '蜡烛图1分钟查询_优化版本 Version 2.0_SZ')
        assert_data(response, '000000', 'ok')
        # print(response.text)