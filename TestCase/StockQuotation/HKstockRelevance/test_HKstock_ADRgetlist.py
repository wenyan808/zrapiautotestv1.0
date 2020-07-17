import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class testHKstockADRgetlist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('ADR列表 -港股ADR')
    def test_HKstock_ADRgetlist(self):
        response = zhuorui('港股', 'ADR列表 -港股ADR')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
