# import hashlib

from Common.tools.md5 import get_md5


def login_xinxi(phone, pwd, area):
    # 输入你的手机号和密码

    # print(pwd1)
    # 创建md5对象
    # m = hashlib.md5()
    #
    # b = pwd.encode(encoding='utf-8')
    # m.update(b)
    # pwd1_md5 = m.hexdigest()
    # 加密
    pwd_md5 = get_md5(pwd)

    return {"phone": phone, "loginPassword": pwd_md5, "phoneArea": area}
# print(pwd1)


# login_xinxi()
