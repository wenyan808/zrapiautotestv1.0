import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockReportDetails:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('个股研报详情')
    def test_Astock_report_details(self):
        response = zhuorui('A股', '个股研报详情')
        assert_data(response, '000000', 'ok')

    # @allure.story('个股研报详情')
    # def test_ggxgfhpxgg(self):
    #     response = zhuorui('个股研报详情')
    #     assert_data(response, '000000', 'ok')
    #
    # @allure.story('个股研报详情')
    # def test_hqggjj(self):
    #     response = zhuorui('个股研报详情')
    #     assert_data(response, '000000', 'ok')
    #
    # @allure.story('个股研报详情')
    # def test_ggxwfy(self):
    #     response = zhuorui('个股研报详情')
    #     assert_data(response, '000200', '数据不存在，操作失败')

    # @allure.story('查询股票市场涨跌概况_参数为空‘)
    # def test_sczdgk(self):
    # 	zhuorui('查询股票市场涨跌概况_参数为空')

    # @allure.story('查询股票市场涨跌概况_参数为4')
    # def test_sczdgk(self):
    #     response = zhuorui('查询股票市场涨跌概况_参数为0')
    #     assert_data(response, '000200', '数据不存在，操作失败')


if __name__ == '__main__':
    pytest.main()
