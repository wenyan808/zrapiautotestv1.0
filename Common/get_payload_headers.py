import json

from Common.sign import get_sign


def get_payload(payload):
    """获取boby或者payload

    :param payload:请求参数body  注意：bool数据传true  false 和 null需要加上""
    :return:返回带签名sign的请求参数
    """
    sign1 = {"sign": get_sign(payload)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(payload)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))
    return eval(payload)


def get_headers(header, token=None):
    """获取headers

    :param header: 请求头参数不包含token
    :param token: 如token = {"token": getLoginAccountToken(phone6, pwd)}
    :return:返回带token的headers
    """
    headers = {}
    headers.update(header)
    # token = {"token": getLoginAccountToken(phone6, pwd)}
    headers.update(token)  # 将token更新到headers
    # print(headers)

    headers1 = json.dumps(dict(headers))
    return eval(headers1)
