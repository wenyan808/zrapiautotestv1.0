import json
import requests as requests
from Common.getTestLoginToken import gettestLoginToken
from Common.get_time_stamp import get_time_stamp13
from Common.sign import get_sign
from glo import http, JSON

class Testrecommendrecent():
    @classmethod
    def setup_class(self):
        self.s = requests.session()

    def tearDown(self):
        self.s.close()

    def test_recomment_recent(self):
        url = http + "/as_recommend/api/stock_recommend/v1/get_recent_recommends"

        payload = {
            "currentPage": 1,
            "home": True,
            "market": 1,
            "pageSize": 10,
            "timeStamp": get_time_stamp13()
        }
        
        sign1 = {"sign": get_sign(payload)}
        payload.update(sign1)

        payload = json.dumps(dict(payload))

        head = {}
        head.update(JSON)
        token1 = {"token": gettestLoginToken()}
        head.update(token1)
        headers = head

        response = self.s.post(
            url=url,
            headers=headers, data=payload
        )

        j = response.json()
        assert response.status_code == 200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
        if "data" in j:
            assert "list" in j.get("data")
            # if len(j.get("data").get("list") != 0:
            #     for i in range(len(j.get("data").get("list"))):
            assert j.get("data").get("yesterday") == True
