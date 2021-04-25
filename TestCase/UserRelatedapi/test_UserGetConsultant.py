# test_UserGetConsultant
import json

import allure
import pytest

from Common.login import login
from Common.sign import get_sign

from Common.requests_library import Requests

from Common.tools.read_yaml import yamltoken

from glo import JSON, HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('用户相关接口-用户获取专属顾问')
class TestUserGetConsultant():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_UserGetConsultant(self):
        # 拼装参数
        header = JSON
        headers = {}
        headers.update(header)
        token = {"token": yamltoken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)

        url1 = HTTP + "/as_user/api/consultant/v1/get_by_user_id"
        paylo = {}
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url1, headers=headers, data=payload, title="用户获取专属顾问"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("msg") == "ok"
            if "data" in j:

                assert j.get("data").get("name") == '孙晓美'
                assert j.get("data").get("wxNum") == '13302434483'
                assert j.get("data").get("qqNum") == '1703164097'
                assert j.get("data").get("headPhoto") == \
                       'http://watch-cloud-source.oss-cn-shenzhen.aliyuncs.com' \
                       '/image/2019-01-30/287-385-max.png'
                assert j.get("data").get("serviceTime") == '工作日9:00-20:00'
                assert j.get("data").get("position") == '高级顾问'





        else:
            raise ValueError(f"{j}")
