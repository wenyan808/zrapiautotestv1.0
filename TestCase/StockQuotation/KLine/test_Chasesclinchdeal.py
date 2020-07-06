import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('逐笔成交')
class TestChasesClinchDeal:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询逐笔成交统计_US个股')
    def test_Chasesclinchdeal_USshare(self):
        response = zhuorui('逐笔成交', '查询逐笔成交统计_US个股')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询逐笔成交统计_SH个股')
    def test_Chasesclinchdeal_SHshare(self):
        response = zhuorui('逐笔成交', '查询逐笔成交统计_SH个股')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询逐笔成交统计_SZ个股')
    def test_Chasesclinchdeal_SZshare(self):
        response = zhuorui('逐笔成交', '查询逐笔成交统计_SZ个股')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询逐笔成交统计_HK个股')
    def test_Chasesclinchdeal_HKshare(self):
        response = zhuorui('逐笔成交', '查询逐笔成交统计_HK个股')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询逐笔成交_US大盘')
    def test_Chasesclinchdeal_UStape(self):
        response = zhuorui('逐笔成交', '查询逐笔成交_US大盘')
        assert_data(response, '000008', '权限不足')
        # print(response.text)

    @allure.story('查询逐笔成交_US个股')
    def test_Chasesclinchdeal_USshare(self):
        response = zhuorui('逐笔成交', '查询逐笔成交_US个股')
        assert_data(response, '000008', '权限不足')
        # print(response.text)

    @allure.story('查询逐笔成交_HS大盘')
    def test_Chasesclinchdeal_HStape(self):
        response = zhuorui('逐笔成交', '查询逐笔成交_HS大盘')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询逐笔成交_HS个股')
    def test_Chasesclinchdeal_HSshare(self):
        response = zhuorui('逐笔成交', '查询逐笔成交_HS个股')
        assert_data(response, '000000', 'ok')
        # print(response.text)

    @allure.story('查询逐笔成交_HK大盘')
    def test_Chasesclinchdeal_HKtape(self):
        response = zhuorui('逐笔成交', '查询逐笔成交_HK大盘')
        assert_data(response, '000008', '权限不足')
        # print(response.text)

    @allure.story('查询逐笔成交_HK个股')
    def test_Chasesclinchdeal_HKshare(self):
        response = zhuorui('逐笔成交', '查询逐笔成交_HK个股')
        assert_data(response, '000008', '权限不足')
        # print(response.text)
