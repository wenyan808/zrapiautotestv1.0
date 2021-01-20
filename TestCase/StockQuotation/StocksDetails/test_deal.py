import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

@allure.feature("查询委托挂单（买卖档）")
class TestDeal:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询委托挂单（买卖档）_US大盘')
    def test_deal_US(self):
        response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_US大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询委托挂单（买卖档）_US个股')
    def test_deal_us(self):
        response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_US个股')
        assert_data(response, '000000', 'ok')

    # @allure.story('查询委托挂单（买卖档）_SZ大盘')
    # def test_deal_SZ(self):
    #     response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_SZ大盘')
    #     assert_data(response, '000000', 'ok')

    @allure.story('查询委托挂单（买卖档）_SZ个股')
    def test_deal_sz(self):
        response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_SZ个股')
        assert_data(response, '000000', 'ok')

    # @allure.story('查询委托挂单（买卖档）_SH大盘')
    # def test_deal_SH(self):
    #     response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_SH大盘')
    #     assert_data(response, '000000', 'ok')

    @allure.story('查询委托挂单（买卖档）_SH个股')
    def test_deal_sh(self):
        response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_SH个股')
        assert_data(response, '000000', 'ok')

    # @allure.story('查询委托挂单（买卖档）_HK大盘')
    # def test_deal_HK(self):
    #     response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_HK大盘')
    #     assert_data(response, '000000', 'ok')

    @allure.story('查询委托挂单（买卖档）_HK个股')
    def test_deal_hk(self):
        response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_HK个股')
        assert_data(response, '000000', 'ok')

    # @allure.story('查询委托挂单（买卖档）_ts不正确')
    # def test_deal_ts_error(self):
    #     response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_ts不正确')
    #     assert_data(response, '000000', 'ok')
    #
    # @allure.story('查询委托挂单（买卖档）_ts异常')
    # def test_deal_ts_exception(self):
    #     response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_ts异常')
    #     assert_data(response, '000000', 'ok')
    #
    # @allure.story('查询委托挂单（买卖档）_ts为空')
    # def test_deal_ts_null(self):
    #     response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_ts为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询委托挂单（买卖档）_code不正确')
    # def test_deal_code_error(self):
    #     response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_code不正确')
    #     assert_data(response, '000000', 'ok')
    #
    # @allure.story('查询委托挂单（买卖档）_code异常')
    # def test_deal_code_exception(self):
    #     response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_code异常')
    #     assert_data(response, '000000', 'ok')
    #
    # @allure.story('查询委托挂单（买卖档）_code为空')
    # def test_deal_code_null(self):
    #     response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_code为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询委托挂单（买卖档）_参数为空')
    # def test_deal_parameter_null(self):
    #     response = zhuorui('个股详情公共接口', '查询委托挂单（买卖档）_参数为空')
    #     assert_data(response, '000000', 'ok')


if __name__ == '__main__':
    pytest.main()






