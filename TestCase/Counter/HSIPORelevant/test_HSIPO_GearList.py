# test_HSIPO_GearList   /as_trade/api/ipo/v1/gear_list       获取新股档位信息
import json

import allure
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.Accountcommon.accountAuth import AccountAuth
from Common.assertapi import assert_data, jsonschema_assert

from Common.sign import get_sign

from Common.requests_library import Requests

from TestAssertions.CounterJsonSchemadata.HSIPORelevantSchema.GearListSchema import GearListSchema


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_获取新股档位信息')
class TestHSIPOGearList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.http = list(AccountAuth())[-1]
        cls.url = cls.http + "/as_trade/api/ipo/v1/gear_list"
        cls.url1 = cls.http + "/as_trade/api/ipo/v1/subscribe_list"

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSIPO_GearList(self):


        # 拼装参数
        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers
        # print(headers)

        paylo = {}

        sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(paylo)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r_data = Requests(self.session).post(
            url=self.url1, headers=headers, data=payload, title="IPO可认购列表"
        )

        k = r_data.json()
        # print(k)
        if "data" in k:
            if len(k.get("data")) != 0:
                ts = k.get("data")[0].get("ts")
                code = k.get("data")[0].get("code")

                body = {
                    "ts": ts,
                    "code": code
                }

                sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
                body1 = {}
                body1.update(body)
                body1.update(sign1)

                payload = json.dumps(dict(body1))

                r = Requests(self.session).post(
                    url=self.url, headers=headers, data=payload, title="获取新股档位信息"
                )

                j = r.json()
                # print(j)
                assert r.status_code == 200
                if j.get("code") == "000000":
                    jsonschema_assert(j.get("code"), j.get("msg"), j, GearListSchema)
                else:
                    raise AssertionError(j)
            else:
                print("IPO可认购列表为空")

        else:
            raise AssertionError("data为空")
