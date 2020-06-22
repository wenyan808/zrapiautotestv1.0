import os
from typing import Union

BASE_DIR: Union[bytes, str] = os.path.dirname(os.path.abspath(__file__))
HTTP = "http://192.168.1.241"
JSON = {
    "Content-Type": "application/json",
    "appVersion": '1.0',
    "deviceId": "032217ff0cf1c544",
    "osType": "android",
    "osVersion": '1.0'
}
# print(BASE_DIR)



