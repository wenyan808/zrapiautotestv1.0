import logging
import os


def read_txt(file: str) -> list:
    """读取txt文件的数据

    :param file: 文件路径
    :return: 数据列表
    """
    logging.info(f"数据文件路径：{os.path.abspath(file)}")
    data = []
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            # 去除注释行
            if line[0] == '#':
                continue
            # 去除换行符
            if line[-1] == '\n':
                line = line[:-1]
            # 去除空行
            if line.strip() == "":
                continue
            data.append(line.split("|"))

    return data


if __name__ == '__main__':
    L = read_txt(r"..\..\Test_Data/stock_ts_code.txt")
    print(L)