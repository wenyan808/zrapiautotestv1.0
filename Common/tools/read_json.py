import json


# 读取json数据
def get_json(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# if __name__ == '__main__':
#     file = r"D:\apiauto-test-zhuorui\Test_Data\user-relateapi.json"
#
#
#
#     data = get_json(file)
#     print(data)
