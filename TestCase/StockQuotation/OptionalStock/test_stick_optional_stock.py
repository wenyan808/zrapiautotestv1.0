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
        q = OperationSql()
        userId = str(q.show_sql("select id from t_user_account where `zr_no`= '10000038';"))
        id = MongoDB("userId", userId[2:-3:])
        cls._id = {"id": str(id[0].get('_id'))}

    @allure.story('置顶自选股')
    def test_stick(self):
        # 写
        write_xlsx("自选股", 59, 7, str(self._id))
        response = zhuorui('自选股', '置顶自选股')
        print(response.json())
        # assert_data(response, '000000', 'ok')

    @allure.story('置顶自选股_已置顶')
    def test_already_stick(self):
        # 写
        write_xlsx("自选股", 58, 7, str(self._id))
        response = zhuorui('自选股', '置顶自选股_已置顶')
        print(response.json())
        # assert_data(response, '000000', 'ok')


if __name__ == '__main__':
    pytest.main()


