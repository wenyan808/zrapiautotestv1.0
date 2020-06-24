import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestNewdayKlineSHtape:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('最新日K_SH大盘')
    def test_newdayKline_SHtape(self):
        response = zhuorui('k线', '最新日K_SH大盘')
        assert_data(response, '000000', 'ok')