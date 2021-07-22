# 查询推荐理由
import json
import requests as requests
from Common.getTestLoginToken import gettestLoginToken
from Common.get_time_stamp import get_time_stamp13
from Common.sign import get_sign
from glo import http, JSON

class Testreasoncommend():
    def setup(self):
        self.s=requests.session()
    def teardowm(self):
        self.s.close()
    def test_commend_reason(self):
        url = http+"/as_recommend/api/stock_recommend/v1/get_recommend_reasons"

        payload = {
            "id": "151",
            "key": "none",
            "timeStamp": get_time_stamp13()
        }
        sign1 = {"sign": get_sign(payload)}
        payload.update(sign1)
        payload = json.dumps(dict(payload))

        header = {}
        header.update(JSON)
        token1 = {"token": gettestLoginToken()}
        header.update(token1)
        headers = header

        response = requests.request("POST", url, headers=headers, data=payload)
        r = response.json()
        # print(r)

        assert response.status_code == 200
        try:
            assert r.get("code") == "000000"
            assert r.get("msg") == "ok"
            if "data" in r:
                for i in range(len(r.get("data"))):
                    assert "type" in r.get("data")[i]
                    for j in range(len(r.get("data")[i].get("list"))):
                        assert "title" in r.get("data")[i].get("list")[j]
                        assert "desc" in r.get("data")[i].get("list")[j]
        except:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{r}"
            )

