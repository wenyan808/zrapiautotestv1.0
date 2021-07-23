getAccountInfoSchema = {
    # required表示数据里必须有这2个字段"msg", "code"
    "required": [
        "code",
        "msg"
    ],
    "type": "object",
    "properties": {
        "msg": {
            "type": "string",
            "pattern": "/ok/"
        },
        "code": {
            "type": "number",
            "minLength": 6,
            "maxLength": 6
        },
        "data": {
            "type": "object",
            "properties": {
                "clientId": {
                    "type": "string",
                    # 符合该关键字指定的正则表达式，才算通过校验。
                    "pattern": "^[0-9]{10}$"
                },
                "fundAccount": {
                    "type": "string",
                    # 符合该关键字指定的正则表达式，才算通过校验。
                    "pattern": "^[0-9]{10}$"
                },
                "accType": {
                    "type": "string",
                    "oneOf": [
                        {"type": "string", "multipleOf": "C"},
                        {"type": "string", "multipleOf": "M"}
                    ]
                },
                "renewalTime": {
                    "type": "number",
                    "oneOf": [
                        {"type": "number", "multipleOf": 0},
                        {"type": "number", "multipleOf": 15},
                        {"type": "number", "multipleOf": 30},
                        {"type": "number", "multipleOf": 60},
                        {"type": "number", "multipleOf": 180}
                    ]
                }
            }
        }
    }
}
