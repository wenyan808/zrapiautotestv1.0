import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


class TestOptionalStockList:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('自选股股票列表_SZ')
    def test_optional_stock_list_sz(self):
        response = zhuorui('自选股', '自选股股票列表_SZ')
        assert_data(response, '000000', 'ok')

    @allure.story('自选股股票列表_SH')
    def test_optional_stock_list_sh(self):
        response = zhuorui('自选股', '自选股股票列表_SH')
        assert_data(response, '000000', 'ok')

    @allure.story('自选股股票列表_HK')
    def test_optional_stock_list_hk(self):
        response = zhuorui('自选股', '自选股股票列表_HK')
        assert_data(response, '000000', 'ok')

    @allure.story('自选股股票列表_SZ&SH')
    def test_optional_stock_list_szsh(self):
        response = zhuorui('自选股', '自选股股票列表_SZ&SH')
        assert_data(response, '000000', 'ok')

    @allure.story('自选股股票列表_SZ&HK')
    def test_optional_stock_list_szhk(self):
        response = zhuorui('自选股', '自选股股票列表_SZ&HK')
        assert_data(response, '000000', 'ok')

    @allure.story('自选股股票列表_SH&HK')
    def test_optional_stock_list_shhk(self):
        response = zhuorui('自选股', '自选股股票列表_SH&HK')
        assert_data(response, '000000', 'ok')

    @allure.story('自选股股票列表_SH&HK&SZ')
    def test_optional_stock_list_shhksz(self):
        response = zhuorui('自选股', '自选股股票列表_SH&HK&SZ')
        assert_data(response, '000000', 'ok')

    @allure.story('自选股股票列表_All')
    def test_optional_stock_list_all(self):
        response = zhuorui('自选股', '自选股股票列表_All')
        assert_data(response, '000000', 'ok')

    # @allure.story('自选股股票列表_ts不正确')
    # def test_optional_stock_list_notts(self):
    #     response = zhuorui('自选股', '自选股股票列表_ts不正确')
    #     assert_data(response, '000103', '参数校验不通过')
    #
    # @allure.story('自选股股票列表_ts异常')
    # def test_optional_stock_list_excets(self):
    #     response = zhuorui('自选股', '自选股股票列表_ts异常')
    #     assert_data(response, '000103', '参数校验不通过')

    @allure.story('自选股股票列表_参数为空')
    def test_optional_stock_list_null(self):
        response = zhuorui('自选股', '自选股股票列表_参数为空')
        assert_data(response, '000000', 'ok')

    @allure.story('自选股股票列表无token_All')
    def test_optional_stock_list_all_notoken(self):
        response = zhuorui('自选股', '自选股股票列表无token_All')
        # print(response.json())
        assert_data(response, '000101', 'token不能为空')


if __name__ == '__main__':
    pytest.main()
