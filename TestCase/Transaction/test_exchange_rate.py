import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


class TestExchangeRate:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('获取两个货币的汇率比率_USD&HKD')
    def test_exchange_rate_USD_and_HKD(self):
        response = zhuorui('个股详情公共接口', '获取两个货币的汇率比率_USD&HKD')
        assert_data(response, '000000', 'ok')

    @allure.story('获取两个货币的汇率比率_USD&CNY')
    def test_exchange_rate_USD_and_CNY(self):
        response = zhuorui('个股详情公共接口', '获取两个货币的汇率比率_USD&CNY')
        assert_data(response, '000000', 'ok')

    @allure.story('获取两个货币的汇率比率_HKD&CNY')
    def test_exchange_rate_HKD_and_CNY(self):
        response = zhuorui('个股详情公共接口', '获取两个货币的汇率比率_HKD&CNY')
        assert_data(response, '000000', 'ok')

    @allure.story('获取两个货币的汇率比率_currencyA')
    def test_exchange_rate_currencyA(self):
        response = zhuorui('个股详情公共接口', '获取两个货币的汇率比率_currencyA')
        assert_data(response, '000000', 'ok')

    @allure.story('获取两个货币的汇率比率_currencyB')
    def test_exchange_rate_currencyB(self):
        response = zhuorui('个股详情公共接口', '获取两个货币的汇率比率_currencyB')
        assert_data(response, '000000', 'ok')

    @allure.story('获取两个货币的汇率比率')
    def test_exchange_rate(self):
        response = zhuorui('个股详情公共接口', '获取两个货币的汇率比率')
        assert_data(response, '000000', 'ok')


if __name__ == '__main__':
    pytest.main()