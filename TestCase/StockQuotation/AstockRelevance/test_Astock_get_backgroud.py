import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockGetBackgroud:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('获取高管的简介')
    def test_Astock_get_backgroud(self):
        response = zhuorui('A股', '获取高管的简介')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('获取高管的简介_token为0')
    def test_Astock_get_backgroud_notoken(self):
        response = zhuorui('A股', '获取高管的简介_token为0')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('获取高管的简介_comCode为空')
    def test_Astock_get_backgroud_comCodeNone(self):
        response = zhuorui('A股', '获取高管的简介_comCode为空')
        assert_data(response, '000103', 'comCode不能为空')
        # print(response.text)

    @allure.story('获取高管的简介_comCode为异常')
    def test_Astock_get_backgroud_comCodeException(self):
        response = zhuorui('A股', '获取高管的简介_comCode为异常')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('获取高管的简介_comCode为错误')
    def test_Astock_get_backgroud_comCodeError(self):
        response = zhuorui('A股', '获取高管的简介_comCode为错误')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('获取高管的简介_pcode为空')
    def test_Astock_get_backgroud_pcodeNone(self):
        response = zhuorui('A股', '获取高管的简介_pcode为空')
        assert_data(response, '000103', 'pCode不能为空')
        # print(response.text)

    @allure.story('获取高管的简介_pcode为异常')
    def test_Astock_get_backgroud_pcodeException(self):
        response = zhuorui('A股', '获取高管的简介_pcode为异常')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('获取高管的简介_pcode为错误')
    def test_Astock_get_backgroud_pcodeError(self):
        response = zhuorui('A股', '获取高管的简介_pcode为错误')
        assert_data(response, '000103', '参数校验不通过')
        # print(response.text)

    @allure.story('获取高管的简介_只传值comCode')
    def test_Astock_get_backgroud_onlyvalcomCode(self):
        response = zhuorui('A股', '获取高管的简介_只传值comCode')
        assert_data(response, '000103', 'pCode不能为空')
        # print(response.text)

    @allure.story('获取高管的简介_只传值pcode')
    def test_Astock_get_backgroud_onlyvalpcode(self):
        response = zhuorui('A股', '获取高管的简介_只传值pcode')
        assert_data(response, '000103', 'comCode不能为空')
        # print(response.text)


