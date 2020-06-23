import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


class TestSynOptionalStock:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('同步自选股_All')
    def test_syn_all(self):
        response = zhuorui('自选股', '同步自选股_All')
        assert_data(response, '000000', 'ok')

    @allure.story('同步自选股_type3ETF')
    def test_syn_type3ETF(self):
        response = zhuorui('自选股', '同步自选股_type3ETF')
        assert_data(response, '000000', 'ok')

    # @allure.story('同步自选股_type不正确')
    # def test_syn_type_error(self):
    #     response = zhuorui('自选股', '同步自选股_type不正确')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('同步自选股_type异常')
    # def test_syn_type_exception(self):
    #     response = zhuorui('自选股', '同步自选股_type异常')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('同步自选股_type为空')
    # def test_syn_type_null(self):
    #     response = zhuorui('自选股', '同步自选股_type为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('同步自选股_ts不正确')
    # def test_syn_ts_error(self):
    #     response = zhuorui('自选股', '同步自选股_ts不正确')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('同步自选股_ts异常')
    # def test_syn_ts_exception(self):
    #     response = zhuorui('自选股', '同步自选股_ts异常')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('同步自选股_ts为空')
    # def test_syn_ts_null(self):
    #     response = zhuorui('自选股', '同步自选股_ts为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('同步自选股_ts异常2')
    # def test_syn_ts_exception2(self):
    #     response = zhuorui('自选股', '同步自选股_ts异常2')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('同步自选股_code不正确')
    # def test_syn_code_error(self):
    #     response = zhuorui('自选股', '同步自选股_code不正确')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('同步自选股_code异常')
    # def test_syn_code_exception(self):
    #     response = zhuorui('自选股', '同步自选股_code异常')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('同步自选股_code为空')
    # def test_syn_code_null(self):
    #     response = zhuorui('自选股', '同步自选股_code为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('同步自选股_参数列表为空')
    # def test_syn_parameter_null(self):
    #     response = zhuorui('自选股', '同步自选股_参数列表为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('同步自选股_参数为空')
    # def test_syn_not_parameter(self):
    #     response = zhuorui('自选股', '同步自选股_参数为空')
    #     assert_data(response, '000000', 'ok')






