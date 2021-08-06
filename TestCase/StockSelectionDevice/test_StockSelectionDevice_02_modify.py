import allure
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import MongoDB, showsql
from Common.tools.unique_text import get_unique_username
from Common.tools.write_xlsx import write_xlsx

# @pytest.mark.skip(reason="状态显示未完成，目前无法运行")
@allure.feature('选股器')
class TestStockSelectionDeviceModify:
    @classmethod
    def setup_class(cls) -> None:
        login()
        # 通过传入数据库的IP地址address，用户名user，密码password，数据库名database连接到后台数据库
        userId = showsql(
            '192.168.1.237', 'root', '123456', "user_account",
            "select user_id from t_user_account where `zr_no`= '68904140';"
        )
        # 通过查询语句找到用户id
        # print(userId)
        # 传入键key，值price，数据库名database，表名surface到MongoDB数据库
        id = MongoDB("192.168.1.236", 27017, "stock_selector", "t_tactic6","user_id", str(userId)[3:-5:])
        # print(str(userId)[3:-5:])
        _id = str(id[-1].get('_id'))
        paylo = {
            "name": f"{get_unique_username(1)[0]}",
            "market": {
                "region": 1,
                "industryCode": "00700",
                "industryName": "HK"
            },
            "id": f"{_id}"
        }
        write_xlsx("Allstock", 48, 7, str(paylo))
    @allure.story('修改策略_1-中国香港')
    def test_StockSelectionDevice_modify01(self):
        response = zhuorui('Allstock', '修改策略_1-中国香港')
        assert_data(response, '000000', 'ok')


        # self._id = {"id": str(id[:-1].get('_id'))}
        # print(self._id)
        # # 写
        # write_xlsx("选股器", 21, 7, str(self._id))
        #
        # response = zhuorui('选股器', '修改策略_1-中国香港')
        # if response.json().get("code") == "000000":
        #     assert_data(response, '000000', 'ok')
        # elif response.json().get("code") == "450001":
        #     assert_data(response, '450001', '策略名称已存在')
        # elif response.json().get("code") == "450002":
        #     assert_data(response, '450002', '操作失败')
        # assert response.status_code == 200
        # # print(response.json())
