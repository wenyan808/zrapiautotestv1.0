RemitBankListSchema = {
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
            "type": "array",
            "items": [
                {
                    "bankId": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"},
                    "type": {
                        "type": "number",
                        "minimum": 0,
                        "exclusiveMaximum": 100,
                    },
                    "status": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 10
                    },
                    "pictUrl": {
                        "type": "string"
                    },
                    "jumpUrl": {
                        "type": "string"
                    }

                }
            ]
        }
    }
}
