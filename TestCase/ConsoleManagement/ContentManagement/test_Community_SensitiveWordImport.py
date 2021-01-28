# test_Community_SensitiveWordImport
import json

import allure
import pytest

from Common.getConsoleLogin import getConsoleLogin_token

from Common.requests_library import Requests

from glo import console_JSON, console_HTTP, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('社区console_敏感词导入')
class TestCommunitySensitiveWordImport():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_Community_SensitiveWordImport(self):
        # url = "http://192.168.1.161:1230"
        url_Import = console_HTTP + "/api/con_sensitive_word/v1/import"
        header = console_JSON
        headers = {}
        headers.update(header)
        token = {"token": getConsoleLogin_token()}
        headers.update(token)  # 将token更新到headers
        # print(headers)
        payload = {
            "types": [1, 2],
            "url": "sensitive_word/2021/01/28/16117975807675666.xlsx"
        }

        r_Import = Requests(self.session).post(
            url=url_Import, headers=headers, json=payload, title="敏感词导入"
        )
        j_Import = r_Import.json()
        # print(j_Import)
        if j_Import.get("code") == "000000":
            assert j_Import.get("code") == "000000"
            assert j_Import.get("msg") == "ok"

        elif j_Import.get("code") == "460401":
            assert j_Import.get("code") == "460401"
            assert j_Import.get("msg") == "总量已超过敏感词上限200词，导入失败"

        else:
            raise AssertionError(j_Import)
