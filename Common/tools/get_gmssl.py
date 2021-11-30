"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/11/16 17:01
# @Author:YiShouquan
# @File:get_gmssl.py
"""
import base64
import binascii

from gmssl import sm2
# sm2的公私钥
SM2_PRIVATE_KEY = '3eeec4dda8e4f615d451e0583f9b8a3eee34aa9dd93bdaca0e93c0691abcc90c'  # 私钥
SM2_PUBLIC_KEY = '04eb316a6de2c8a590c92fdb216cc5507b8bc772940941aca5ae04919' \
                 '37ab23ef3ee70f4fcac903d40ef2e59d32dd70fe0f1c41449fae6453d28930d01916ced69'  # 公钥


def get_sm2(data):
    """加密
    :param data: 传入值必须是这样的格式，如：b"123456"
    :return: 加密的数值
    """
    private_key = SM2_PRIVATE_KEY
    # 分割"04"
    public_key = SM2_PUBLIC_KEY.split('04', 1)[-1]
    # print(public_key)
    sm2_crypt = sm2.CryptSM2(
        public_key=public_key, private_key=private_key)
    # data = b"111"
    # 加密
    enc_data = sm2_crypt.encrypt(data)
    # print(enc_data.hex())
    return enc_data.hex()


# print(get_sm2(b"123456"))
# import base64
# h = base64.b16encode(get_sm2(b"123456"))
# print(h.decode('ascii'))
"""注：
如果你要进行解密那麽你需要公钥开头加上”04“
"""
