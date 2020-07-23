import os

import pytest

if __name__ == '__main__':
    pytest.main(['--alluredir', '../allure-xml'])
    os.system('pytest --alluredir=./report/xml')
    os.system('allure generate ./report/xml -o ./report/html --clean')