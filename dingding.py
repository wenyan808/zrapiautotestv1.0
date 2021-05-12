# -*- coding: UTF-8 -*-

import json
import requests


class DingDing(object):
    def __init__(self,
                 title,
                 at=False,
                 dev=False,
                 isAtAll=True,
                 url_1='http://image.sinajs.cn/newchart/daily/n/sz000333.gif',
                 ):
        """
        模拟钉钉机器人发消息
        :param title: 标题
        :param news: 消息内容
        :param at: @谁的手机号，列表形式，列表的元素为字符串；不填写默认不@任何人
        :param isAtAll: 为True时@所有人；为False时，不@任何人；不填写，默认不@任何人；
        """
        self.dev = dev
        self.title = title
        self.isAtAll = isAtAll
        # self.news = news
        self.at = at
        self.img_url_1 = url_1
        self.run()

    def run(self):
        # 群机器人
        url = "https://oapi.dingtalk.com/robot/send?access_token=09acd5ad506d0c05e0c5760d0eeefc1cf381ad53df5940d4248d1d8eae491fc2"
        with open('./allure-report/history/history-trend.json', 'r', encoding='utf8')as fp:
            json_data = json.load(fp)
            buildOrder = "#"+ str(json_data[0]["buildOrder"])
            failed = json_data[0]["data"]["failed"]
            broken = json_data[0]["data"]["broken"]
            total = json_data[0]["data"]["total"]
            failedc = json_data[0]["data"]["failed"] - json_data[1]["data"]["failed"]
            brokenc = json_data[0]["data"]["broken"] - json_data[1]["data"]["broken"]
            totalc = json_data[0]["data"]["total"] - json_data[1]["data"]["total"]
            news = [buildOrder,failed,failedc,broken,brokenc,total,totalc]
            # 设置@人员，列表，列表内的元素为字符串
            newsData = {
                "msgtype": "markdown",
                "markdown": {
                    "title": self.title,
                    "text":
                        # "![](" + self.img_url_1 + ")" + "\n\n" +
                        '<font color=#01814A size=3 face="微软雅黑" style="font-weight:bold;">··· 任务：%s</font>' % news[0] + "\n\n"
                        '<font color=#AE0000 size=2 face="微软雅黑">·· failed：%s</font>' % news[1] + "\n\n"
                        '<font color=#003E3E size=2 face="微软雅黑">· 相比上次：%s</font>' % news[2] + "\n\n"
                        '<font color=#FF359A size=2 face="微软雅黑">·· broken：%s</font>' % news[3] + "\n\n"
                        '<font color=#003E3E size=2 face="微软雅黑">· 相比上次：%s</font>' % news[4] + "\n\n"
                        '<font color=#3C3C3C size=2 face="微软雅黑">·· total：%s</font>' % news[5] + "\n\n"
                        '<font color=#0080FF size=2 face="微软雅黑">· 相比上次：%s</font>' % news[6] + "\n\n"
                        "![](" + self.img_url_1 + ")"
                },
                "at": {
                    "atMobiles": [],
                    "isAtAll": False
                }
            }
            if self.at:
                newsData['at']['atMobiles'].append(self.at)
            # 设置@所有人
            if self.isAtAll:
                newsData['at']['isAtAll'] = True

            headers = {
                'Content-Type': 'application/json; charset=utf-8'
            }
            # 关闭ssl安全警告
            requests.packages.urllib3.disable_warnings()
            f = requests.post(url, data=json.dumps(newsData), headers=headers, verify=False)


if __name__ == '__main__':
    DingDing(title='自动化任务标题', isAtAll=False)
