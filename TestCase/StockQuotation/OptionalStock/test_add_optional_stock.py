import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


class TestAddOptionalStock:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('添加自选股_US大盘')
    def test_add_US(self):
        response = zhuorui('自选股', '添加自选股_US大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('添加自选股_US个股')
    def test_add_us(self):
        response = zhuorui('自选股', '添加自选股_US个股')
        assert_data(response, '000000', 'ok')

    @allure.story('添加自选股_SH大盘')
    def test_add_SH(self):
        response = zhuorui('自选股', '添加自选股_SH大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('添加自选股_SH个股')
    def test_add_sh(self):
        response = zhuorui('自选股', '添加自选股_SH个股')
        assert_data(response, '000000', 'ok')

    @allure.story('添加自选股_SZ大盘')
    def test_add_SZ(self):
        response = zhuorui('自选股', '添加自选股_SZ大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('添加自选股_SZ个股')
    def test_add_sz(self):
        response = zhuorui('自选股', '添加自选股_SZ个股')
        assert_data(response, '000000', 'ok')

    @allure.story('添加自选股_HK大盘')
    def test_add_HK(self):
        response = zhuorui('自选股', '添加自选股_HK大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('添加自选股_HK个股')
    def test_add_hk(self):
        response = zhuorui('自选股', '添加自选股_HK个股')
        assert_data(response, '000000', 'ok')

    # @allure.story('添加自选股_type不正确')
    # def test_add_stock_type_error(self):
    #     response = zhuorui('自选股', '添加自选股_type不正确')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('添加自选股_type异常')
    # def test_add_stock_type_exception(self):
    #     response = zhuorui('自选股', '添加自选股_type异常')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('添加自选股_type为空')
    # def test_add_stock_type_null(self):
    #     response = zhuorui('自选股', '添加自选股_type为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('添加自选股_ts不正确')
    #     # def test_add_stock_ts_error(self):
    #     #     response = zhuorui('自选股', '添加自选股_ts不正确')
    #     #     assert_data(response, '000000', 'ok')

    # @allure.story('添加自选股_ts异常')
    # def test_add_stock_ts_exception(self):
    #     response = zhuorui('自选股', '添加自选股_ts异常')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('添加自选股_ts为空')
    # def test_add_stock_ts_null(self):
    #     response = zhuorui('自选股', '添加自选股_ts为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('添加自选股_code不正确')
    # def test_add_stock_code_error(self):
    #     response = zhuorui('自选股', '添加自选股_code不正确')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('添加自选股_code异常')
    # def test_add_stock_code_exception(self):
    #     response = zhuorui('自选股', '添加自选股_code异常')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('添加自选股_code为空')
    # def test_add_stock_code_null(self):
    #     response = zhuorui('自选股', '添加自选股_code为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('添加自选股_达到上限')
    # def test_add_stock_upper_limit(self):
    #     response = zhuorui('自选股', '添加自选股_达到上限')
    #     assert_data(response, '000000', 'ok')
    #
    # @allure.story('添加自选股_参数为空')
    # def test_add_stock_parameter_null(self):
    #     response = zhuorui('自选股', '添加自选股_参数为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('添加自选股无token_US大盘')
    # def test_add_US_notoken(self):
    #     response = zhuorui('自选股', '添加自选股无token_US大盘')
    #     print(response.json())
    #     # assert_data(response, '000101', 'token不能为空')
    #
    # @allure.story('添加自选股无token_US个股')
    # def test_add_us_notoken(self):
    #     response = zhuorui('自选股', '添加自选股无token_US个股')
    #     print(response.json())
    #     # assert_data(response, '000101', 'token不能为空')
    #
    # @allure.story('添加自选股无token_SH大盘')
    # def test_add_SH_notoken(self):
    #     response = zhuorui('自选股', '添加自选股无token_SH大盘')
    #     print(response.json())
    #     # assert_data(response, '000101', 'token不能为空')
    #
    # @allure.story('添加自选股无token_SH个股')
    # def test_add_sh_notoken(self):
    #     response = zhuorui('自选股', '添加自选股无token_SH个股')
    #     print(response.json())
    #     # assert_data(response, '000101', 'token不能为空')
    #
    # @allure.story('添加自选股无token_SZ大盘')
    # def test_add_SZ_notoken(self):
    #     response = zhuorui('自选股', '添加自选股无token_SZ大盘')
    #     print(response.json())
    #     # assert_data(response, '000101', 'token不能为空')
    #
    # @allure.story('添加自选股无token_SZ个股')
    # def test_add_sz_notoken(self):
    #     response = zhuorui('自选股', '添加自选股无token_SZ个股')
    #     print(response.json())
    #     # assert_data(response, '000101', 'token不能为空')
    #
    # @allure.story('添加自选股无token_HK大盘')
    # def test_add_HK_notoken(self):
    #     response = zhuorui('自选股', '添加自选股无token_HK大盘')
    #     print(response.json())
    #     # assert_data(response, '000101', 'token不能为空')
    #
    # @allure.story('添加自选股无token_HK个股')
    # def test_add_hk_notoken(self):
    #     response = zhuorui('自选股', '添加自选股无token_HK个股')
    #     print(response.json())
    #     # assert_data(response, '000101', 'token不能为空')

#
# if __name__ == '__main__':
#     pytest.main()



