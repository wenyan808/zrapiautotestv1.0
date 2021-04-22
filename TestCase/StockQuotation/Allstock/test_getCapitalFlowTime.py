# test_getCapitalFlowTime
import json
import logging
import random

import allure
import pytest
import requests


from Common.login import login
from Common.show_sql import showsql

from Common.sign import get_sign
from Common.tools.read_write_json import write_json, get_json

from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# @pytest.mark.skip(reason="调试中")
@allure.feature('公共分类')
class TestGetCapitalFlowTime:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            '192.168.1.237', 'root', '123456', 'stock_market',
            "select ts,code,name from t_stock_search;"
        )
        random_stock = random.sample(ts_code, 100)
        stock_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/AllStockData/test_getCapitalFlowTime.json", stock_data)

    @allure.story('按时间查询资金统计数据')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/test_getCapitalFlowTime.json"))
    def test_getCapitalFlowTime(self, info):
        # pass
        url = HTTP + "/as_market/api/stock/view/v1/getCapitalFlowTime"
        headers = JSON

        # 拼装参数
        paylo = {
            "ts": info.get("ts"),
            "code": info.get("code"),
            "dayCount": 3
        }
        # paylo = info
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
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                if len(j.get("data")) != 0:
                    for i in range(len(j.get("data"))):
                        assert "totalInflowAndOutflow" in j.get("data")[i]
                        assert "totalInflowAndOutflow" in j.get("data")[i]
                        if "ts" in j.get("data")[i]:
                            assert j.get("data")[i].get("ts") == paylo.get("ts")
                        else:
                            logging.info(f"{paylo.get('ts')}不存在")
                        if "code" in j.get("data")[i]:
                            assert j.get("data")[i].get("code") == paylo.get("code")
                        else:
                            logging.info(f"{paylo.get('code')}不存在")
                else:
                    logging.info("data参数存在但data为空list")
            else:
                logging.info("无data参数")