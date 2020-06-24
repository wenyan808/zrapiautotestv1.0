import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestMonthKlineUSshare:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('月K查询_US个股')
    def test_MonthKline_USshare(self):
        response = zhuorui('k线', '月K查询_US个股')
        assert_data(response, '000000', 'ok')
        # print(response.text)