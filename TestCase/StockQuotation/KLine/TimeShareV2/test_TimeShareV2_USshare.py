import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestKlinev2USshareTime:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('分时查询_优化版本 Version 2.0_US个股')
    def test_Kline_v2USshare_time(self):
        response = zhuorui('k线', '分时查询_优化版本 Version 2.0_US个股')
        assert_data(response, '000000', 'ok')