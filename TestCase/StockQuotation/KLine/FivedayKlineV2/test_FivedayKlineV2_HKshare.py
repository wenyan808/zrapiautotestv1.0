import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestFivedayKlinev2HKtape:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('五日查询_优化版本 Version 2.0_HK大盘')
    def test_fivedayKlinev2_HKtape(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_HK大盘')
        assert_data(response, '000000', 'ok')
        # print(response)