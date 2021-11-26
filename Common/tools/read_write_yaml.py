import yaml

from glo import BASE_DIR


def yamlconfig(name):
    """配置一个自定义名称的yaml文件"""
    with open(BASE_DIR + '/TestData/' + name + '.yaml', 'rb') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    name1 = data.get(name)
    return name1
    # print(name1)


# print(yamlconfig("flag"))
def write_yaml(name, data):
    """写入到自定义名称的yaml文件"""
    with open(BASE_DIR + '/TestData/' + name + '.yaml', "w", encoding="utf-8") as f:
        f.write("flag: " + data)

def read_yaml(name):
    """读取自定义名称的yaml文件"""
    with open(BASE_DIR + r'/TestData/' + name + '.yaml', 'rb') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    name1 = data.get('flag')
    return name1


def yamltoken():
    """获取token.yaml文件中的token"""
    with open(BASE_DIR + r'/TestData/token.yaml', 'rb') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    name1 = data.get('token')
    return name1
    # print(name1)

# yamltoken()
