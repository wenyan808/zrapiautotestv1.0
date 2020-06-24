import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestDayKlineSZshare:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('日K查询_SZ个股')
    def test_dayKline_SZshare(self):
        response = zhuorui('k线', '日K查询_SZ个股')
        assert_data(response, '000000', 'ok')