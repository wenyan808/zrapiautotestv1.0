import allure
import pandas as pd
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import OperationSql, MongoDB
from Common.tools.read_xlsx_exampleshuju import shuju
from Common.tools.write_xlsx import write_xlsx
from glo import BASE_DIR


class TestDelOptionalStock:
    @classmethod
    def setup_class(cls) -> None:
        login()

    @allure.story('删除自选股_根据code_All')
    def test_code_all(self):
        response = zhuorui('自选股', '删除自选股_根据code_All')
        assert_data(response, '000000', 'ok')

    # @allure.story('删除自选股_根据code_type不正确')
    # def test_code_type_error(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_type不正确')

    # @allure.story('删除自选股_根据code_ts不正确')
    # def test_code_ts_error(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_ts不正确')

    # @allure.story('删除自选股_根据code_参数列表为空')
    # def test_coed_parameter_null(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_参数列表为空')

    # @allure.story('删除自选股_根据code_ts异常')
    # def test_code_ts_exception(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_ts异常')

    # @allure.story('删除自选股_根据code_code不正确')
    # def test_code_code_error(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_code不正确')

    # @allure.story('删除自选股_根据code_code异常')
    # def test_code_code_exception(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_code异常')

    # @allure.story('删除自选股_根据code_code为空')
    # def test_code_code_null(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_code为空')

    # @allure.story('删除自选股_根据code_ts为空')
    # def test_code_ts_null(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_ts为空')

    # @allure.story('删除自选股_根据code_type异常')
    # def test_code_type_exception(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_type异常')

    # @allure.story('删除自选股_根据code_type为空')
    # def test_code_type_null(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_type为空')

    # @allure.story('删除自选股_根据code_ts异常2')
    # def test_code_ts_exception2(self):
    #     response = zhuorui('自选股', '删除自选股_根据code_ts异常2')

    @allure.story('删除自选股_All')
    def test_all(self):
        q = OperationSql()
        userId = str(q.show_sql("select id from t_user_account where `zr_no`= '15685670';"))
        print(userId[2:-3:])
        id = MongoDB("userId", userId[2:-3:])
        list1 = list()
        for id1 in id:
            list1.append(str(id1.get('_id')))
        _id = {"ids": list1}
        # 写
        write_xlsx("自选股", str(_id))
        response = zhuorui('自选股', '删除自选股_All')
        assert_data(response, '000000', 'ok')

    # @allure.story('删除自选股_参数列表空')
    # def test_parameter_null(self):
    #     response = zhuorui('自选股', '删除自选股_参数列表空')
    #     print(response.json())
    #     assert_data(response, '000000', 'ok')


# if __name__ == '__main__':
#     pytest.main()
