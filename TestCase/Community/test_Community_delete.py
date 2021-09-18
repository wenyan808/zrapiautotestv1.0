# test_Community_delete
import json
import time

import allure
import pytest

from Common.login import login
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_yaml import yamltoken
from glo import HTTP, JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区-删帖')
class TestCommunitydelete():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()  # 调用登录接口通过token传出来

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    def test_Community_delete(self):
        # login()  # 调用登录接口通过token传出来
        url = HTTP + "/as_community/api/post/v1/add"
        headers = {}
        headers.update(JSON)

        # 拼装参数
        paylo = {
            "articleType": 1,
            "content": "虽然酷寒难当，但经过数千万年暴风雪的磨炼后，终能抵达理想家园"
                       "[tag:00700.HK][tag:600519.SH][img:community/images/2020/12/03/16069737543880963.jpeg]",
            "images": [{
                "name": "community/images/2020/12/03/16069737543880963.jpeg",
                "w": 447,
                "h": 583,
                "url": "http://zhuorui-public.oss-cn-shenzhen.aliyuncs.com/community/images/2020/12/03/16069737543880963.jpeg"
            }],
            "products": [
                {
                    "ts": "Hk",
                    "code": "00700",
                    "name": "腾讯控股",
                    "type": "2"
                },
                {
                    "ts": "SH",
                    "code": "600519",
                    "name": "贵州茅台",
                    "type": "2"
                }
            ]
        }
        # print(paylo)
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        # print(token)
        # print(type(token))

        token1 = yamltoken()
        token = {"token": token1}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        payload = json.dumps(dict(payload1))
        # time.sleep(60.1)

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="发帖(短文)"
        )
        y = r.json()
        # print(y)
        postId = y.get("data").get("postId")
        # print(postId)
        body = {'postId': f"{postId}"}
        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        body1 = {}
        body1.update(body)
        body1.update(sign1)
        # print(body1)
        delete_url = HTTP + "/as_community/api/post/v1/delete"

        r = Requests(self.session).post(
            url=delete_url, headers=headers, json=body1, title="删帖"
        )
        j = r.json()
        # print(j)
        # 断言
        assert r.status_code ==200
        assert j.get("code") == "000000"
        assert j.get("msg") == "ok"
