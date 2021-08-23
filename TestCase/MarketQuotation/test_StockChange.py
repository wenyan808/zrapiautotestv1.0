#字段说明：
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login, login_common


@allure.feature('板快行情')
class TestClass():

    @classmethod
    def setup_class(cls) -> None:
        login_common()

    @allure.story('根据市场查询港股股票异动数据')
    def test_listHK(self):
        response = zhuorui('市场行情', '根据市场查询港股股票异动数据')
        assert_data(response, '000000', 'ok')

    @allure.story('根据市场查询美股股票异动数据')
    def test_listUS(self):
        response = zhuorui('市场行情', '根据市场查询美股股票异动数据')
        assert_data(response, '000000', 'ok')

    @allure.story('根据市场查询A股股票异动数据')
    def test_listA(self):
        response = zhuorui('市场行情', '根据市场查询A股股票异动数据')
        assert_data(response, '000000', 'ok')

    @allure.story('根据行业查询股票异动数据_港股行业为空')
    def test_industryHKNULL(self):
        response = zhuorui('市场行情', '根据行业查询股票异动数据_港股行业为空')
        assert_data(response, '000000', 'ok')

    @allure.story('根据行业查询股票异动数据_美股行业为空')
    def test_industryUSNULL(self):
        response = zhuorui('市场行情', '根据行业查询股票异动数据_美股行业为空')
        assert_data(response, '000000', 'ok')

    @allure.story('根据行业查询股票异动数据_A股行业为空')
    def test_industryANULL(self):
        response = zhuorui('市场行情', '根据行业查询股票异动数据_A股行业为空')
        assert_data(response, '000000', 'ok')

    @allure.story('根据行业查询股票异动数据_港股行业')
    def test_industryHK(self):
        response = zhuorui('市场行情', '根据行业查询股票异动数据_港股行业')
        assert_data(response, '000000', 'ok')

    @allure.story('根据行业查询股票异动数据_美股行业')
    def test_industryUS(self):
        response = zhuorui('市场行情', '根据行业查询股票异动数据_美股行业')
        assert_data(response, '000000', 'ok')

    @allure.story('根据行业查询股票异动数据_A股行业')
    def test_industryA(self):
        response = zhuorui('市场行情', '根据行业查询股票异动数据_A股行业')
        assert_data(response, '000000', 'ok')

    @allure.story('根据指数查询股票异动数据_港股为空')
    def test_indexHKNULL(self):
        response = zhuorui('市场行情', '根据指数查询股票异动数据_港股为空')
        assert_data(response, '000000', 'ok')

    @allure.story('根据指数查询股票异动数据_美股为空')
    def test_indexUSNULL(self):
        response = zhuorui('市场行情', '根据指数查询股票异动数据_美股为空')
        assert_data(response, '000000', 'ok')

    @allure.story('根据指数查询股票异动数据_A股为空')
    def test_indexANULL(self):
        response = zhuorui('市场行情', '根据指数查询股票异动数据_A股为空')
        assert_data(response, '000000', 'ok')

    @allure.story('根据指数查询股票异动数据_港股恒生')
    def test_indexHSI(self):
        response = zhuorui('市场行情', '根据指数查询股票异动数据_港股恒生')
        assert_data(response, '000000', 'ok')

    @allure.story('根据指数查询股票异动数据_港股国企')
    def test_indexHSCEI(self):
        response = zhuorui('市场行情', '根据指数查询股票异动数据_港股国企')
        assert_data(response, '000000', 'ok')

    @allure.story('根据指数查询股票异动数据_港股红筹')
    def test_indexHSCCI(self):
        response = zhuorui('市场行情', '根据指数查询股票异动数据_港股红筹')
        assert_data(response, '000000', 'ok')

    @allure.story('根据指数查询股票异动数据_美股道指')
    def test_indexUSDIA(self):
        response = zhuorui('市场行情', '根据指数查询股票异动数据_美股道指')
        assert_data(response, '000000', 'ok')

    @allure.story('根据指数查询股票异动数据_美股纳指')
    def test_indexUSQQQ(self):
        response = zhuorui('市场行情', '根据指数查询股票异动数据_美股纳指')
        assert_data(response, '000000', 'ok')

    @allure.story('根据指数查询股票异动数据_美股标普')
    def test_indexUSSPY(self):
        response = zhuorui('市场行情', '根据指数查询股票异动数据_美股标普')
        assert_data(response, '000000', 'ok')

    @allure.story('根据指数查询股票异动数据_A股上证')
    def test_indexA1(self):
        response = zhuorui('市场行情', '根据指数查询股票异动数据_A股上证')
        assert_data(response, '000000', 'ok')

    @allure.story('根据指数查询股票异动数据_A股深证')
    def test_index2(self):
        response = zhuorui('市场行情', '根据指数查询股票异动数据_A股深证')
        assert_data(response, '000000', 'ok')

    @allure.story('根据指数查询股票异动数据_A股创业')
    def test_index3(self):
        response = zhuorui('市场行情', '根据指数查询股票异动数据_A股创业')
        assert_data(response, '000000', 'ok')

    @allure.story('根据自选股查询股票异动数据')
    def test_list_selected(self):
        response = zhuorui('市场行情', '根据自选股查询股票异动数据')
        assert_data(response, '000000', 'ok')

    @allure.story('根据股票查询股票异动数据_港股00700')
    def test_codeHK(self):
        response = zhuorui('市场行情', '根据股票查询股票异动数据_港股00700')
        assert_data(response, '000000', 'ok')

    @allure.story('根据股票查询股票异动数据_A股002594')
    def test_codeA(self):
        response = zhuorui('市场行情', '根据股票查询股票异动数据_A股002594')
        assert_data(response, '000000', 'ok')

    @allure.story('根据股票查询股票异动数据_美股GOOG')
    def test_codeUS(self):
        response = zhuorui('市场行情', '根据股票查询股票异动数据_美股GOOG')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票异动设置模板')
    def test_template(self):
        response = zhuorui('市场行情', '查询股票异动设置模板')
        assert_data(response, '000000', 'ok')

    @allure.story('同步股票异动设置_不关闭')
    def test_sys(self):
        response = zhuorui('市场行情', '同步股票异动设置_不关闭')
        assert_data(response, '000000', 'ok')

    @allure.story('同步股票异动设置_关闭所有')
    def test_sys(self):
        response = zhuorui('市场行情', '同步股票异动设置_关闭所有')
        assert_data(response, '000000', 'ok')

    @allure.story('查询股票异动设置')
    def test_sys(self):
        response = zhuorui('市场行情', '查询股票异动设置')
        assert_data(response, '000000', 'ok')