import json
import requests
from jsonschema import SchemaError, validate, draft7_format_checker, ValidationError
from Common import getConsoleLogin
from Common.getConsoleLogin import getConsoleLogin_token
from Common.get_time_stamp import get_time_stamp13
from TestAssertions.test_assertions_Recommendedstcokdata.test_recommend_addschem import addresultschema
from glo import console_JSON, http


class Testupdate():
    def test_recommend_update(self):
        url = http + ":1216/api/con_stock_recommend/v1/update"

        payload1 = {
            "ts": "HK",
            "code": "00700",
            "type": 2,
            "id": "224",
            "name": "腾讯控股",
            "operationType": 1,
            "recommendedTime": get_time_stamp13(),
            "recommendedPrice": "612.000",
            "referrerReason": "[{\"type\":\"消息面\",\""
                              "list\":[{\"title\":\"市场机会\",\"desc\":\"adsfdasfagdsagag\"}]}]"
        }

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
            assert r.get("msg") == "ok"
        elif r.get("code") == "000200":
            assert r.get("msg") == "数据不存在，操作失败"
        else:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{r}"
            )
            # assert r.get("data") != False

        # assert response.status_code == 200
        # schema = r
        # try:
        #     validate(instance=addresultschema, schema=schema, format_checker=draft7_format_checker)
        # except SchemaError as e:
        #     return 1, f"验证模式schema出错：\n出错位置：{'--> '.join([i for i in e.path])}\n提示信息：{e.message}"
        # except ValidationError as e:
        #     return 1, f"json数据不符合schema规定：\n出错字段：{'-->'.join([i for i in e.path])}\n提示信息：{e.message}"
        # else:
        #     return 0, "success!"
