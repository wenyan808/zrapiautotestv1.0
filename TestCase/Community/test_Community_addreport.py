# test_Community_addreport
import json
import random

import allure
import pytest

from Common.get_time_stamp import get_time_stamp13
from Common.login import login
from Common.show_sql import MongoDBField, showsql
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import write_json
from Common.tools.read_yaml import yamltoken
from glo import HTTP, JSON, BASE_DIR


@pytest.mark.skip(reason="调试中 ")
@allure.feature('社区_举报')
class TestCommunityaddreport():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()  # 调用登录接口通过token传出来
        # # 传入键key，值price，数据库名database，表名surface到MongoDB数据库
        # _paylo = MongoDBField("192.168.1.237", 27017, "community", "t_report", [{}, {"type": 1}])
        # print(_paylo)
        # # paylo = []
        # # for i in range(len(_paylo)):
        # #     _id = _paylo[i].get("_id")
        # #     _id = re.search("[^ObjectId]",_id.text)
        # #     type = _paylo[i].get("type")
        # #     paylo1 = {"_id": _id, "type": type}
        # #     paylo.append(paylo1)
        # # print(paylo)
        #
        # # print(MongoDBField("192.168.1.237", 27017, "community", "t_report", [{}, {"type": 1}]))
        # # random_paylo = random.sample(_paylo, 50)
        # # paylo_data = list(map(lambda code: {"ts": code[0], "code": code[1]}, random_paylo))
        # # write_json(BASE_DIR + r"/TestData/Communityaddreport.json", paylo)


    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_addreport(self):
        # login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/report/v1/add"
        headers = JSON
        # userId = showsql(
        #     '192.168.1.237', 'root', '123456', "user_account",
        #     "select user_id from t_user_account where `zr_no`= '68904140';"
        # )
        # print(userId[3:-5:])
        # 拼装参数
        # paylo = {
        #
        #     "reportedId": "5fb22c84791d040006a931fd",
        #     "type": 2,
        #     "reportedType": 3
        #
        # }
        paylo = {

            "reportedId": "5fe2b0b1791d040006ec7ed1",
            "type": 2
        }
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        headers = headers
        # print(token)
        # print(type(token))
        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        payload = json.dumps(dict(payload1))
        # time.sleep(60.01)

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="举报"
        )
        y = r.json()
        # print(y)
        # 断言
        assert r.status_code == 200
        if y.get("code") == "000000":
            assert y.get("code") == "000000"
            assert y.get("msg") == "ok"
        else:
            assert y.get("code") == "460600"
            assert y.get("msg") == "举报已提交"