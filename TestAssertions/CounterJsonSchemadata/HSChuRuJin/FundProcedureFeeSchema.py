FundProcedureFeeSchema = {  # required表示数据里必须有这2个字段"msg", "code"
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
            "type": "array",
            "items": [
                {
                    "fare": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100
                    },
                    "fareMoneyType": {
                        "type": "string",
                        "oneOf": [
                            {"type": "string", "multipleOf": "CNY"},
                            {"type": "string", "multipleOf": "HKD"},
                            {"type": "string", "multipleOf": "USD"}
                        ]
                    }
                }
            ]
        }
    }
}
