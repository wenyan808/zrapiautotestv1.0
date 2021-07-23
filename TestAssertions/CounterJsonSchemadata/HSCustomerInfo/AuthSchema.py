authSchema = {
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
                "userId": {
                    "type": "string",
                    # 符合该关键字指定的正则表达式，才算通过校验。
                    "pattern": "^[a-zA-Z0-9]{32}$"
                },
                "forceChangePwd": {
                    "type": "number",
                    "oneOf": [
                        {"type": "number", "mul2tipleOf": 0},
                        {"type": "number", "multipleOf": 1}
                    ]
                }
            }
        }
    }
}
