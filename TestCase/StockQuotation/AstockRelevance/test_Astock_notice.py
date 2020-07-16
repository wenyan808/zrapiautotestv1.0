import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

@allure.feature('A股')
class TestAstockF10Briefing:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('个股相关分红派息公告查询')
    def test_Astock_F10_briefing(self):
        response = zhuorui('A股', '个股相关分红派息公告查询')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('个股相关分红派息公告查询_token为0')
    def test_Astock_F10_briefing_notoken(self):
        response = zhuorui('A股', '个股相关分红派息公告查询_token为0')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('个股相关分红派息公告查询_ts为空')
    def test_Astock_F10_briefing_tsNone(self):
        response = zhuorui('A股', '个股相关分红派息公告查询_ts为空')
        # print(response.text)
        assert_data(response, '000103', 'ts格式有误')
    #
    @allure.story('个股相关分红派息公告查询_ts为异常')
    def test_Astock_F10_briefing_tsException(self):
        response = zhuorui('A股', '个股相关分红派息公告查询_ts为异常')
        # print(response.text)
        assert_data(response, '000103', 'ts格式有误')

    @allure.story('个股相关分红派息公告查询_ts为错误')
    def test_Astock_F10_briefing_tsError(self):
        response = zhuorui('A股', '个股相关分红派息公告查询_ts为错误')
        # print(response.text)
        assert_data(response, '000103', 'ts格式有误')

    @allure.story('个股相关分红派息公告查询_code为空')
    def test_Astock_F10_briefing_codeNone(self):
        response = zhuorui('A股', '个股相关分红派息公告查询_code为空')
        # print(response.text)
        assert_data(response, '000103', 'code格式有误')

    @allure.story('个股相关分红派息公告查询_code为异常')
    def test_Astock_F10_briefing_codeException(self):
        response = zhuorui('A股', '个股相关分红派息公告查询_code为异常')
        # print(response.text)
        assert_data(response, '000103', 'code格式有误')

    @allure.story('个股相关分红派息公告查询_code为错误')
    def test_Astock_F10_briefing_codeError(self):
        response = zhuorui('A股', '个股相关分红派息公告查询_code为错误')
        # print(response.text)
        assert_data(response, '000000', 'ok')
#







