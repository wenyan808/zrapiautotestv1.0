import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('k线')
class TestAfterPowerFactor:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('查询最新复权因子_HK大盘_HSI')
    def test_AfterPowerFactor_HKtape_HSI(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_HSI')
        assert_data(response, '000000', 'ok')
        assert response.json().get("data") == 1
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_HSCEI')
    def test_AfterPowerFactor_HKtape_HSCEI(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_HSCEI')
        assert_data(response, '000000', 'ok')
        assert response.json().get("data") == 1
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_HSCCI')
    def test_AfterPowerFactor_HKtape_HSCCI(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_HSCCI')
        assert_data(response, '000000', 'ok')
        assert response.json().get("data") == 1
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_CES100')
    def test_AfterPowerFactor_HKtape_CES100(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_CES100')
        assert_data(response, '000000', 'ok')
        assert response.json().get("data") == 1
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_CES300')
    def test_AfterPowerFactor_HKtape_CES300(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_CES300')
        assert_data(response, '000000', 'ok')
        assert response.json().get("data") == 1
        # print(response.json())


    @allure.story('查询最新复权因子_HK大盘_ts为空')
    def test_AfterPowerFactor_HKtape_tsNone(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_ts为中文')
    def test_AfterPowerFactor_HKtape_tschinese(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_只传ts')
    def test_AfterPowerFactor_HKtape_onlyvalts(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_只传ts')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_code为空')
    def test_AfterPowerFactor_HKtape_codeNone(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_code为空')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_code为中文')
    def test_AfterPowerFactor_HKtape_codechinese(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_code为中文')
        assert_data(response, '000103', 'code格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_只传code')
    def test_AfterPowerFactor_HKtape_onlyvalcode(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_只传code')
        assert_data(response, '000103', 'ts格式有误')
        # print(response.json())

    @allure.story('查询最新复权因子_HK大盘_无token')
    def test_AfterPowerFactor_HKtape_notoken(self):
        response = zhuorui('k线', '查询最新复权因子_HK大盘_无token')
        assert_data(response, '000000', 'ok')
        assert response.json().get("data") == 1
        # print(response.json())

    # @allure.story('查询最新复权因子_HK大盘')
    # def test_AfterPowerFactor_HKtape(self):
    #     response = zhuorui('k线', '查询最新复权因子_HK大盘')
    #     # assert_data(response, '000000', 'ok')
    #     print(response.json())
