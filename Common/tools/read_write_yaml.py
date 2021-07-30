import yaml

from glo import BASE_DIR


def yamlconfig(name):
    with open(BASE_DIR + '/TestData/' + name + '.yaml', 'rb') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    name1 = data.get(name)
    return name1
    # print(name1)


# print(yamlconfig("flag"))
def write_yaml(name, data):
    with open(BASE_DIR + '/TestData/' + name + '.yaml', "w", encoding="utf-8") as f:
        f.write("flag: " + data)




def yamltoken():
    with open(BASE_DIR + r'/TestData/token.yaml', 'rb') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    name1 = data.get('token')
    return name1
    # print(name1)

# yamltoken()
