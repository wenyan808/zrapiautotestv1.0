import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import OperationSql, MongoDB
from Common.tools.write_xlsx import write_xlsx


class TestStickOptionalStock:
    @classmethod
    def setup_class(cls) -> None:
        login()
        q = OperationSql("192.168.1.237", "root", "123456", "user_account")
        userId = str(q.show_sql("select id from t_user_account where `zr_no`= '68904140';"))
        id = MongoDB("192.168.1.236", 27017, "stock_selector", "t_tactic6", "user", userId[3:-5:])
        # print(id)
        # print(id[-1].get('_id'))
        cls._id = {"id": str(id[-1].get('_id'))}

    @allure.story('置顶自选股')
    def test_stick(self):
        # 写
        write_xlsx("自选股", 62, 7, str(self._id))
        response = zhuorui('自选股', '置顶自选股')
        # print(response.json())
        assert_data(response, '000000', 'ok')

    @allure.story('置顶自选股_已置顶')
    def test_already_stick(self):
        # 写
        write_xlsx("自选股", 61, 7, str(self._id))
        response = zhuorui('自选股', '置顶自选股_已置顶')
        # print(response.json())
        assert_data(response, '000000', 'ok')

    # @allure.story('置顶自选股_id为空')
    # def test_stick_id_null(self):
    #     response = zhuorui('自选股', '置顶自选股_id为空')
    #     print(response.json())
    #     assert_data(response, '000000', 'ok')

    # @allure.story('置顶自选股_参数为空')
    # def test_stick_parameter_null(self):
    #     response = zhuorui('自选股', '置顶自选股_参数为空')
    #     print(response.json())
    #     assert_data(response, '000000', 'ok')

    # @allure.story('置顶自选股_id不正确')
    # def test_stick_id_error(self):
    #     response = zhuorui('自选股', '置顶自选股_id不正确')
    #     print(response.json())
    #     assert_data(response, '000000', 'ok')

    # @allure.story('置顶自选股_id异常')
    # def test_stick_id_exception(self):
    #     response = zhuorui('自选股', '置顶自选股_id异常')
    #     print(response.json())
    #     assert_data(response, '000000', 'ok')

    # @allure.story('置顶自选股无token')
    # def test_stick_notoken(self):
    #     # 写
    #     write_xlsx("自选股", 79, 7, str(self._id))
    #     response = zhuorui('自选股', '置顶自选股无token')
    #     # print(response.json())
    #     assert_data(response, '000101', 'token不能为空')


if __name__ == '__main__':
    pytest.main()
