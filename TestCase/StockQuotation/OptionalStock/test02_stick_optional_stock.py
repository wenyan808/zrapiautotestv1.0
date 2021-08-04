import allure
import pytest
from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login import login
from Common.show_sql import MongoDB, showsql
from Common.tools.write_xlsx import write_xlsx


class TestStickOptionalStock:
    @classmethod
    def setup_class(cls) -> None:
        login()
        userId = showsql(
            '192.168.1.237', 'root', '123456', "user_account",
            "select user_id from t_user_account where `zr_no`= '68904140';"
        )
        # print(userId)
        id = MongoDB("192.168.1.236", 27017, "stock_market", "t_stock_selected", "userId", list(list(userId)[0])[0])
        print(id)
        cls._id = {"id": str(id[0]["_id"])}

    @allure.story('置顶自选股')
    def test_stick(self):
        # 写
        write_xlsx("自选股", 59, 7, str(self._id))
        response = zhuorui('自选股', '置顶自选股')
        assert_data(response, '000000', 'ok')

    @allure.story('置顶自选股_已置顶')
    def test_already_stick(self):
        # 写
        write_xlsx("自选股", 58, 7, str(self._id))
        response = zhuorui('自选股', '置顶自选股_已置顶')
        # print(response.json())
        assert_data(response, '000000', 'ok')

    @allure.story('置顶自选股_id为空')
    def test_stick_id_null(self):
        response = zhuorui('自选股', '置顶自选股_id为空')
        print(response.json())
        assert_data(response, '000103', 'id不能为空')

    @allure.story('置顶自选股_参数为空')
    def test_stick_parameter_null(self):
        response = zhuorui('自选股', '置顶自选股_参数为空')
        print(response.json())
        assert_data(response, '000103', 'id不能为空')

    @allure.story('置顶自选股_id不正确')
    def test_stick_id_error(self):
        response = zhuorui('自选股', '置顶自选股_id不正确')
        print(response.json())
        assert_data(response, '000200', '数据不存在，操作失败')

    @allure.story('置顶自选股_id异常')
    def test_stick_id_exception(self):
        response = zhuorui('自选股', '置顶自选股_id异常')
        print(response.json())
        assert_data(response, '000200', '数据不存在，操作失败')

    @allure.story('置顶自选股无token')
    def test_stick_notoken(self):
        # 写
        write_xlsx("自选股", 76, 7, str(self._id))
        response = zhuorui('自选股', '置顶自选股无token')
        assert_data(response, '000101', 'token不能为空')


if __name__ == '__main__':
    pytest.main()
