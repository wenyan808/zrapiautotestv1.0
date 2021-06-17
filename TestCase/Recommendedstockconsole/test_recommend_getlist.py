import json
import requests
from jsonschema import SchemaError, validate, draft7_format_checker, ValidationError
from Common import getConsoleLogin
from Common.getConsoleLogin import getConsoleLogin_token
from TestAssertions.test_assertions_Recommendedstcokdata.test_recommend_addschem import addresultschema
from glo import console_JSON, http

class Testgetlist():
    def test_recommend_getlist(self):
        url = http+":1216/api/con_stock_recommend/v1/get_list"

        payload1 = {
            "id": 360,
            "sort": "1",
            "currentPage": 1,
            "pageSize": 20
        }

        payload = json.dumps(dict(payload1))

        head = {}
        head.update(console_JSON)
        token1 = {"token": getConsoleLogin_token()}
        head.update(token1)
        headers = head

        response = requests.request("POST", url, headers=headers, data=payload)

        r = response.json()
        print(r)

        assert response.status_code == 200
        if r.get("code") == "000000":
            assert r.get("msg") == "ok"
        else:
                raise AssertionError(r)

        assert response.status_code == 200
        schema = r
        try:
            validate(instance=addresultschema, schema=schema, format_checker=draft7_format_checker)
        except SchemaError as e:
            return 1, f"验证模式schema出错：\n出错位置：{'--> '.join([i for i in e.path])}\n提示信息：{e.message}"
        except ValidationError as e:
            return 1, f"json数据不符合schema规定：\n出错字段：{'-->'.join([i for i in e.path])}\n提示信息：{e.message}"
        else:
            return 0, "success!"
