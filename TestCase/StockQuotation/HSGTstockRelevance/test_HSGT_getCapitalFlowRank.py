import logging

import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login


# test_HSGT_getCapitalFlowRank
# @pytest.mark.skip(reason="调试中，返回的结果是404")
@allure.feature('沪深港股通资金流向排行榜')
class TestHSGTgetCapitalFlowRank:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('沪深港股通资金流向排行榜_沪股通')
    def test_HSGT_getCapitalFlowRank_1(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_沪股通')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_深股通')
    def test_HSGT_getCapitalFlowRank_2(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_深股通')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_港股通')
    def test_HSGT_getCapitalFlowRank_3(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_港股通')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_港股通(沪)')
    def test_HSGT_getCapitalFlowRank_4(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_港股通(沪)')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_港股通(深)')
    def test_HSGT_getCapitalFlowRank_5(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_港股通(深)')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_queryDay为5')
    def test_HSGT_getCapitalFlowRank_queryDayof5(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_queryDay为5')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_queryDay为20')
    def test_HSGT_getCapitalFlowRank_queryDayof20(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_queryDay为5')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_queryDay为60')
    def test_HSGT_getCapitalFlowRank_queryDayof60(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_queryDay为5')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_queryDay为空')
    def test_HSGT_getCapitalFlowRank_queryDaynull(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_queryDay为空')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_净买卖股数')
    def test_HSGT_getCapitalFlowRank_one(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_净买卖股数')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_资金净流向')
    def test_HSGT_getCapitalFlowRank_two(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_资金净流向')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]

                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_流通股比例')
    def test_HSGT_getCapitalFlowRank_three(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_流通股比例')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_升序')
    def test_HSGT_getCapitalFlowRank_asce(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_升序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_逆序')
    def test_HSGT_getCapitalFlowRank_desc(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_逆序')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_pageSize为10')
    def test_HSGT_getCapitalFlowRank_pageSizeof10(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_pageSize为10')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")

    @allure.story('沪深港股通资金流向排行榜_currentPage为21')
    def test_HSGT_getCapitalFlowRank_currentPageof21(self):
        response = zhuorui('沪深港通', '沪深港股通资金流向排行榜_currentPage为21')
        assert_data(response, '000000', 'ok')
        assert response.status_code == 200
        # print(response.json())
        if "data" in response.json():
            if len(response.json().get("data")) != 0:
                # pass
                # for i in range(len(response.json().get("data"))):
                assert "date" in response.json().get("data")
                assert "list" in response.json().get("data")
                if len(response.json().get("data").get("list")) != 0:
                    for i in range(len(response.json().get("data").get("list"))):
                        # pass
                        assert "ts" in response.json().get("data").get("list")[i]
                        assert "code" in response.json().get("data").get("list")[i]
                        assert "type" in response.json().get("data").get("list")[i]
                        assert "delay" in response.json().get("data").get("list")[i]
                        assert "name" in response.json().get("data").get("list")[i]
                        assert "netStockVolume" in response.json().get("data").get("list")[i]
                        # assert "netCapitalFlow" in response.json().get("data").get("list")[i]
                        # assert "flowStockRatio" in response.json().get("data").get("list")[i]

            else:
                logging.info("data是空的集合")

        else:

            logging.info("无data数据")