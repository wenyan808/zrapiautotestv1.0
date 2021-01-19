import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


class TestBroker:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询股票状态_港股大盘')
    def test_stock_stathktype1(self):
        response = zhuorui('个股详情公共接口', '查询股票状态_港股大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票状态_A股大盘')
    def test_stock_statatype1(self):
        response = zhuorui('个股详情公共接口', '查询股票状态_A股大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票状态_美股大盘')
    def test_stock_statusustype1(self):
        response = zhuorui('个股详情公共接口', '查询股票状态_美股大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票状态_A股SZ个股')
    def test_stock_statusasz(self):
        response = zhuorui('个股详情公共接口', '查询股票状态_A股SZ个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票状态_A股SH个股')
    def test_stock_statusash(self):
        response = zhuorui('个股详情公共接口', '查询股票状态_A股SH个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票状态_港股个股')
    def test_stock_statushktype2(self):
        response = zhuorui('个股详情公共接口', '查询股票状态_港股个股')
        # print(response.json())
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票状态_美股个股')
    def test_stock_statusustype2(self):
        response = zhuorui('个股详情公共接口', '查询股票状态_美股个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票状态_港股ETF')
    def test_stock_statushktype3(self):
        response = zhuorui('个股详情公共接口', '查询股票状态_港股ETF')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票状态_美股ETF')
    def test_stock_statusustype3(self):
        response = zhuorui('个股详情公共接口', '查询股票状态_美股ETF')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票状态_参数空列表')
    def test_stock_statusnull(self):
        response = zhuorui('个股详情公共接口', '查询股票状态_参数空列表')
        assert_data(response, '000103', 'size 需要大于0')

    @allure.story('查询股票状态_All')
    def test_stock_statusall(self):
        response = zhuorui('个股详情公共接口', '查询股票状态_All')
        assert_data(response, '000000', 'ok')


# if __name__ == '__main__':
#     pytest.main()



