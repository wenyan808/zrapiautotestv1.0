# 字段说明：url路径，paylo接受参数，sign1可以自动生成签名，headers为头部信息，response为返回报文
import requests, json
from Common.tools.read_yaml import yamltoken
from Common.sign import get_sign
from glo import JSON, HTTP
import logging


def common(i):
    http = HTTP
    header = JSON
    token2, urll, requestmode, paylop = i[3], i[5], i[6], i[7]
    url = http + urll
    # print(url)
    paylo = eval(paylop)
    # print(paylo)
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    # 调用登录接口通过token传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)
    headers = header
    # print(token)
    # print(type(token))
    if token2 == 1:
        token1 = yamltoken()
        # print(TOKEN)
        token = {"token": token1}
        headers.update(token)
    # print(headers)
    payload = json.dumps(dict(payload1))

    # data = {
    #     "url": url,
    #     "requestmode": requestmode,
    #     "headers": headers,
    #     "payload": payload
    # }
    # with open(BASE_DIR +"/TestConfig/data.ini", "w", encoding="utf-8") as f:
    #     f.write(f"{data}\n")
    # write_config(BASE_DIR +"/TestConfig/data.ini","w",data)
    # print(data)

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
