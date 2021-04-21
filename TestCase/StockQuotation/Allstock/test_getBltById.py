# test_getBltById
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


@pytest.mark.skip(reason="调试中")
@allure.feature('公共分类')
class TestGetBltById:
    @classmethod
    def setup_class(cls) -> None:
        login()
        ts_code = showsql(
            '192.168.1.237', 'root', '123456', 'stock_market',
            "select ts,code,name from t_stock_search;"
        )
        random_stock = random.sample(ts_code, 10)
        stock_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))
        write_json(BASE_DIR + r"/TestData/AllStockData/test_getBltById.json", stock_data)

    @allure.story('公告获得公告列表分页')
    @pytest.mark.parametrize('info', get_json(BASE_DIR + r"/TestData/AllStockData/test_getBltById.json"))
    def test_getBltById(self, info):
        # pass
        url = HTTP + "/as_market/api/announcement/v1/get_blt_by_id"
        headers = JSON

        # 拼装参数
        paylo = {
            "ts": info.get("ts"),
            "code": info.get("code"),
            "currentPage": 1,
            "pageSize": 15
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
                    assert "total" in j.get("data")
                    assert "currentPage" in j.get("data")
                    assert "pageSize" in j.get("data")
                    if len(j.get("data").get("list")) != 0:
                        for i in range(len(j.get("data").get("list"))):
                            assert "lineId" in j.get("data").get("list")[i]
                            assert "title" in j.get("data").get("list")[i]
                            assert "pubDate" in j.get("data").get("list")[i]
                            assert "url" in j.get("data").get("list")[i]
                            print(j.get("data").get("list")[i].get("url"))
                            assert j.get("data").get("list")[i].get("url") == \
                                   f"http://192.168.1.239:8080/zhuorui_h5/noticeDetail" \
                                   + f"?lineId={j.get('data').get('list')[i].get('lineId')}" \
                                     f"&ts={paylo.get('ts')}&code={info.get('code')}"

                    else:
                        logging.info(print(j.get("data").get("list")))
                else:
                    logging.info("data参数存在但data为空list")

            else:
                logging.info("无data参数")
