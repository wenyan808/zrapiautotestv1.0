import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockNewstcokListpage:
    def setup_class(cls) -> None:
        login()

    @allure.story('新股日历分页获取已上市列表')
    def test_Astock_newstcok_listedpage(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表')
        # print(response)
        assert_data(response, '000000', 'ok')