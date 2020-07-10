import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestAfterPowerFactor:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询最新复权因子_SH大盘_000001')
    def test_AfterPowerFactor_SHtape_000001(self):
        response = zhuorui('k线', '查询最新复权因子_SH大盘_000001')
        assert_data(response, '000000', 'ok')
        # assert response.json().get("data") == 1
        # print(response.json())

    @allure.story('查询最新复权因子_SH大盘_000159')
    def test_AfterPowerFactor_SHtape_000159(self):
        response = zhuorui('k线', '查询最新复权因子_SH大盘_000159')
        assert_data(response, '000000', 'ok')
        # assert response.json().get("data") == 1
        # print(response.json())

    # @allure.story('查询最新复权因子_SH大盘')
    # def test_AfterPowerFactor_SHtape_HSCCI(self):
    #     response = zhuorui('k线', '查询最新复权因子_SH大盘')
    #     assert_data(response, '000000', 'ok')
    #     # print(response.json())
    #
    # @allure.story('查询最新复权因子_SH大盘')
    # def test_AfterPowerFactor_SHtape_CES100(self):
    #     response = zhuorui('k线', '查询最新复权因子_SH大盘')
    #     assert_data(response, '000000', 'ok')
    #     # print(response.json())
    #
    # @allure.story('查询最新复权因子_SH大盘')
    # def test_AfterPowerFactor_SHtape(self):
    #     response = zhuorui('k线', '查询最新复权因子_SH大盘')
    #     assert_data(response, '000000', 'ok')
    #     # print(response.json())


    @allure.story('查询最新复权因子_SH大盘_ts为空')
    def test_AfterPowerFactor_SHtape_tsNone(self):
        response = zhuorui('k线', '查询最新复权因子_SH大盘_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_SH大盘_ts为中文')
    def test_AfterPowerFactor_SHtape_tschinese(self):
        response = zhuorui('k线', '查询最新复权因子_SH大盘_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_只传ts')
    def test_AfterPowerFactor_SHtape_onlyvalts(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_只传ts')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_code为空')
    def test_AfterPowerFactor_SHtape_codeNone(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_code为空')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_code为中文')
    def test_AfterPowerFactor_SHtape_codechinese(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_code为中文')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_只传code')
    def test_AfterPowerFactor_SHtape_onlyvalcode(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_只传code')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_无token')
    def test_AfterPowerFactor_SHtape_notoken(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_无token')
        assert_data(response, '000000', 'ok')
        assert response.json().get("data") == 1
        # print(response.json())

    # @allure.story('查询最新复权因子_SH大盘')
    # def test_AfterPowerFactor_SHtape(self):
    #     response = zhuorui('k线', '查询最新复权因子_SH大盘')
    #     # assert_data(response, '000000', 'ok')
    #     print(response.json())