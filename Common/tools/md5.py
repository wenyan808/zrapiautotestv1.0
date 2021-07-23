import hashlib


def get_md5(s: str):
    if s:
        m = hashlib.md5()
        m.update(str(s).encode("utf-8"))
        return m.hexdigest()
    raise TypeError("传入参数不能为空")


print(get_md5("zr123456"))