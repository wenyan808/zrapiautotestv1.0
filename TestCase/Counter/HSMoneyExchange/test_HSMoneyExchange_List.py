# test_HSMoneyExchange_List   兑换记录     /as_trade/api/money_exchange/v1/list
import json

import allure
from jsonschema import validate, draft7_format_checker, SchemaError, ValidationError

from Common.Accountcommon.accountAuth import AccountAuth
from Common.get_time_stamp import TimeTostamp, get_time_stamp13

from Common.sign import get_sign

from Common.requests_library import Requests


from TestAssertions.CounterJsonSchemadata.HSMoneyExchange.ListSchema import ListSchema


# @pytest.mark.skip(reason="调试中 ")
@allure.feature('柜台app_恒生3.0 货币兑换—兑换记录')
class TestHSMoneyExchangeList():
    @classmethod
    def setup_class(cls) -> None:
        cls.session = Requests().get_session()

    def tearDown(self) -> None:
        Requests(self.session).close_session()

    # @pytest.mark.skip(reason="调试中 ")
    def test_HSMoneyExchange_List(self):
        http = list(AccountAuth())[-1]
        url = http + "/as_trade/api/money_exchange/v1/list"

        # 拼装参数
        headers = list(AccountAuth())[1]  # 将柜台token赋值到headers
        # print(headers)
        moneyType = "HKD"  # 源币种类别:HKD,USD,CNY
        toMoneyType = "CNY"  # 目标币种类别:HKD,USD,CNY
        createStartTime = TimeTostamp()  # 开始时间(时间戳)
        createEndTime = get_time_stamp13()  # 截止时间(时间戳)
        status = 1  # 1、待审核（处理中） 2、已通过 3、已驳回
        body = {
            "moneyType": moneyType,
            "toMoneyType": toMoneyType,
            "createStartTime": createStartTime,
            "createEndTime": createEndTime,
            "status": status
        }

        sign1 = {"sign": get_sign(body)}  # 把参数签名后通过sign1传出来
        payload1 = {}
        payload1.update(body)
        payload1.update(sign1)

        payload = json.dumps(dict(payload1))

        r = Requests(self.session).post(
            url=url, headers=headers, data=payload, title="兑换记录"
        )

        j = r.json()
        # print(j)
        assert r.status_code == 200
        if j.get("code") == "000000":
            assert j.get("code") == "000000"
            assert j.get("msg") == "ok"
            schema = j
            try:
                validate(instance=ListSchema, schema=schema, format_checker=draft7_format_checker)
            except SchemaError as e:
                return 1, f"验证模式schema出错：\n出错位置：{'--> '.join([i for i in e.path])}\n提示信息：{e.message}"
            except ValidationError as e:
                return 1, f"json数据不符合schema规定：\n出错字段：{'-->'.join([i for i in e.path])}\n提示信息：{e.message}"
            else:
                return 0, "success!"
        else:
            raise AssertionError(j)
