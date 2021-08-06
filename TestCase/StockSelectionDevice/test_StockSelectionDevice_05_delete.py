import json
import allure
import requests

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import MongoDB, showsql
from Common.sign import get_sign
from Common.tools.read_write_yaml import yamltoken
from Common.tools.write_xlsx import write_xlsx
from glo import JSON, HTTP


# @pytest.mark.skip(reason="状态显示未完成，目前无法运行")
@allure.feature('选股器')
class TestStockSelectionDeviceDelete:
    @classmethod
    def setup_class(cls) -> None:
        login()
      # 通过传入数据库的IP地址address，用户名user，密码password，
        userId = showsql(
            '192.168.1.237', 'root', '123456', "user_account",
            "select user_id from t_user_account where `zr_no`= '68904140';"
        )
        # 通过查询语句找到用户id
        # 传入键key，值price，数据库名database，表名surface到MongoDB数据库
        id = MongoDB("192.168.1.236", 27017, "stock_selector", "t_tactic6", "user_id", str(userId)[3:-5:])
        # print(str(userId)[3:-5:])
        _id = str(id[-1].get('_id'))
        paylo = {
            "region": 1,
            "tacticId": f"{_id}"
        }
        write_xlsx("Allstock", 51, 7, str(paylo))
    @allure.story('删除策略_1-中国香港')
    def test_StockSelectionDevice_delete01(self):
        response = zhuorui('Allstock', '删除策略_1-中国香港')
        assert_data(response, '000000', 'ok')