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
        # print(response.text)

    @allure.story('个股研报详情_token为0')
    def test_Astock_report_details_notoken(self):
        response = zhuorui('A股', '个股研报详情_token为0')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('个股研报详情_id为None')
    def test_Astock_report_details_idNone(self):
        response = zhuorui('A股', '个股研报详情_id为None')
        assert_data(response, '000103', 'id不能为空')
        # print(response.text)

    @allure.story('个股研报详情_不传id')
    def test_Astock_report_details_notpassedonid(self):
        response = zhuorui('A股', '个股研报详情_不传id')
        assert_data(response, '000103', 'id不能为空')
        # print(response.text)
    #
    # @allure.story('A股', '个股研报详情')
    # def test_sczdgk(self):
    #     response = zhuorui('A股', '个股研报详情')
    #     assert_data(response, '000200', '数据不存在，操作失败')
    #     print(response.text)
    #
    # @allure.story('A股', '个股研报详情')
    # def test_sczdgk(self):
    #     response = zhuorui('A股', '个股研报详情')
    #     assert_data(response, '000200', '数据不存在，操作失败')
    #     print(response.text)


if __name__ == '__main__':
    pytest.main()
