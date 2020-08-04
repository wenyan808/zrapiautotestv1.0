import allure

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import OperationSql, MongoDB
from Common.tools.write_xlsx import write_xlsx


@allure.feature('选股器')
class TestStockSelectionDevicePut:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('保存策略_1-中国香港')
    def test_StockSelectionDevice_put01(self):
        response = zhuorui('选股器', '保存策略_1-中国香港')
        if response.json().get("code") == "000000":
            assert_data(response, '000000', 'ok')
        elif response.json().get("code") == "450001":
            assert_data(response, '450001', '策略名称已存在')
        assert response.status_code == 200
        # print(response.json())
        # q = OperationSql("192.168.1.236", "root", "123456", "t_tactic6")
        # Id = str(q.show_sql("select _id from t_user_account where `user_id`= '68904140';"))
        # id = MongoDB("Id", Id[2:-3:])
        # # print(id)
        # # print(id[-1].get('_id'))
        # self._id = {"id": str(id[-1].get('_id'))}
        # write_xlsx("选股器", 21, 7, str(self._id))

    @allure.story('保存策略_2-美国')
    def test_StockSelectionDevice_put02(self):
        response = zhuorui('选股器', '保存策略_2-美国')
        if response.json().get("code") == "000000":
            assert_data(response, '000000', 'ok')
        elif response.json().get("code") == "450001":
            assert_data(response, '450001', '策略名称已存在')
        assert response.status_code == 200
        # print(response.json())

    @allure.story('保存策略_3-中国')
    def test_StockSelectionDevice_put03(self):
        response = zhuorui('选股器', '保存策略_3-中国')
        if response.json().get("code") == "000000":
            assert_data(response, '000000', 'ok')
        elif response.json().get("code") == "450001":
            assert_data(response, '450001', '策略名称已存在')
        assert response.status_code == 200
        # print(response.json())

    # @allure.story('保存策略')
    # def test_StockSelectionDevice_put01(self):
    #     response = zhuorui('选股器', '保存策略')
    #     assert_data(response, '000000', 'ok')
    #     assert response.status_code == 200
    #     # print(response.json())
