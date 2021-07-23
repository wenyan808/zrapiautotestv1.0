PurRecordDetailSchema = {
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
            "ts": {
                "type": "string",
                "oneOf": [
                    {"type": "string", "multipleOf": "SH"},
                    {"type": "string", "multipleOf": "HK"},
                    {"type": "string", "multipleOf": "SZ"},
                    {"type": "string", "multipleOf": "US"}
                ]
            },
            "code": {
                "type": "string",
                "pattern": "[A-Za-z0-9]*$"
            },
            "name": {
                "type": "string",
                "minLength": 0,
                "maxLength": 30
            },
            "moneyType": {
                "type": "string"
            },
            "handlingFee": {
                "type": "string"
            },
            "depositDate": {
                "type": "string",
                "format": "data_time",
                "minLength": 13
            },
            "closeTime": {
                "type": "string",
                "format": "data_time",
                "minLength": 13
            }
        }
    }
}
