import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockNewstcokList:
    def setup_class(cls) -> None:
        login()

    @allure.story('新股日历获取待上市列表')
    def test_Astock_newstcok_list(self):
        response = zhuorui('A股', '新股日历获取待上市列表')
        # print(response)
        assert_data(response, '000000', 'ok')