import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('A股')
class TestAstockNewstcokCount:
    def setup_class(cls) -> None:
        login()

    @allure.story('新股日历获取待上市、今日上市数量')
    def test_Astock_newstcok_count(self):
        response = zhuorui('A股', '新股日历获取待上市、今日上市数量')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('新股日历获取待上市、今日上市数量_token为0')
    def test_Astock_newstcok_count_notohen(self):
        response = zhuorui('A股', '新股日历获取待上市、今日上市数量_token为0')
        # print(response.text)
        assert_data(response, '000000', 'ok')




