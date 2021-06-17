# test_EM_UserGroupImport   用户组导入   /api/con_user_group/v1/import

import json

import allure

import pytest

from Common.OSS import oss_file
from Common.getConsoleLogin import getConsoleLogin_token
from Common.sign import get_sign

from Common.requests_library import Requests

from Common.tools.read_write_json import get_json

from glo import BASE_DIR, console_HTTP, console_JSON


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_持仓偏好')
class TestEMUserGroupImport():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(
                                 BASE_DIR + r"/TestData/test_EventManagementdata/test_EM_UserGroupImport.json"))
    def test_EM_UserGroupImport(self, info):
        url = console_HTTP + "/api/con_user_group/v1/import"
        url1 = console_HTTP + "/api/con_sts/v1/token"
        header = console_JSON
        header = header

        headers = {}
        headers.update(header)

        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        checkColumn = info.get("checkColumn")
        uploads = "user_group"
        groupName = group_name = info.get("groupName")
        catalog = "/Business/Img/"
        url2 = list(oss_file(uploads, group_name, catalog, url1, headers))[-1]

        paylo = {
            "url": url2,
            "checkColumn": checkColumn,
            "groupName": groupName,
        }
        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)
        payload = json.dumps(dict(payload1))

        r_import  = Requests(self.session).post(
                url=url, headers=headers, data=payload, title="持仓偏好"
            )
        j = r_import.json()
        # print(j)
        assert r_import.status_code == 200

        assert j.get("code") == "000000"
        assert j.get("msg") == 'ok'
        assert len(j.get("data")) != 0
        assert j.get("data").get("duplicate") == 0
        assert "url" in j.get("data")
        assert "http://zhuorui-public-test.oss-cn-shenzhen.aliyuncs.com/user_group/invalid/" in j.get("data").get("url")
        assert "total" in j.get("data")
        assert j.get("data").get("total") == 19
        assert "groupId" in j.get("data")


