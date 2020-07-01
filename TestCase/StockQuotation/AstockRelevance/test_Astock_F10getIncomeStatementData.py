import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockF10getIncomeStatementData:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('A股F10获取利润表详情页数据')
    def test_Astock_F10getIncomeStatementData(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_token为0')
    def test_Astock_F10getIncomeStatementData_notoken(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_token为0')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_ts为空')
    def test_Astock_F10getIncomeStatementData_tsNone(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_ts为空')
        assert_data(response, '000103', 'ts不能为空')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_ts为异常')
    def test_Astock_F10getIncomeStatementData_tsException(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_ts为异常')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_code为空')
    def test_Astock_F10getIncomeStatementData_codeNone(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_code为空')
        assert_data(response, '000103', 'code不能为空')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_ts为错误')
    def test_Astock_F10getIncomeStatementData_tsError(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_ts为错误')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_code为异常')
    def test_Astock_F10getIncomeStatementData_codeException(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_code为异常')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('A股F10获取利润表详情页数据_code为错误')
    def test_Astock_F10getIncomeStatementData_codeError(self):
        response = zhuorui('A股', 'A股F10获取利润表详情页数据_code为错误')
        assert_data(response, '000000', 'ok')
        # print(response.text)





