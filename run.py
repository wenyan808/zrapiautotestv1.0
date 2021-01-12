import os



if __name__ == '__main__':
    os.system('pytest --alluredir=./report/xml')
    os.system('allure generate ./report/xml -o ./report/html --clean')