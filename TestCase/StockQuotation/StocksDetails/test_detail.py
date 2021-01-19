import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

@allure.feature("查看逐笔成交")
class TestDetail:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询逐笔成交_US大盘')
    def test_detail_US(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交_US大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交_US个股')
    def test_detail_us(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交_US个股')
        assert_data(response, '000000', 'ok')

    # @allure.story('查询逐笔成交_SZ大盘')
    # def test_detail_SZ(self):
    #     response = zhuorui('个股详情公共接口', '查询逐笔成交_SZ大盘')
    #     # print(response.json())
    #     assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交_SH个股')
    def test_detail_sh(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交_SH个股')
        assert_data(response, '000000', 'ok')

    # @allure.story('查询逐笔成交_HK大盘')
    # def test_detail_HK(self):
    #     response = zhuorui('个股详情公共接口', '查询逐笔成交_HK大盘')
    #     assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交_HK个股')
    def test_detail_hk(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交_HK个股')
        assert_data(response, '000000', 'ok')


if __name__ == '__main__':
    pytest.main()







