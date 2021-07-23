import json

import requests

from Common.sign import get_sign
from glo import HTTP


def modify_submit_audit(headers):
    """修改资料提交审核(大陆+海外)
    ：:param headers:带token的请求参数headers
    ：:return 返回修改资料提交审核(大陆+海外)的结果数据
    """
    url = HTTP + "/as_user/api/cn_open/v1/modify_submit_audit"

    # 拼装参数
    paylo = {}
    # print(paylo)
    sign1 = {"sign": get_sign(paylo)}  # 把参数签名后通过sign1传出来
    payload1 = {}
    payload1.update(paylo)
    payload1.update(sign1)

    payload = json.dumps(dict(payload1))

    r = requests.session().post(
        url=url, headers=headers, data=payload
    )

    j3 = r.json()
    # print(j3)
    return j3
