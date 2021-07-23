GetEnableBalanceSchema = {
    # required表示数据里必须有这2个字段"msg", "code"
    "required": [
        "code",
        "msg",
        "data"
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
                "enableBalance": {
                    "type": "number",
                    "pattern": "^[0-9]{10}$",
                    "minimum": 0,
                    "maximum": 100000000000
                }
            }
        }
    }
}
