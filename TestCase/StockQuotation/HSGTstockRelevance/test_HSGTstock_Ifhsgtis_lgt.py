import json

import allure
import pytest

from Common.login import login
from Common.requests_library import Requests
from Common.show_sql import OperationSql
from Common.sign import get_sign
from Common.tools.read_write_json import get_json, write_json
from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


# test_HSGTstock_Ifhsgtis_lgt

@pytest.mark.skip(reason="tiaoshizhong ")
@allure.feature('陆股通')
class testHSGTstockIfhsgtis_lgt:
    @classmethod
    def setup_class(cls) -> None:
        login()
        q = OperationSql("192.168.1.237", "root", "123456", "stock_market")
        ts_code = q.show_sql("select ts,code from t_stock_search where ts='SH' or ts='SZ';")
        ts_code_shuju = json.dumps(list(map(lambda code: {"ts": code[0], "code": code[1]}, ts_code)))
        # write_json(r"TestData/hsgtis_lgt.json", ts_code_shuju)
        with open(r"TestData/hsgtis_lgt.json", "w", encoding="utf-8") as f:
            json.dump(ts_code_shuju, f, indent=2, ensure_ascii=False)

    # @allure.story('判断股票是否是陆股通')
    # @pytest.mark.parametrize("_data", get_json(BASE_DIR + r"/TestData/hsgtis_lgt.json"))
    # def test_HSGTstock_Ifhsgtis_lgt(self, _data):
    #     url = HTTP + "/api/stock_market_data/v1/hsgt/is_lgt"
    #     headers = JSON
    #
    #     # 拼装参数
    #
    #     paylo = _data
    #     # print(paylo)
    #     sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    #     # 调用登录接口通过token传出来
    #     payload1 = {}
    #     payload1.update(paylo)
    #     payload1.update(sign1)
    #     headers = headers
    #     # print(token)
    #     # print(type(token))
    #
    #     token1 = yamltoken()
    #     token = {"token": token1}
    #     headers.update(token)
    #     # print(headers)
    #     payload = json.dumps(dict(payload1))
    #
    #     r = Requests(self.session).post(
    #         url=url, headers=headers, data=payload, title="判断股票是否是陆股通"
    #     )
    #     # 断言
    #     j = r.json()
    #     # print(j)
    #
    #     assert r.status_code == 200
    #     assert j.get("code") == "000000"
    #     assert j.get("msg") == "ok"
    #     # print(j)
    #     if "data" in j:
    #         if len(j.get("data")) != 0:
    #             if j.get("data").get("luStockConnect") == True:
    #                 print("是陆股通")
    #             else:
    #                 print("不是陆股通")
