# test_HSIPO_PurRecordList      IPO申购记录列表     /as_trade/api/ipo/v1/pur_record_list
import json

import allure
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.Accountcommon.accountAuth import AccountAuth

from Common.sign import get_sign

from Common.requests_library import Requests

from TestAssertions.CounterJsonSchemadata.HSIPORelevantSchema.PurRecordListSchema import PurRecordListSchema


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_IPO申购记录列表')
class TestHSIPOPurRecordList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSIPO_PurRecordList(self):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/ipo/v1/pur_record_list"

        # 拼装参数
        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers
        # print(headers)

        paylo = {}

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="IPO申购记录列表"
        )

        k = r.json()
        # print(k)
        assert r.status_code == 200
        if k.get("code") == "000000":
            assert k.get("code") == "000000"
            assert k.get("msg") == "ok"

            schema = k
            try:
                validate(instance=PurRecordListSchema, schema=schema, format_checker=draft7_format_checker)
            except SchemaError as e:
                return 1, f"验证模式schema出错：\n出错位置：{'--> '.join([i for i in e.path])}\n提示信息：{e.message}"
            except ValidationError as e:
                return 1, f"json数据不符合schema规定：\n出错字段：{'-->'.join([i for i in e.path])}\n提示信息：{e.message}"
            else:
                return 0, "success!"
        else:
            raise AssertionError(k)
