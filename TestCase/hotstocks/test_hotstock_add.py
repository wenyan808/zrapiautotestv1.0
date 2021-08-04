import json
import random
import requests
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.assertapi import jsonschema_assert
from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import getTimeTostamp
from Common.show_sql import showsql
from TestAssertions.test_assertions_Recommendedstcokdata.test_recommend_addschem import addresultschema
from TestCase.Recommendedstockconsole.test_recommend_adddel import get_market_status
from glo import console_JSON, http

class Testhotstockadd():
    def test_hotstockadd(self):
        url = http+":1216/api/con_hot_search_stocks/v1/add"

        ts_code = showsql(
            "192.168.1.237", "root", "123456", "stock_market",
            "select ts,code from t_stock_search where ts!='US' and suspension = 1 ;"
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
        if get_market_status(1) != 8:
            response = requests.request("POST", url, headers=headers, data=payload)
            r = response.json()
            # print(r)
    
            assert response.status_code == 200
            try:
                jsonschema_assert(r.get("code"), r.get("msg"), r, addresultschema)
                assert r.get("data") == True
            except:
                raise AssertionError(
                    f"\n请求地址：{url}"
                    f"\nbody参数：{payload}"
                    f"\n请求头部参数：{headers}"
                    f"\n返回数据结果：{r}"
                )

            # schema = r
            # try:
            #     validate(instance=addresultschema, schema=schema, format_checker=draft7_format_checker)
            # except SchemaError as e:
            #     return 1, f"验证模式schema出错：\n出错位置：{'--> '.join([i for i in e.path])}\n提示信息：{e.message}"
            # except ValidationError as e:
            #     return 1, f"json数据不符合schema规定：\n出错字段：{'-->'.join([i for i in e.path])}\n提示信息：{e.message}"
            # else:
            #     return 0, "success!"
