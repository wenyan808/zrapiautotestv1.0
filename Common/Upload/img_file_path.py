
import os
import time


from PIL import Image
from pandas.tests.dtypes.test_missing import now

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 获取图片大小
def imgSize(img_path):
    img = Image.open(img_path)
    # print(img.size)
    return img.size


# 生成存放图片路径
def imgURL(name):
    # random_name = now.strftime("%Y/%m/%d/") + str(round(time.time() * 1000)) + str(random.randint(1000, 9999))
    random_name = str(round(int(time.time())))
    # 存放OSS路径
    file_name = name.format(random_name)
    # print(file_name)
    return file_name


# 生成存放文件路径
def fileURL(name):
    random_name = now.strftime("%Y%m%d/")+ str(round(int(time.time())))
    # 存放OSS路径
    file_name = name.format(random_name)
    # print(file_name)
    return file_name
