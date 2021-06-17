import json
import oss2

from Common.Upload.GetsecurityToken import getsecurityToken

from Common.Upload.img_file_path import imgURL, fileURL

from Common.getTestLoginToken import getlogintoken
from Common.login import login
from Common.show_sql import showsql
from Common.tools.read_yaml import yamltoken
from glo import BASE_DIR, phone2, HTTP, JSON, phoneArea, pwd, phone


def oss_img(Storage_directory: str, img_name: str, userId: str, catalog: str, url: str, headers: dict):
    """上传图片到OSS()
    在调用这个方法时，请参照http://192.168.1.203:3001/project/54/interface/api/5072的说明进行参考
    :param Storage_directory:存放目录
    :param img_name: 图片的名字
    :param userId: 用户的userid
    :param catalog: 存放路径 如：/Business/UserFileUp/
    :param url: url地址
    :param headers: headers参数(里面包含登录的token)
    :return: 图片的url
    """
    local_img_path = BASE_DIR + catalog + img_name
    # print(local_img_path)
    name = Storage_directory + '/' + userId + '/{}'
    oss_img_path = imgURL(name) + img_name
    # print(oss_img_path)
    url = url
    header = headers

    rj = getsecurityToken(url, header)
    # print(rj)
    AccessKeyId = rj.get("accessKeyId")
    # print(AccessKeyId)
    AccessKeySecret = rj.get("accessKeySecret")
    # print(AccessKeySecret)
    SecurityToken = rj.get("securityToken")
    # print(SecurityToken)
    if Storage_directory == "open":
        Endpoint = rj.get("bucketNames")[0].get("endpoint")
        BucketName = rj.get("bucketNames")[0].get("bucketName")
    else:
        Endpoint = rj.get("bucketNames")[1].get("endpoint")
        BucketName = rj.get("bucketNames")[1].get("bucketName")
    auth = oss2.StsAuth(AccessKeyId, AccessKeySecret, SecurityToken)
    endpoint = 'http://' + Endpoint
    # print(endpoint)
    bucket = oss2.Bucket(auth, endpoint, BucketName)

    # print(bucket)
    result = bucket.put_object_from_file(oss_img_path, local_img_path)
    # print(result.status)
    if result.status == 200:
        jpg_url = bucket.sign_url('GET', oss_img_path, 6000)  # 阿里返回一个关于Zabbix_Graph.jpg的url地址 60是链接60秒有效
        jpg_url = json.dumps(jpg_url)
        # print(jpg_url)
        return jpg_url, oss_img_path
    else:
        print("上传失败")


def oss_file(Storage_directory: str, file_name: str, catalog: str, url: str, headers: dict):
    """上传文件到oss
    在调用这个方法时，请参照http://192.168.1.203:3001/project/54/interface/api/5072的说明进行参考
    :param Storage_directory:存放目录
    :param file_name: 文件名字
    :param catalog: 存放路径 如：/Business/UserFileUp/
    :param url: url地址
    :param headers: headers参数(里面包含登录的token)
    :return: 返回文件的url
    """
    local_file_path = BASE_DIR + catalog + file_name
    # print(local_file_path)
    name = Storage_directory + '/{}'
    oss_file_path = fileURL(name) + file_name
    # print(oss_file_path)
    url = url
    header = headers
    j = getsecurityToken(url, header)
    AccessKeyId = j.get("accessKeyId")
    AccessKeySecret = j.get("accessKeySecret")
    SecurityToken = j.get("securityToken")
    if Storage_directory == "open":
        Endpoint = j.get("bucketNames")[0].get("endpoint")
        BucketName = j.get("bucketNames")[0].get("bucketName")
    else:
        Endpoint = j.get("bucketNames")[1].get("endpoint")
        BucketName = j.get("bucketNames")[1].get("bucketName")
    auth = oss2.StsAuth(AccessKeyId, AccessKeySecret, SecurityToken)
    endpoint = 'http://' + Endpoint
    # print(endpoint)
    bucket = oss2.Bucket(auth, endpoint, BucketName)
    # 必须以二进制的方式打开文件，因为需要知道文件包含的字节数。
    with open(local_file_path, 'rb') as fileobj:
        bucket.put_object(oss_file_path, fileobj)
        file_url = bucket.sign_url('GET', oss_file_path, 6000)
        file_url = json.dumps(file_url)
        # print(file_url)
        return file_url, oss_file_path


