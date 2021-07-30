# 字段说明：url路径，paylo接受参数，sign1可以自动生成签名，headers为头部信息，response为返回报文
import requests, json
from Common.tools.read_write_yaml import yamltoken
from Common.sign import get_sign
from glo import JSON, HTTP
import logging


def common(i):
    http = HTTP
    header = JSON
    headers = {}
    headers.update(header)
    token2, urll, requestmode, paylop = i[3], i[5], i[6], i[7]
    url = http + urll
    paylo = eval(paylop)
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    # 调用登录接口通过token传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    if token2 == 1:
        token1 = yamltoken()
        token = {"token": token1}
        # asdad = {"123": "sd"}
        headers.update(token)

    payload = json.dumps(dict(payload1))
    # print(
    #     f"\n请求地址：{url}"
    #     f"\nbody参数：{payload}"
    #     f"\n请求头部参数：{headers}"
    # )

    response = requests.request(requestmode, url, headers=headers, data=payload)
    logging.info(
        f"""请求：
url:{url}
method:{requestmode}
headers:{headers}
data:{payload}
"""
    )
    if response.encoding:
        text = response.content.decode(response.encoding)
    else:
        text = response.text
    logging.info(
        f"""响应：
url:{response.url}
status_code:{response.status_code}
headers:{response.headers}
cookies:{dict(response.cookies)}
text:{text.encode("utf-8").decode("unicode_escape")}
"""
    )
    # # res = response.json().get("data")
    # # code = response.json().get('code')
    # print(response.json())
    return response

    # print(response.json())

# assert code == '000000'

# print(res)


