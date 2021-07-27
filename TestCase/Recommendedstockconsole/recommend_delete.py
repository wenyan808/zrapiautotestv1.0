"""
@File  ：test_recommend_adddel.py
@Author: renfei
@Time  : 2021/7/26
@Desc  : 新增荐股
@last  : 最后一次修改 chenjialuo 2021/7/27
"""

import json
import requests
from jsonschema import SchemaError, validate, draft7_format_checker, ValidationError
from Common.getConsoleLogin import getConsoleLogin_token
from TestAssertions.test_assertions_Recommendedstcokdata.test_recommend_addschem import addresultschema
from glo import console_JSON, http

# 删除荐股的方法
def delete1(i,token):
    # 获取id,ts,code
    id,ts,code = recommend_getlist(i,token)
    url = http+":1216/api/con_stock_recommend/v1/delete"

    payload1 = {
            "id": id,
            "ts": ts,
            "code": code
}
    payload = json.dumps(dict(payload1))

    head = {}
    head.update(console_JSON)
    token1 = {"token": token}
    head.update(token1)
    headers = head

    response = requests.request("POST", url, headers=headers, data=payload)

    r = response.json()
    # print(r)

    assert response.status_code == 200
    if r.get("code") == "000000":
        assert r.get("msg") == "ok"
        assert r.get("data") == True
    elif r.get("code") == "000200":
        assert r.get("msg") == "数据不存在，操作失败"
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


# 获取荐股列表
def recommend_getlist(i,token):
    url = http+":1216/api/con_stock_recommend/v1/get_list"
    # 传参 id sort currentPage pageSize
    payload1 = {
        "id": 363,
        "sort": "1",
        "currentPage": 1,
        "pageSize": 20
    }

    payload = json.dumps(dict(payload1))

    head = {}
    head.update(console_JSON)
    token1 = {"token": token}
    head.update(token1)
    headers = head

    response = requests.request("POST", url, headers=headers, data=payload)
    # get到荐股列表的下标
    r = response.json().get("data").get("list")[i]

    return r.get("id"),r.get("ts"),r.get("code")
