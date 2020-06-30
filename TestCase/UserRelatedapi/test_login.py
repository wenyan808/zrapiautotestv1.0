import allure
import pytest

from Common.assertapi import assert_data
from Common.guide import zhuorui
from Common.login_xinxi import login_xinxi
from Common.tools.write_xlsx import write_xlsx
from glo import BASE_DIR


class TestLogin:
    @allure.story('用户密码登录')
    def test_login(self):
        paylo = login_xinxi('18379204795', '102522ql', '86')
        # 写
        write_xlsx("Sheet1", 1, 7, str(paylo))
        response = zhuorui('Sheet1', '用户密码登录')
        assert_data(response, '000000', 'ok')
        resp = response.json().get('code')
        if resp == "000000":
            res = response.json().get('data').get('token')
            with open(BASE_DIR + r'/TestData/token.yaml', 'w') as file:
                file.write("token: " + res)


if __name__ == '__main__':
    pytest.main()





