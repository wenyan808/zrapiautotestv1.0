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
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('新股日历分页获取已上市列表_token为0')
    def test_Astock_newstcok_listedpage_notoken(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_token为0')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('新股日历分页获取已上市列表_上市日期')
    def test_Astock_newstcok_listedpage_ListingDate(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_上市日期')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('新股日历分页获取已上市列表_发行价')
    def test_Astock_newstcok_listedpage_Offerprice(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_发行价')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('新股日历分页获取已上市列表_现价')
    def test_Astock_newstcok_listedpage_price(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_现价')
        # print(response.text)
        assert_data(response, '000000', 'ok')


    @allure.story('新股日历分页获取已上市列表_总市值')
    def test_Astock_newstcok_listedpage_MktCap(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_总市值')
        # print(response.text)
        assert_data(response, '000000', 'ok')


    @allure.story('新股日历分页获取已上市列表_currentPage为空')
    def test_Astock_newstcok_listedpage_currentPageNone(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_currentPage为空')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('新股日历分页获取已上市列表_currentPage为错误')
    def test_Astock_newstcok_listedpage_currentPageError(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_currentPage为错误')
        # print(response.text)
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('新股日历分页获取已上市列表_currentPage为异常')
    def test_Astock_newstcok_listedpage_currentPageException(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_currentPage为异常')
        # print(response.text)
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('新股日历分页获取已上市列表_只传currentPage')
    def test_Astock_newstcok_listedpage_onlycurrentPage(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_只传currentPage')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('新股日历分页获取已上市列表_pageSize为空')
    def test_Astock_newstcok_listedpage_pageSizeNone(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_pageSize为空')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('新股日历分页获取已上市列表_pageSize为异常')
    def test_Astock_newstcok_listedpage_pageSizeException(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_pageSize为异常')
        # print(response.text)
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('新股日历分页获取已上市列表_pageSize为错误')
    def test_Astock_newstcok_listedpage_pageSizeError(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_pageSize为错误')
        # print(response.text)
        # assert_data(response, '000000', 'ok')
        assert_data(response, '000001', '系统繁忙,请稍候再试')

    @allure.story('新股日历分页获取已上市列表_只传pageSize')
    def test_Astock_newstcok_listedpage_onlypageSize(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_只传pageSize')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('新股日历分页获取已上市列表_order为空')
    def test_Astock_newstcok_listedpage_orderNone(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_order为空')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('新股日历分页获取已上市列表_order为异常')
    def test_Astock_newstcok_listedpage_orderException(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_order为异常')
        # print(response.text)
        assert_data(response, '000103', 'must be less than or equal to 4')

    @allure.story('新股日历分页获取已上市列表_order为错误')
    def test_Astock_newstcok_listedpage_orderError(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_order为错误')
        # print(response.text)
        assert_data(response, '000103', '参数校验不通过')

    @allure.story('新股日历分页获取已上市列表_只传order')
    def test_Astock_newstcok_listedpage_onlyorder(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_只传order')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('新股日历分页获取已上市列表_asc为空')
    def test_Astock_newstcok_listedpage_ascNone(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_asc为空')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('新股日历分页获取已上市列表_只传asc')
    def test_Astock_newstcok_listedpage_onlyasc(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_只传asc')
        # print(response.text)
        assert_data(response, '000000', 'ok')

    @allure.story('新股日历分页获取已上市列表_asc为升序')
    def test_Astock_newstcok_listedpage_ascOftrue(self):
        response = zhuorui('A股', '新股日历分页获取已上市列表_asc为升序')
        # print(response.text)
        assert_data(response, '000000', 'ok')









