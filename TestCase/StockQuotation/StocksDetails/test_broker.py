import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

@allure.feature("查询买卖经纪")
class TestBroker:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询买卖经纪_US大盘')
    def test_broker_US(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_US大盘')
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('查询买卖经纪_US个股')
    def test_broker_us(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_US个股')
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('查询买卖经纪_SZ大盘')
    def test_broker_SZ(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_SZ大盘')
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('查询买卖经纪_SZ个股')
    def test_broker_sz(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_SZ个股')
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('查询买卖经纪_SH大盘')
    def test_broker_SH(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_SH大盘')
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('查询买卖经纪_SH个股')
    def test_broker_sh(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_SH个股')
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('查询买卖经纪_HK大盘')
    def test_broker_HK(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_HK大盘')
        assert_data(response, '000000', 'ok')

    @allure.story('查询买卖经纪_HK个股')
    def test_broker_hk(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_HK个股')
        assert_data(response, '000000', 'ok')
        # print(response.json())

    @allure.story('查询买卖经纪_ts不正确')
    def test_broker_ts_error(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_ts不正确')
        assert_data(response, '000103', 'ts格式有误')

    @allure.story('查询买卖经纪_ts异常')
    def test_broker_ts_exception(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_ts异常')
        assert_data(response, '000103', 'ts格式有误')

    @allure.story('查询买卖经纪_ts为空')
    def test_broker_ts_null(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_ts为空')
        assert_data(response, '000103', 'ts格式有误')

    @allure.story('查询买卖经纪_code不正确')
    def test_broker_code_error(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_code不正确')
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('查询买卖经纪_code异常')
    def test_broker_code_exception(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_code异常')
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('查询买卖经纪_code为空')
    def test_broker_code_null(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_code为空')
        assert_data(response, '000103', 'code格式有误')

    @allure.story('查询买卖经纪_参数为空')
    def test_broker_parameter_null(self):
        response = zhuorui('个股详情公共接口', '查询买卖经纪_参数为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())
#
# if __name__ == '__main__':
#     pytest.main()
