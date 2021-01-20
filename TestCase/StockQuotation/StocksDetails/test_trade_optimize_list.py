import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

# @allure.feature("查询逐笔成交统计(优化)")
@pytest.mark.skip(reason="调试中 ")
class TestDetail:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询逐笔成交统计(优化)_US大盘')
    def test_te(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_US大盘')
        print(response.json())
        # assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_US个股')
    def test_detail_us(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_US个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_SZ大盘')
    def test_detail_US(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_SZ大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_SZ个股')
    def test_detail_us(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_SZ个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_SH大盘')
    def test_detail_US(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_SH大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_SH个股')
    def test_detail_us(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_SH个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_HK大盘')
    def test_detail_US(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_HK大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_HK个股')
    def test_detail_us(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_HK个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_ts不正确')
    def test_detail_US(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_ts不正确')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_ts异常')
    def test_detail_us(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_ts异常')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_ts为空')
    def test_detail_US(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_ts为空')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_code不正确')
    def test_detail_us(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_code不正确')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_code异常')
    def test_detail_US(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_code异常')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_code为空')
    def test_detail_us(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_code为空')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_参数为空')
    def test_detail_us(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_参数为空')
        assert_data(response, '000000', 'ok')