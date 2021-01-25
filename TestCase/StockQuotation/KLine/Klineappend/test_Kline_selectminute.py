# test_Kline_selectminute
import json
import random

import allure
import pytest
import requests

from Common.get_time_stamp import TimeTostamp, get_time_stamp13
from Common.login import login
from Common.show_sql import showsql

from Common.sign import get_sign
from Common.tools.read_write_json import get_json, write_json

from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('K线')
class TestKlineSelectminute:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            "192.168.1.237", "root", "123456", "stock_market",
            "select ts,code from t_stock_search;"
        )  # 可以添加条件筛选：where ts='HK' or ts='SH' or ts='SZ' or ts='US'
        random_stock = random.sample(ts_code, 500)
        ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/test_Kline_selectminute.json", ts_code_data)

    @allure.story('查询分时')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/test_Kline_selectminute.json"))
    def test_Kline_selectminute(self, info):
        # pass
        url = HTTP + "/as_market/api/kline/v1/select_minute"
        header = JSON

        # 拼装参数
        paylo = {
            "startTime": TimeTostamp(),
            "endTime": get_time_stamp13(),
            "limit": 50
        }
        paylo1 = info
        paylo.update(paylo1)
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
                assert "type" in j.get("data")
                assert "ts" in j.get("data")
                assert j.get("data").get("ts") == info.get("ts")
                assert "code" in j.get("data")
                assert j.get("data").get("code") == info.get("code")
                if "preClose" in j.get("data"):
                    assert "preClose" in j.get("data")
                assert "adj" in j.get("data")
                if "list" in j.get("data"):
                    for i in range(len(j.get("data").get("list"))):
                        assert "time" in j.get("data").get("list")[i]
                        if "close" in j.get("data").get("list")[i]:
                            assert "close" in j.get("data").get("list")[i]
                        if "sharestraded" in j.get("data").get("list")[i]:
                            assert "sharestraded" in j.get("data").get("list")[i]
                        if "turnover" in j.get("data").get("list")[i]:
                            assert "turnover" in j.get("data").get("list")[i]
                        if "vwap" in j.get("data").get("list")[i]:
                            assert "vwap" in j.get("data").get("list")[i]
