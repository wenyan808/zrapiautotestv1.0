# test_FollowList
import json
import logging

import allure
import pytest

from Common.get_time_stamp import get_time_stamp13
from Common.login import login
from Common.show_sql import showsql

from Common.sign import get_sign

from Common.requests_library import Requests

from Common.tools.read_write_yaml import yamltoken

from glo import JSON, HTTP


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('主页信息-我的关注列表')
class TestFollowList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        login()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_FollowList(self):
        # 拼装参数
        header = {}
        header.update(JSON)
        headers = {}
        headers.update(header)
        token = {"token": yamltoken()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        createTime = get_time_stamp13()
        url = HTTP + "/as_user/api/follow/v1/list"
        paylo = {
            "createTime": createTime,
            "pageSize": 20
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="我的关注列表"
        )
        j = r.json()
        # print(j)
        assert r.status_code == 200
        try:
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            if "data" in j:
                userId = showsql(
                    '192.168.1.237', 'root', '123456', "user_account",
                    "select user_id from t_user_account where `zr_no`= '48066661';"
                )

                assert j.get("data")[0].get("userId") == list(list(userId)[0])[0]
                assert j.get("data")[0].get("headPhoto") == \
                       "http://zhuorui-public-test.oss-cn-shenzhen.aliyuncs.com/" \
                       "head_photo/fef4a889f81c4c778afc07b9b15f7e5b/16267765146200448.jpg"

                assert j.get("data")[0].get("nickname") == "卓锐用户48066661"
                assert j.get("data")[0].get("fansCount") == 1
                assert j.get("data")[0].get("createTime") == 1626776457000
                assert j.get("data")[0].get("zrNo") == "48066661"

        except:
            raise AssertionError(
                f"\n请求地址：{url}"
                f"\nbody参数：{payload}"
                f"\n请求头部参数：{headers}"
                f"\n返回数据结果：{j}"
            )
