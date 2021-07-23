GearListSchema={
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
        }
    }
}