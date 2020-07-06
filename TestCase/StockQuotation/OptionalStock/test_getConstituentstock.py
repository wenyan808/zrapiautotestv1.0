import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('成分股')
class TestgetConstituentStock:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询成份股_必选参数港股')
    def test_getConstituentstock_onlyhk(self):
        response = zhuorui('成分股', '查询成份股_必选参数港股')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询成份股_组合可选参数')
    def test_getConstituentstock_combine(self):
        response = zhuorui('成分股', '查询成份股_组合可选参数')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询成份股_必选参数空')
    def test_getConstituentstock_None(self):
        response = zhuorui('成分股', '查询成份股_必选参数空')
        assert_data(response, '000103', 'code is not null')
        # print(response.text)

    @allure.story('查询成份股_必选参数沪深')
    def test_getConstituentstock_onlysh(self):
        response = zhuorui('成分股', '查询成份股_必选参数沪深')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询成份股_必选参数沪深其他')
    def test_getConstituentstock_onlyshother(self):
        response = zhuorui('成分股', '查询成份股_必选参数沪深其他')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询成份股_必选参数港股其他')
    def test_getConstituentstock_onlyhkother(self):
        response = zhuorui('成分股', '查询成份股_必选参数港股其他')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询成份股_Hk')
    def test_getConstituentstock_HK(self):
        response = zhuorui('成分股', '查询成份股_Hk')
        assert_data(response, '000000', 'ok')
        # print(response.text)


