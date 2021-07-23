# test_HSIPO_Pur       IPO申购          /as_trade/api/ipo/v1/pur
import json

import allure
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.Accountcommon.accountAuth import AccountAuth
from Common.assertapi import assert_data, jsonschema_assert

from Common.sign import get_sign

from Common.requests_library import Requests

# @pytest.mark.skip(reason="调试中 ")
from TestAssertions.CounterJsonSchemadata.HSIPORelevantSchema.PurRecordDetailSchema import PurRecordDetailSchema
from TestAssertions.CounterJsonSchemadata.HSIPORelevantSchema.PurSchema import PurSchema


@allure.feature('柜台app_申购')
class TestHSIPOGearList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()
        cls.http = list(AccountAuth())[-1]
        cls.url = cls.http + "/as_trade/api/ipo/v1/gear_list"
        cls.url1 = cls.http + "/as_trade/api/ipo/v1/subscribe_list"
        cls.url2 = cls.http + "/as_trade/api/ipo/v1/pur"

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

            getinfo = Requests(self.session).post(
                url=self.url, headers=headers, data=payload, title="获取新股档位信息"
            )

            j = getinfo.json()
            # print(j)
            if "data" in j:
                applyQty = j.get("data")[0].get("applyQty")  # 申购数量
                actionIn = 1  # 1：申购，3：撤销申购
                payloa = {

                    "ts": ts,
                    "code": code,
                    "applyQty": applyQty,
                    "actionIn": actionIn

                }
                sign1 = {"sign": get_sign(payloa)}  # 把参数签名后通过sign1传出来
                payload2 = {}
                payload2.update(payloa)
                payload2.update(sign1)

                payload3 = json.dumps(dict(payload2))
                r = Requests(self.session).post(
                    url=self.url2, headers=headers, data=payload3, title="IPO申购"
                )
                g = r.json()
                # print(g)
                assert r.status_code == 200
                if g.get("code") == "000000":
                    if jsonschema_assert(g.get("code"), g.get("msg"), g, PurSchema) is not (0, "success!"):
                        if len(k.get("data")) != 0:
                            sign2 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
                            body2 = {}
                            body2.update(body)
                            body2.update(sign2)

                            payload3 = json.dumps(dict(body2))

                            getinfo = Requests(self.session).post(
                                url=self.url3, headers=headers, data=payload3, title="IPO申购记录详情"
                            )

                            j = getinfo.json()
                            # print(j)
                            assert getinfo.status_code == 200
                            if j.get("code") == "000000":
                                assert j.get("data").get("ts") == body.get("ts")
                                assert j.get("data").get("data") == body.get("code")
                                jsonschema_assert(j.get("code"), j.get("msg"), j, PurRecordDetailSchema)
                            else:
                                raise AssertionError(j)

                        else:
                            raise AssertionError("data无数据")

                elif g.get("code") == "350604":
                    assert g.get("msg") == "您已申请该新股认购，暂不支持重复认购"
                else:
                    raise AssertionError(g)
                actionIn1 = 3  # 1：申购，3：撤销申购
                payloa1 = {

                    "ts": ts,
                    "code": code,
                    "applyQty": applyQty,
                    "actionIn": actionIn1

                }
                sign1 = {"sign": get_sign(payloa1)}  # 把参数签名后通过sign1传出来
                payload4 = {}
                payload4.update(payloa1)
                payload4.update(sign1)

                payload5 = json.dumps(dict(payload4))
                r1 = Requests(self.session).post(
                    url=self.url2, headers=headers, data=payload5, title="IPO撤销申购"
                )
                h = r1.json()
                # print(h)
                assert r1.status_code == 200
                if h.get("code") == "000000":
                    assert h.get("code") == "000000"
                    assert h.get("msg") == "ok"
                else:
                    raise AssertionError(h)
            else:
                print("当前可认购IPO未配置单位信息")
        else:
            raise AssertionError("当前无可认购IPO")
