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
        response = zhuorui('交易', '获取两个货币的汇率比率_USD&HKD')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('获取两个货币的汇率比率_USD&CNY')
    def test_exchange_rate_USD_and_CNY(self):
        response = zhuorui('交易', '获取两个货币的汇率比率_USD&CNY')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            # assert response.json().get("data")
            # print(response.json().get("data").get("rate"))
            if len(response.json().get("data")) != 0:
                assert "rate" in response.json().get("data")



    @allure.story('获取两个货币的汇率比率_HKD&CNY')
    def test_exchange_rate_HKD_and_CNY(self):
        response = zhuorui('交易', '获取两个货币的汇率比率_HKD&CNY')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            # assert response.json().get("data")
            # print(response.json().get("data").get("rate"))
            if len(response.json().get("data")) != 0:
                assert "rate" in response.json().get("data")

    @allure.story('获取两个货币的汇率比率_currencyA')
    def test_exchange_rate_currencyA(self):
        response = zhuorui('交易', '获取两个货币的汇率比率_currencyA')
        assert response.status_code == 200
        # assert_data(response, '000103', 'currencyB is null')
        assert_data(response, '000103', 'currencyB is error')
        # print(response.json())


    @allure.story('获取两个货币的汇率比率_currencyB')
    def test_exchange_rate_currencyB(self):
        response = zhuorui('交易', '获取两个货币的汇率比率_currencyB')
        assert response.status_code == 200
        assert_data(response, '000103', 'currencyA is error')
        # print(response.json())

    @allure.story('获取两个货币的汇率比率')
    def test_exchange_rate(self):
        response = zhuorui('交易', '获取两个货币的汇率比率')
        assert response.status_code == 200
        # assert_data(response, '000103', 'currencyB is null')
        # assert_data(response, '000103', 'currencyA is error')
        assert_data(response, '000103', 'currencyB is error')
        # print(response.json())


if __name__ == '__main__':
    pytest.main()
