import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('股票资金')
class TestAktienfond:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询股票的最新资金数据_US')
    def test_getnewAktienfond_US(self):
        response = zhuorui('股票资金', '查询股票的最新资金数据_US')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询股票的最新资金数据_SH')
    def test_getnewAktienfond_SH(self):
        response = zhuorui('股票资金', '查询股票的最新资金数据_SH')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询股票的最新资金数据_SZ')
    def test_getnewAktienfond_SZ(self):
        response = zhuorui('股票资金', '查询股票的最新资金数据_SZ')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询股票的最新资金数据_HK')
    def test_getnewAktienfond_HK(self):
        response = zhuorui('股票资金', '查询股票的最新资金数据_HK')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询股票的历史资金数据_US')
    def test_gethistoryAktienfond_US(self):
        response = zhuorui('股票资金', '查询股票的历史资金数据_US')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询股票的历史资金数据_SZ')
    def test_gethistoryAktienfond_SZ(self):
        response = zhuorui('股票资金', '查询股票的历史资金数据_US')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询股票的历史资金数据_SH')
    def test_gethistoryAktienfond_SH(self):
        response = zhuorui('股票资金', '查询股票的历史资金数据_SH')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询股票的历史资金数据_HK')
    def test_gethistoryAktienfond_HK(self):
        response = zhuorui('股票资金', '查询股票的历史资金数据_HK')
        assert_data(response, '000000', 'ok')
        # print(response.text)
