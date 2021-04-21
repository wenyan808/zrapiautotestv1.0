# test_Newslist
import json
import logging
import random

import allure
import pytest
import requests


from Common.login import login
from Common.show_sql import showsql

from Common.sign import get_sign
from Common.tools.read_write_json import get_json, write_json

from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('公共分类')
class TestNewslist:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            '192.168.1.237', 'root', '123456', 'stock_market',
            "select ts,code from t_stock_search;"
        )
        random_stock = random.sample(ts_code, 500)
        ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/AllStockData/test_Newslis.json", ts_code_data)

    @allure.story('查询资讯新闻列表分页')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/test_Newslis.json"))
    def test_Newslist(self, info):
        # pass
        url = HTTP + "/as_market/api/hk/news/v1/news/list"
        headers = JSON

        # 拼装参数
        paylo = {
            "currentPage": 1,
            "pageSize": 15
        }
        paylo1 = {
            "code": f'{info.get("code")}'
        }
        paylo.update(paylo1)
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        # 调用登录接口通过token传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = headers
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
            for i in range(len(j.get("data").get("list"))):
                assert "newsId" in j.get("data").get("list")[i]
                assert "createTime" in j.get("data").get("list")[i]
                assert "newsTitle" in j.get("data").get("list")[i]
                assert "newsType" in j.get("data").get("list")[i]
                assert "newsFlag" in j.get("data").get("list")[i]
                if "detailUrl" in j.get("data").get("list")[i]:
                    assert "http://192.168.1.239:8080/zhuorui_h5/newsDetail" \
                           in j.get("data").get("list")[i].get("detailUrl")
                    a = j.get("data").get("list")[i].get("newsId")
                    b = j.get("data").get("list")[i].get("newsFlag")
                    assert j.get("data").get("list")[i].get("detailUrl") == \
                           "http://192.168.1.239:8080/zhuorui_h5/newsDetail" \
                           + f"?id={a}&newsFlag={b}&ts={info.get('ts')}"
            assert "total" in j.get("data")
            assert j.get("data").get("pageSize") == paylo.get("pageSize")
            assert j.get("data").get("currentPage") == paylo.get("currentPage")
