import logging

import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


@allure.feature('港股')
class testHKstockNewstockOrdered:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('新股可认购-简况_HK')
    def test_HKstock_NewstockOrdered_HK(self):
        response = zhuorui('港股', '新股可认购-简况_HK')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # for i in range(len(response.json().get("data"))):
                assert "priceLow" in response.json().get("data")
                assert "priceHigh" in response.json().get("data")
                assert "volunit" in response.json().get("data")
                assert "startDate" in response.json().get("data")
                assert "entranceFee" in response.json().get("data")
                assert "endDate" in response.json().get("data")
                assert "listingDate" in response.json().get("data")
                assert "industry" in response.json().get("data")
                assert "totalNumber" in response.json().get("data")
                assert "totalCapitalStock" in response.json().get("data")
                assert "totalMarketValueLow" in response.json().get("data")
                assert "totalMarketValueHigh" in response.json().get("data")
                assert "sponsor" in response.json().get("data")
                assert "cornerstoneInvestors" in response.json().get("data")
                assert "companyDesc" in response.json().get("data")
                assert "mainStockHolders" in response.json().get("data")
                assert "url" in response.json().get("data")

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('新股可认购-简况_HK_无token')
    def test_HKstock_NewstockOrdered_HK_notoken(self):
        response = zhuorui('港股', '新股可认购-简况_HK_无token')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('新股可认购-简况_HK_ts为US')
    def test_HKstock_NewstockOrdered_HK_tsofUS(self):
        response = zhuorui('港股', '新股可认购-简况_HK_ts为US')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('新股可认购-简况_HK_ts为空')
    def test_HKstock_NewstockOrdered_HK_tsNone(self):
        response = zhuorui('港股', '新股可认购-简况_HK_ts为空')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('新股可认购-简况_HK_ts为中文')
    def test_HKstock_NewstockOrdered_HK_tsofchinese(self):
        response = zhuorui('港股', '新股可认购-简况_HK_ts为中文')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('新股可认购-简况_HK_code为空')
    def test_HKstock_NewstockOrdered_HK_codeNone(self):
        response = zhuorui('港股', '新股可认购-简况_HK_code为空')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('新股可认购-简况_HK_code为中文')
    def test_HKstock_NewstockOrdered_HK_codeofchinese(self):
        response = zhuorui('港股', '新股可认购-简况_HK_code为中文')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('新股可认购-简况_HK_code为PDD')
    def test_HKstock_NewstockOrdered_HK_codeofPDD(self):
        response = zhuorui('港股', '新股可认购-简况_HK_code为PDD')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('新股可认购-简况_HK_只传code')
    def test_HKstock_NewstockOrdered_HK_onlycode(self):
        response = zhuorui('港股', '新股可认购-简况_HK_只传code')
        assert_data(response, '000103', 'ts格式有误')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('新股可认购-简况_HK_只传ts')
    def test_HKstock_NewstockOrdered_HK_onlyts(self):
        response = zhuorui('港股', '新股可认购-简况_HK_只传ts')
        assert_data(response, '000103', 'code格式有误')
        assert response.status_code == 200
        # print(response.json())