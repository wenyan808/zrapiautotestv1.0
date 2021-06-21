# test_US_newslist
import json
import logging
import random
import time

import allure
import pytest
import requests

from Common.login import login
from Common.show_sql import showsql
from Common.sign import get_sign
from Common.tools.read_write_json import write_json, get_json
from Common.tools.read_yaml import yamltoken
from glo import BASE_DIR, HTTP, JSON


# test_getStockjump
# @pytest.mark.skip(reason="调试中，返回的结果是404")
@allure.feature('美股相关')
class TestUSNewslist:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('个股新闻分页查询')
    def test_US_newslist(self):
        # pass
        url = HTTP + "/as_market/api/us/news/v1/list"
        header = JSON

        # 拼装参数

        paylo = {
            "ts": "US",
            "code": "TSLA"
        }
        # paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        # 调用登录接口通过token传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = {}
        headers.update(header)
        # print(token)
        # print(type(token))

        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)
        # print(headers)
        payload = json.dumps(dict(payload1))
        # time.sleep(1)
        r = requests.post(url=url, headers=headers, data=payload)
        # 断言
        j = r.json()
        # print(j)

        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                if "list" in j.get("data"):
                    for i in range(len(j.get("data").get("list"))):
                        assert "newsId" in j.get("data").get("list")[i]
                        assert "createTime" in j.get("data").get("list")[i]
                        assert "newsTitle" in j.get("data").get("list")[i]
                        assert "detailUrl" in j.get("data").get("list")[i]
                        assert j.get("data").get("list")[i].get(
                            "detailUrl") == "http://192.168.1.239:8080/zhuorui_h5/newsDetail" + "?" + \
                               f"id={j.get('data').get('list')[i].get('newsId')}" + \
                               "&" + f"ts={paylo.get('ts')}"

                assert "total" in j.get("data")
                assert "pageSize" in j.get("data")
                assert "currentPage" in j.get("data")
                assert j.get("data").get("pageSize") == 15
                assert j.get("data").get("currentPage") == 1

            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")

    @allure.story('个股新闻分页查询_all')
    # @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/getnewslist.json"))
    def test_US_newslist_all(self):
        # pass
        url = HTTP + "/as_market/api/us/news/v1/list"
        header = JSON

        # 拼装参数

        paylo = {
            "ts": "US",
            "code": "TSLA",
            "pageSize": 15,
            "currentPage": 2
        }
        # paylo = info
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        # 调用登录接口通过token传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = {}
        headers.update(header)
        # print(token)
        # print(type(token))

        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)
        # print(headers)
        payload = json.dumps(dict(payload1))
        # time.sleep(1)
        r = requests.post(url=url, headers=headers, data=payload)
        # 断言
        j = r.json()
        # print(j)

        assert r.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            if len(j.get("data")) != 0:
                if "list" in j.get("data"):
                    for i in range(len(j.get("data").get("list"))):
                        assert "newsId" in j.get("data").get("list")[i]
                        assert "createTime" in j.get("data").get("list")[i]
                        assert "newsTitle" in j.get("data").get("list")[i]
                        assert "detailUrl" in j.get("data").get("list")[i]
                        assert j.get("data").get("list")[i].get(
                            "detailUrl") == "http://192.168.1.239:8080/zhuorui_h5/newsDetail" + "?" + \
                               f"id={j.get('data').get('list')[i].get('newsId')}" + \
                               "&" + f"ts={paylo.get('ts')}"
                assert "total" in j.get("data")
                assert "pageSize" in j.get("data")
                assert "currentPage" in j.get("data")
                assert j.get("data").get("currentPage") == paylo.get("currentPage")

            else:
                logging.info("data是空的集合")

        else:
            logging.info("无data数据")
