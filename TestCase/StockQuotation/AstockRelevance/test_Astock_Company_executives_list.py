import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockCompanyExecutivesList:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('公司高管列表-详情页')
    def test_Astock_Company_executives_list(self):
        response = zhuorui('A股', '公司高管列表-详情页')
        assert_data(response, '000000', 'ok')