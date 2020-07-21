import os

import pytest
import requests
import sys
import json

# 查询股票价格
# from TestCase.StockQuotation import
# from TestCase.
# TestClass().test_cxzjtj()
# TestGetCapitalFlowTime().test_getCapitalFlowTime()
# test_cxzjtj()
# if __name__ == '__main__':
# 	pytest.main()


# if __name__ == '__main__':
#     pytest.main(['-s', '-q', '--alluredir', '../allure-xml'])
# TestClass1().test_hs()

os.system('if exist "report" (rd /s/q report)')
os.system('pytest --alluredir=./report/xml')
os.system('allure generate ./report/xml -o ./report/html --clean')

# send_email(filename)
