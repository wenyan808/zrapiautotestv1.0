import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

@allure.feature("查看股票盘口数据")
class TestHandicap:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询股票盘口数据_All')
    def test_handicap_all(self):
        response = zhuorui('个股详情公共接口', '查询股票盘口数据_All')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票盘口数据_type3ETF')
    def test_handicap_type3ETF(self):
        response = zhuorui('个股详情公共接口', '查询股票盘口数据_type3ETF')
        assert_data(response, '000000', 'ok')

    # @allure.story('查询股票盘口数据_type不正确')
    # def test_handicap_type_error(self):
    #     response = zhuorui('个股详情公共接口', '查询股票盘口数据_type不正确')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询股票盘口数据_type异常')
    # def test_handicap_type_exception(self):
    #     response = zhuorui('个股详情公共接口', '查询股票盘口数据_type异常')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询股票盘口数据_type为空')
    # def test_handicap_type_null(self):
    #     response = zhuorui('个股详情公共接口', '查询股票盘口数据_type为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询股票盘口数据_ts不正确')
    # def test_handicap_ts_error(self):
    #     response = zhuorui('个股详情公共接口', '查询股票盘口数据_ts不正确')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询股票盘口数据_ts异常')
    # def test_handicap_ts_exception(self):
    #     response = zhuorui('个股详情公共接口', '查询股票盘口数据_ts异常')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询股票盘口数据_ts为空')
    # def test_handicap_ts_null(self):
    #     response = zhuorui('个股详情公共接口', '查询股票盘口数据_ts为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询股票盘口数据_ts异常2')
    # def test_handicap_ts_exception2(self):
    #     response = zhuorui('个股详情公共接口', '查询股票盘口数据_ts异常2')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询股票盘口数据_code不正确')
    # def test_handicap_code_error(self):
    #     response = zhuorui('个股详情公共接口', '查询股票盘口数据_code不正确')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询股票盘口数据_code异常')
    # def test_handicap_code_exception(self):
    #     response = zhuorui('个股详情公共接口', '查询股票盘口数据_code异常')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询股票盘口数据_code为空')
    # def test_handicap_code_null(self):
    #     response = zhuorui('个股详情公共接口', '查询股票盘口数据_code为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询股票盘口数据_参数列表为空')
    # def test_handicap_parameter_list_null(self):
    #     response = zhuorui('个股详情公共接口', '查询股票盘口数据_参数列表为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询股票盘口数据_参数为空')
    # def test_handicap_parameter_null(self):
    #     response = zhuorui('个股详情公共接口', '查询股票盘口数据_参数为空')
    #     assert_data(response, '000000', 'ok')


if __name__ == '__main__':
    pytest.main()
