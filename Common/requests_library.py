import requests
import logging


class Requests(object):
    def __init__(self, session: requests.Session = None):
        self._session = session

    def get_session(self):
        """获取 session"""
        if self._session:
            logging.info(f"获得 session")
            return self._session
        logging.info("获取新session")
        return requests.Session()

    def close_session(self):
        """关闭"""
        logging.info("关闭 session")
        self._session.close()

    def get(self, url, params=None, headers=None, cookies=None, timeout=None, title=None):
        """get 请求

        :param url: 请求地址
        :param params: 查询参数
        :param headers: 消息头
        :param cookies: cookies
        :param timeout: 超时
        :param title: 动作标题
        :return:
        """
        logging.info(f"发送 get 请求：{title}")
        logging.info(
            f"""请求：
url:{url}
method:get
params:{params}
headers:{headers}
cookies:{cookies}
timeout:{timeout}
"""
        )
        r = self._session.request("GET", url=url, params=params, headers=headers, cookies=cookies, timeout=timeout)

        if r.encoding:
            text = r.content.decode(r.encoding)
        else:
            text = r.text

        logging.info(
            f"""响应：
url:{r.url}
status_code:{r.status_code}
headers:{r.headers}
cookies:{dict(r.cookies)}
text:{text.encode("utf-8").decode("unicode_escape")}
"""
        )
        return r

    def post(self, url, params=None, data=None, headers=None, cookies=None,
             timeout=None, json=None, title=None):
        """post 请求

        :param url: 请求地址
        :param params: 查询参数
        :param data: body数据：表单
        :param headers: 消息头
        :param cookies: cookies
        :param timeout: 超时
        :param json: body数据：json
        :param title: 动作标题
        :return:
        """
        logging.info(f"发送 post 请求：{title}")
        logging.info(
            f"""请求：
url:{url}
method:post
params:{params}
headers:{headers}
cookies:{cookies}
timeout:{timeout}
data:{data}
json:{json}
"""
        )
        r = self._session.request(
            "POST", url=url, params=params, headers=headers, cookies=cookies, timeout=timeout, data=data, json=json
        )

        if r.encoding:
            text = r.content.decode(r.encoding)
        else:
            text = r.text

        logging.info(
            f"""响应：
url:{r.url}
status_code:{r.status_code}
headers:{r.headers}
cookies:{dict(r.cookies)}
text:{text.encode("utf-8").decode("unicode_escape")}
"""
        )
        return r