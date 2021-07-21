import json
import requests
from Common.getTestLoginToken import gettestLoginToken
from Common.sign import get_sign
from glo import http, JSON

class Testhistorycommend():
    def setup(self):
        self.s = requests.session()

    def teardown(self):
        self.s.close()

    def test_get_history_handcap(self):
        url = http+"/as_recommend/api/stock_recommend/v1/get_home_history"

        payload = {}

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
        assert r.get("code") == "000000"
        assert r.get("msg") == "ok"
        if "data" in r:
            assert "list" in r.get("data")
            # if len(j.get("data").get("list") != 0:
            #     for i in range(len(j.get("data").get("list"))):
        #     assert r.get("data").get("yesterday") == True