import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

@pytest.mark.skip(reason="该测试用例版本过低，pass")
@allure.feature('k线')
class TestYearKlineUSshare:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('年K查询_US个股')
    def test_YearKline_USshare(self):
        response = zhuorui('k线', '年K查询_US个股')
        assert_data(response, '000000', 'ok')
        # print(response.json())