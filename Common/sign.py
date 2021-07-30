import requests
import json


def get_sign(payload1):
    url = "http://192.168.1.209:1130/sign"

    payload = payload1
    headers = {
        'Content-Type': 'application/json'
    }
    jdata = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=jdata)
    sign1 = str(response.text.encode('utf8'))
    sign = sign1[2:-1:]
    # print(response)
    return sign
# print(get_sign({"password": "372003d405088971640c0b6bfd6a7346", "phone": "15816263996", "phoneArea": "86"}))
# print(get_sign({}))
# get_sign({
#   "handicap": {
#       "stockList": [{"ts":"SH","type":"2","code":"688466"}],
#       "phone": "18379204795",
#       "password": "33791626cdcbbf5b0b834f9d808f3188",
#       "phoneArea": "86"
#     }
# })
