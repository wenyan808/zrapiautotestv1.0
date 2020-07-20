# 发送邮件
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(filename):
    # 需要用到smtplib模块
    # 需要用到email模块
    # 登录QQ邮箱
    from_addr = "647857136@qq.com"
    password = "ycyevvbfkyjkbdce"
    stmp_server = "smtp.qq.com"
    # 实例化邮件对象
    msgRoot = MIMEMultipart()
    # 发送人
    msgRoot['From'] = "647857136@qq.com"
    # 设置邮箱标题
    msgRoot["Subject"] = "卓锐API测试"
    # 接收人
    msgRoot["To"] = ",".join(["q18379204975@163.com"])
    # 设置邮件正文内容
    msgText = MIMEText("接口测试报告")
    # 添加邮件正文内容
    msgRoot.attach(msgText)
    # 添加附件
    att = MIMEText(open(filename, "rb").read(), "basde64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment; filename={}".format(filename.strip("/")[-1])
    msgRoot.attach(att)

    server = smtplib.SMTP(stmp_server, 25)
    # 登录邮件服务器
    server.login(from_addr, password)
    # 发送文件
    server.sendmail(from_addr, ["647857136@qq.com"], msgRoot.as_string())
