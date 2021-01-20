import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

@allure.feature("查看逐笔成交统计")
class TestStatistics:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询逐笔成交统计_US大盘')
    def test_statistics_US(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计_US大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计_US个股')
    def test_statistics_us(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计_US个股')
        assert_data(response, '000000', 'ok')

    # @allure.story('查询逐笔成交统计_SZ大盘')
    # def test_statistics_SZ(self):
    #     response = zhuorui('个股详情公共接口', '查询逐笔成交统计_SZ大盘')
    #     assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计_SZ个股')
    def test_statistics_sz(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计_SZ个股')
        assert_data(response, '000000', 'ok')

    # @allure.story('查询逐笔成交统计_SH大盘')
    # def test_statistics_SH(self):
    #     response = zhuorui('个股详情公共接口', '查询逐笔成交统计_SH大盘')
    #     assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计_SH个股')
    def test_statistics_sh(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计_SH个股')
        assert_data(response, '000000', 'ok')

    # @allure.story('查询逐笔成交统计_HK大盘')
    # def test_statistics_HK(self):
    #     response = zhuorui('个股详情公共接口', '查询逐笔成交统计_HK大盘')
    #     assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计_HK个股')
    def test_statistics_hk(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计_HK个股')
        assert_data(response, '000000', 'ok')

    # @allure.story('查询逐笔成交统计_ts不正确')
    # def test_statistics_ts_error(self):
    #     response = zhuorui('个股详情公共接口', '查询逐笔成交统计_ts不正确')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询逐笔成交统计_ts异常')
    # def test_statistics_ts_exception(self):
    #     response = zhuorui('个股详情公共接口', '查询逐笔成交统计_ts异常')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询逐笔成交统计_ts为空')
    # def test_statistics_ts_null(self):
    #     response = zhuorui('个股详情公共接口', '查询逐笔成交统计_ts为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询逐笔成交统计_code不正确')
    # def test_statistics_code_error(self):
    #     response = zhuorui('个股详情公共接口', '查询逐笔成交统计_code不正确')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询逐笔成交统计_code异常')
    # def test_statistics_code_exception(self):
    #     response = zhuorui('个股详情公共接口', '查询逐笔成交统计_code异常')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询逐笔成交统计_code为空')
    # def test_statistics_code_null(self):
    #     response = zhuorui('个股详情公共接口', '查询逐笔成交统计_code为空')
    #     assert_data(response, '000000', 'ok')

    # @allure.story('查询逐笔成交统计_参数为空')
    # def test_statistics_parameter_null(self):
    #     response = zhuorui('个股详情公共接口', '查询逐笔成交统计_参数为空')
    #     assert_data(response, '000000', 'ok')


if __name__ == '__main__':
    pytest.main()
