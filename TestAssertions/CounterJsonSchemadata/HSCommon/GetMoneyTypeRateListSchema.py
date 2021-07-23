getMoneyTypeRateListSchema = {
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
                    "moneyType": {
                        "type": "string",
                        # 符合该关键字指定的正则表达式，才算通过校验。
                        "pattern": "^[A-Z]{3}$"
                    },
                    "rate": {
                        "type": "number"}},
                {
                    "moneyType": {
                        "type": "string",
                        # 符合该关键字指定的正则表达式，才算通过校验。
                        "pattern": "^[A-Z]{3}$"
                    },
                    "rate": {
                        "type": "number"
                    }
                },
                {
                    "moneyType": {
                        "type": "string",
                        # 符合该关键字指定的正则表达式，才算通过校验。
                        "pattern": "^[A-Z]{3}$"
                    },
                    "rate": {
                        "type": "number"
                    }
                }
            ]
        }
    }
}