# print(oss_file("sensitive_word", "敏感词.xlsx"))
# userId1 = showsql(
#     '192.168.1.237', 'root', '123456', "user_account",
#     f"select user_id from t_user_account where 'phone'= '{phone}';"
# )
# userId = list(list(userId1)[0])[0]
# catalog = r"/Business/Img/community/"
# url1 = HTTP + "/as_common/api/sts/v1/token"
# header = JSON
# login()
# token1 = yamltoken()
# token = {"token": token1}
# header.update(token)
# print(header)
#
# # print(list(oss_img("community", "zhurong.png", userId, catalog, url1, headers)))
# print(oss_img("community", "zhurong.png", userId, catalog, url1, header))
# 参考链接：https://www.cnblogs.com/coolops/p/12841334.html


# 参考链接：https://help.aliyun.com/document_detail/88434.html?spm=a2c4g.11186623.6.1189.274e2da16jq1Mh
# # 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
# auth = oss2.Auth('yourAccessKeyId', 'yourAccessKeySecret')
# # yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
# # 填写Bucket名称。
# bucket = oss2.Bucket(auth, 'yourEndpoint', 'examplebucket')
#
#
# # 定义回调参数Base64编码函数。
# def encode_callback(callback_params):
#     cb_str = json.dumps(callback_params).strip()
#     return oss2.compat.to_string(base64.b64encode(oss2.compat.to_bytes(cb_str)))
#
#
# # 设置上传回调参数。
# callback_params = {}
# # 设置回调请求的服务器地址，例如http://oss-demo.aliyuncs.com:23450。
# callback_params['callbackUrl'] = 'http://oss-demo.aliyuncs.com:23450'
# # （可选）设置回调请求消息头中Host的值，即您的服务器配置Host的值。
# # callback_params['callbackHost'] = 'yourCallbackHost'
# # 设置发起回调时请求body的值。
# callback_params['callbackBody'] = 'bucket=${bucket}&object=${object}'
# # 设置发起回调请求的Content-Type。
# callback_params['callbackBodyType'] = 'application/x-www-form-urlencoded'
# encoded_callback = encode_callback(callback_params)
# # // 设置发起回调请求的自定义参数，由Key和Value组成，Key必须以x:开始。
# callback_var_params = {'x:my_var1': 'my_val1', 'x:my_var2': 'my_val2'}
# encoded_callback_var = encode_callback(callback_var_params)
#
# # 上传并回调。
# params = {'callback': encoded_callback, 'callback-var': encoded_callback_var}
# # 填写Object完整路径和字符串。Object完整路径中不能包含Bucket名称。
# result = bucket.put_object('exampleobject.txt', 'a' * 1024 * 1024, params)
#
#
#
#
# import os
# from oss2 import SizedFileAdapter, determine_part_size
# from oss2.models import PartInfo
# import oss2
#
# # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录RAM控制台创建RAM账号。
# auth = oss2.Auth('<yourAccessKeyId>', '<yourAccessKeySecret>')
# # Endpoint以杭州为例，其它Region请按实际情况填写。
# bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', '<yourBucketName>')
#
# key = '<yourObjectName>'
# filename = '<yourLocalFile>'
#
# total_size = os.path.getsize(filename)
# # determine_part_size方法用于确定分片大小。
# part_size = determine_part_size(total_size, preferred_size=100 * 1024)
#
# # 初始化分片。
# # 如需在初始化分片时设置文件存储类型，请在init_multipart_upload中设置相关headers，参考如下。
# # headers = dict()
# # headers["x-oss-storage-class"] = "Standard"
# # upload_id = bucket.init_multipart_upload(key, headers=headers).upload_id
# upload_id = bucket.init_multipart_upload(key).upload_id
# parts = []
#
# # 逐个上传分片。
# with open(filename, 'rb') as fileobj:
#     part_number = 1
#     offset = 0
#     while offset < total_size:
#         num_to_upload = min(part_size, total_size - offset)
#         # 调用SizedFileAdapter(fileobj, size)方法会生成一个新的文件对象，重新计算起始追加位置。
#         result = bucket.upload_part(key, upload_id, part_number,
#                                     SizedFileAdapter(fileobj, num_to_upload))
#         parts.append(PartInfo(part_number, result.etag))
#
#         offset += num_to_upload
#         part_number += 1
#
# # 完成分片上传。
# # 如需在完成分片上传时设置文件访问权限ACL，请在complete_multipart_upload函数中设置相关headers，参考如下。
# # headers = dict()
# # headers["x-oss-object-acl"] = oss2.OBJECT_ACL_PRIVATE
# # bucket.complete_multipart_upload(key, upload_id, parts, headers=headers)
# bucket.complete_multipart_upload(key, upload_id, parts)
#
# # 验证分片上传。
# with open(filename, 'rb') as fileobj:
#     assert bucket.get_object(key).read() == fileobj.read()
#
#
#
#
