import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockReportDetailsList:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('个股研报分页查询')
    def test_Astock_report_details_list(self):
        response = zhuorui('A股', '个股研报分页查询')
        assert_data(response, '000000', 'ok')