# 用户密码登录
# 字段说明：url路径，paylo接受参数，sign1可以自动生成签名，headers为头部信息，response为返回报文
import requests
import json

import yaml

from Common.tools.read_xlsx_exampleshuju import shuju
from Common.login_xinxi import login_xinxi
from Common.sign import get_sign
import glo
from glo import BASE_DIR


def test_loginpwd(sheet):
    # 用户密码登录
    for i in shuju(sheet):
        if "登录" in i:
            urll, requestmode, palop = i[5], i[6], i[7]
            http = glo.HTTP
            # print(http)
            header = glo.JSON
            url = http + urll
            # print(urll)
            paylo = {}
            paylo.update(login_xinxi(eval(i[7])['phone'], eval(i[7])['password'],
                                     eval(i[7])['phoneArea']))  # 在login_xinxi(phone，password)里面填写的格式
            sign1 = {"sign": get_sign(paylo)}
            payload1 = {}
            payload1.update(paylo)
            payload1.update(sign1)
            payload = json.dumps(dict(payload1))
            headers = header
            # print(paylo)
            response = requests.request(requestmode, url, headers=headers, data=payload)
            resp = response.json().get('code')
            # print(resp)
            if resp == "000000":
                res = response.json().get('data').get('token')
                # glo.TOKEN = res
                # print(glo.TOKEN)
                # return res
                # print(res)
                # else :
                # print(json.loads(response.text).get('msg'))

                # print(resp)



                # with open(BASE_DIR + r'/TestData/token.yaml', 'w') as outfile:
                #     yaml.dump(data, outfile, default_flow_style=False)
                with open(BASE_DIR+r'/TestData/token.yaml','w') as file:
                    file.write("token: "+res)

# test_loginpwd()


# if __name__ == '__main__':
#     pytest.main(['-s', '-q', '--alluredir', '../allure-xml'])
