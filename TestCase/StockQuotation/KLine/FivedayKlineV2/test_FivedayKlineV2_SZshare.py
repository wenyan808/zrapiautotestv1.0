import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestKlinev2SZshareFiveday:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('五日查询_优化版本 Version 2.0_SZ个股')
    def test_Kline_v2SZshare_fiveday(self):
        response = zhuorui('k线', '五日查询_优化版本 Version 2.0_SZ个股')
        assert_data(response, '000000', 'ok')