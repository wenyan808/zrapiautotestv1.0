import json
from TestAssertions.test_assertions_Recommendedstcokdata.test_recommend_addschem import addresultschema
import requests
from Common.get_time_stamp import get_time_stamp13
from Common.sign import get_sign
from glo import JSON, HTTP, JSON1
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

class Testhotstockget():

    def test_hotstock_get(self):
        url = HTTP+"/as_recommend/api/hot_stocks/v1/get"
        # print(url)

        paylo = {"timeStamp": get_time_stamp13()}
        sign1 = {"sign": get_sign(paylo)}
        paylo.update(sign1)
        payload = json.dumps(dict(paylo))

        headers = JSON1

        response = requests.request("POST", url, headers=headers, data=payload)
        r = response.json()

        assert response.status_code == 200
        if r.get("code") == "000000":
            assert r.get("msg") == "ok"
            assert r.get("data") != None
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