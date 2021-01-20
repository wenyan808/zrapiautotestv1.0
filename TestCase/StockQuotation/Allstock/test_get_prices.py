import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

@allure.feature('查询股票价格数据')
class TestBroker:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询股票价格数据_港股大盘')
    def test_getpricehktype1(self):
        response = zhuorui('个股详情公共接口', '查询股票价格数据_港股大盘')
        # print(response.json())
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票价格数据_A股大盘')
    def test_getpriceatype1(self):
        response = zhuorui('个股详情公共接口', '查询股票价格数据_A股大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票价格数据_美股大盘')
    def test_getpriceustype1(self):
        response = zhuorui('个股详情公共接口', '查询股票价格数据_美股大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票价格数据_A股SZ个股')
    def test_getpriceasz(self):
        response = zhuorui('个股详情公共接口', '查询股票价格数据_A股SZ个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票价格数据_A股SH个股')
    def test_getpriceash(self):
        response = zhuorui('个股详情公共接口', '查询股票价格数据_A股SH个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票价格数据_港股个股')
    def test_getpricehktype2(self):
        response = zhuorui('个股详情公共接口', '查询股票价格数据_港股个股')
        # print(response.json())
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票价格数据_美股个股')
    def test_getpriceustype2(self):
        response = zhuorui('个股详情公共接口', '查询股票价格数据_美股个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票价格数据_港股ETF')
    def test_getpricehktype3(self):
        response = zhuorui('个股详情公共接口', '查询股票价格数据_港股ETF')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票价格数据_美股ETF')
    def test_getpriceustype3(self):
        response = zhuorui('个股详情公共接口', '查询股票价格数据_美股ETF')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票价格数据_All')
    def test_getpriceall(self):
        response = zhuorui('个股详情公共接口', '查询股票价格数据_All')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票价格数据_参数列表空')
    def test_getpricenull(self):
        response = zhuorui('个股详情公共接口', '查询股票价格数据_参数列表空')
        assert_data(response, '000000', 'ok')
#
# if __name__ == '__main__':
#     pytest.main()
