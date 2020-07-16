import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

@pytest.mark.skip(reason="该测试用例版本过低，pass")
@allure.feature('k线')
class TestYearKlineSZshare:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('年K查询_SZ个股')
    def test_YearKline_SZshare(self):
        response = zhuorui('k线', '年K查询_SZ个股')
        assert_data(response, '000000', 'ok')
        # print(response.text)