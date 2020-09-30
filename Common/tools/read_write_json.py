


import json


# 读取json数据
def get_json(file: str):
    """读取并获取json文件

    :param file: 文件路径
    :return:
    """
    with open(file, "r", encoding="utf-8") as f:
        data_json = json.load(f)
    return data_json
    # jsonData = json.load(f)
    # data_list = list()
    # for data in jsonData.values():
    #     data_list.append(data)
    # return data_list


def write_json(file, data):
    """写入json文件

    :param file: 文件路径
    :param data:需要传入的数据
    :return:
    """

    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)  # 写为多行

# if __name__ == '__main__':
#     file = r"D:\apiauto-test-zhuorui\Test_Data\user-relateapi.json"
#
#
#
#     data = get_json(file)
#     print(data)
