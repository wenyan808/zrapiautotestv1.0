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

    @allure.story('查询逐笔成交统计(top20)_US大盘')
    def test_tradesta20_US(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_US大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(top20)_US个股')
    def test_tradesta20_USge(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_US个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(top20)_SZ大盘')
    def test_tradesta20_SZ(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_SZ大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(top20)_SZ个股')
    def test_tradesta20_SZge(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_SZ个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(top20)_SH大盘')
    def test_tradesta20_SH(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_SH大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(top20)_SH个股')
    def test_tradesta20_Sge(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_SH个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(top20)_HK大盘')
    def test_tradesta20_HK(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_HK大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(top20)_HK个股')
    def test_tradesta20_HKge(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_HK个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(top20)_ts不正确')
    def test_tradesta20_tsno(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_ts不正确')
        assert_data(response, '000103', 'ts格式有误')

    @allure.story('查询逐笔成交统计(top20)_ts异常')
    def test_tradesta20_tsyc(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_ts异常')
        assert_data(response, '000103', 'ts格式有误')

    @allure.story('查询逐笔成交统计(top20)_ts为空')
    def test_tradesta20_tsnone(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_ts为空')
        assert_data(response, '000103', 'ts格式有误')

    @allure.story('查询逐笔成交统计(top20)_code不正确')
    def test_tradesta20_codeno(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_code不正确')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(top20)_code异常')
    def test_tradesta20_codeyc(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_code异常')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(top20)_code为空')
    def test_tradestayh_codenone(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_code为空')
        assert_data(response, '000103', 'code格式有误')

    @allure.story('查询逐笔成交统计(top20)_参数为空')
    def test_tradestayh_codenone(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(top20)_参数为空')
        assert_data(response, '000103', 'ts格式有误')

    @allure.story('查询逐笔成交统计(优化)_US大盘')
    def test_tradesta20_US(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_US大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_US个股')
    def test_tradestayh_USge(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_US个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_SZ大盘')
    def test_tradestayh_SZ(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_SZ大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_SZ个股')
    def test_tradestayh_SZge(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_SZ个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_SH大盘')
    def test_tradestayh_SH(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_SH大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_SH个股')
    def test_tradestayh_SHge(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_SH个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_HK大盘')
    def test_tradestayh_HK(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_HK大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_HK个股')
    def test_tradestayh_HKge(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_HK个股')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_ts不正确')
    def test_tradesta20_tsno(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_ts不正确')
        assert_data(response, '000103', 'ts格式有误')

    @allure.story('查询逐笔成交统计(优化)_ts异常')
    def test_tradesta20_tsyc(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_ts异常')
        assert_data(response, '000103', 'ts格式有误')

    @allure.story('查询逐笔成交统计(优化)_ts为空')
    def test_tradesta20_tsnone(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_ts为空')
        assert_data(response, '000103', 'ts格式有误')

    @allure.story('查询逐笔成交统计(优化)_code不正确')
    def test_tradesta20_codeno(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_code不正确')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_code异常')
    def test_tradesta20_codeyc(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_code异常')
        assert_data(response, '000000', 'ok')

    @allure.story('查询逐笔成交统计(优化)_code为空')
    def test_tradestayh_codenone(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_code为空')
        assert_data(response, '000103', 'code格式有误')

    @allure.story('查询逐笔成交统计(优化)_参数为空')
    def test_tradestayh_codenone(self):
        response = zhuorui('个股详情公共接口', '查询逐笔成交统计(优化)_参数为空')
        assert_data(response, '000103', 'ts格式有误')

if __name__ == '__main__':
    pytest.main()
