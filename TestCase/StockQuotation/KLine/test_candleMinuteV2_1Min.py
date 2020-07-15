import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestCandleMinute1Min:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('蜡烛图1分钟查询_优化版本 Version 2.0_HK个股')
    def test_candleMinute_1min_HKshare(self):
        response = zhuorui('k线', '蜡烛图1分钟查询_优化版本 Version 2.0_HK个股')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('蜡烛图1分钟查询_优化版本 Version 2.0_US个股')
    def test_candleMinute_1min_USshare(self):
        response = zhuorui('k线', '蜡烛图1分钟查询_优化版本 Version 2.0_US个股')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('蜡烛图1分钟查询_优化版本 Version 2.0_SH个股')
    def test_candleMinute_1min_SHshare(self):
        response = zhuorui('k线', '蜡烛图1分钟查询_优化版本 Version 2.0_SH个股')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('蜡烛图1分钟查询_优化版本 Version 2.0_SZ个股')
    def test_candleMinute_1min_SZshare(self):
        response = zhuorui('k线', '蜡烛图1分钟查询_优化版本 Version 2.0_SZ个股')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())