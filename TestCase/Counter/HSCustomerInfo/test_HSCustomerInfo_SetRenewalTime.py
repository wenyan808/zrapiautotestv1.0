# test_HSCustomerInfo_SetRenewalTime       用户设置证券账号断线续约时长       /as_trade/api/account/v1/set_renewal_time
import json

import allure
import pytest
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.get_time_stamp import get_time_stamp13
from Common.getTestLoginToken import gettestLoginToken
from Common.sign import get_sign

from Common.requests_library import Requests
from Common.tools.read_write_json import get_json
from TestAssertions.CounterJsonSchemadata.HSCustomerInfo.SetRenewalTimeSchema import SetRenewalTimeSchema

from glo import http, JSON_dev, BASE_DIR


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_用户设置证券账号断线续约时长')
class TestHSCustomerInfoSetRenewalTime():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    @pytest.mark.parametrize('info',
                             get_json(BASE_DIR +
                                      r"/TestData/Counterdata/HSCustomerInfodata/"
                                      r"test_HSCustomerInfo_SetRenewalTimedata.json"))
    def test_HSCustomerInfo_SetRenewalTime(self, info):
        url = http + "/as_trade/api/account/v1/set_renewal_time"
        renewalTime = info.get("renewalTime")  # 续约时长，已分钟为单位 0，15，30，60，180
        timeStamp = get_time_stamp13()  # 获取当前时间戳
        # 拼装参数
        headers = JSON_dev
        headers = headers
        headers1 = {}
        token = {"token": gettestLoginToken()}
        headers1.update(headers)
        headers1.update(token)  # 将token更新到headers
        # print(headers)

        body = {
            "renewalTime": renewalTime,
            "timeStamp": timeStamp
        }

        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(body)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers1, data=payload, title="用户设置证券账号断线续约时长"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            assert j.get("data") == True

            schema = j
            try:
                validate(instance=SetRenewalTimeSchema, schema=schema, format_checker=draft7_format_checker)
            except SchemaError as e:
                return 1, f"验证模式schema出错：\n出错位置：{'--> '.join([i for i in e.path])}\n提示信息：{e.message}"
            except ValidationError as e:
                return 1, f"json数据不符合schema规定：\n出错字段：{'-->'.join([i for i in e.path])}\n提示信息：{e.message}"
            else:
                return 0, "success!"
        else:
            raise AssertionError(j)
