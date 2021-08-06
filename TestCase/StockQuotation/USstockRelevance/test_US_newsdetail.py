# test_US_newsdetail
import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login

# @pytest.mark.skip(reason="调试中，返回的结果是404")
@allure.feature('美股相关')
class TestUSNewsdetail:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('个股新闻详情')
    def test_US_newsdetail(self):
        response = zhuorui("Allstock", "个股新闻详情")
        assert_data(response, '000000', 'ok')
        #
        # url = HTTP + "/as_market/api/us/news/v1/detail"
        # headers = {}
        # headers.update(JSON)
        #
        # # 拼装参数
        #
        # paylo = {
        #     "id": 1025985
        # }
        # # paylo = info
        # # print(paylo)
        # sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        # # 调用登录接口通过token传出来
        # payload1 = {}
        # payload1.update(paylo)
        # payload1.update(sign1)
        #
        # # print(token)
        # # print(type(token))
        #
        # token1 = yamltoken()
        # token = {"token": token1}
        # headers.update(token)
        # # print(headers)
        # payload = json.dumps(dict(payload1))
        # # time.sleep(1)
        # r = requests.post(url=url, headers=headers, data=payload)
        # # 断言
        # j = r.json()
        # # print(j)
        # # 通过盘口接口查询昨收价last和diffRate
        # url_last = HTTP + "/as_market/api/handicap/v1/get_handicap"
        # boby = {
        #     "stockList": [
        #         {
        #             "ts": "US",
        #             "code": "TSLA",
        #             "type": "2"
        #         }
        #     ]
        # }
        # sign1 = {"sign": get_sign(boby)}  # 把参数签名后通过sign1传出来
        # # 调用登录接口通过token传出来
        # boby1 = {}
        # boby1.update(boby)
        # boby1.update(sign1)
        # boby = json.dumps(dict(boby1))
        # r = requests.post(url=url_last, headers=headers, data=boby)
        # y=r.json()
        # # print(y)
        # assert r.status_code == 200
        # assert j.get("code") == "000000"
        # assert j.get("msg") == "ok"
        # if "data" in j:
        #     if len(j.get("data")) != 0:
        #         assert "content" in j.get("data")
        #         assert "title" in j.get("data")
        #         assert "pubTime" in j.get("data")
        #         assert "source" in j.get("data")
        #         assert "relateStock" in j.get("data")
        #         assert j.get("data").get("relateStock")[0].get("ts") == "US"
        #         assert j.get("data").get("relateStock")[0].get("code") == "TSLA"
        #         assert j.get("data").get("relateStock")[0].get("name") == "特斯拉"
        #         assert "last" in j.get("data").get("relateStock")[0]
        #         assert "diffRate" in j.get("data").get("relateStock")[0]
        #         assert j.get("data").get("relateStock")[0].get("last") == y.get("data")[0].get("last")
        #         assert j.get("data").get("relateStock")[0].get("diffRate") == y.get("data")[0].get("diffRate")
        #         assert j.get("data").get("relateStock")[0].get("type") == 2
        #         # print(j.get("data"))
        #
        #     else:
        #         logging.info("data是空的集合")
        #
        # else:
        #     logging.info("无data数据")
