import json
import random
import requests
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError
from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import getTimeTostamp
from Common.show_sql import showsql
from TestAssertions.test_assertions_Recommendedstcokdata.test_recommend_addschem import addresultschema
from glo import console_JSON, http

class Testhotstockadd():
    def test_hotstockadd(self):
        url = http+":1216/api/con_hot_search_stocks/v1/add"

        ts_code = showsql(
            "192.168.1.237", "root", "123456", "stock_market",
            "select ts,code from t_stock_search where ts='HK' or ts='SH' or ts='SZ';"
        )
        random_stock = random.sample(ts_code, 1)
        ts_code_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_stock))

        tsCode = ts_code_data[0].get("code")+"."+ts_code_data[0].get("ts")

        payload1 = {"tsCode": tsCode,
                   "recommendTime": getTimeTostamp(1)}

        payload = json.dumps(dict(payload1))

        head = {}
        head.update(console_JSON)
        token1 = {"token": getConsoleLogin_token()}
        head.update(token1)
        headers = head

        response = requests.request("POST", url, headers=headers, data=payload)
        r = response.json()
        # print(r)

        assert response.status_code == 200
        if r.get("code") == "000000":
            assert "msg" == "ok"
            assert "data" == True
        else:
            raise AssertionError(r)

        schema = r
        try:
            validate(instance=addresultschema, schema=schema, format_checker=draft7_format_checker)
        except SchemaError as e:
            return 1, f"验证模式schema出错：\n出错位置：{'--> '.join([i for i in e.path])}\n提示信息：{e.message}"
        except ValidationError as e:
            return 1, f"json数据不符合schema规定：\n出错字段：{'-->'.join([i for i in e.path])}\n提示信息：{e.message}"
        else:
            return 0, "success!"
