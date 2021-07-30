
def _init():
    global _global_pwd
    _global_pwd = ["123456"]
def set_value(pwd):
    _global_pwd[0] = pwd
def get_value():
    return _global_pwd[0]
_init()