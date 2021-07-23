GetFundsInfoSchema = {
    # required表示数据里必须有这2个字段"msg", "code"
    "required": [
        "code",
        "msg",
        "data",
        "sellAmt"
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
                        "pattern": "^[A-Z]{3}$"
                    },
                    "fundAccount": {
                        "type": "string",
                        "pattern": "^[0-9]{10}$"
                    },
                    "accType": {
                        "type": "number",
                        "oneOf": [
                            {"type": "string", "multipleOf": "C"},
                            {"type": "string", "multipleOf": "M"}
                        ]
                    },
                    "mv": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 10
                    },
                    "enableBalance": {
                        "type": "number",
                        "pattern": "^[0-9]{10}$",
                        "minimum": 0,
                        "maximum": 100000000000
                    },

                    "netAssets": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "cashAmt": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "freezeAmt": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "fetchBalance": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "buyAmt": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "sellAmt": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "holdMv": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    }
                },
                {
                    "moneyType": {
                        "type": "string",
                        "pattern": "^[A-Z]{3}$"
                    },
                    "fundAccount": {
                        "type": "string",
                        "pattern": "^[0-9]{10}$"
                    },
                    "accType": {
                        "type": "number",
                        "oneOf": [
                            {"type": "string", "multipleOf": "C"},
                            {"type": "string", "multipleOf": "M"}
                        ]
                    },
                    "mv": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 10
                    },
                    "enableBalance": {
                        "type": "number",
                        "pattern": "^[0-9]{10}$",
                        "minimum": 0,
                        "maximum": 100000000000
                    },

                    "netAssets": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "cashAmt": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "freezeAmt": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "fetchBalance": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "buyAmt": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "sellAmt": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "holdMv": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    }
                },
                {
                    "moneyType": {
                        "type": "string",
                        "pattern": "^[A-Z]{3}$"
                    },
                    "fundAccount": {
                        "type": "string",
                        "pattern": "^[0-9]{10}$"
                    },
                    "accType": {
                        "type": "number",
                        "oneOf": [
                            {"type": "string", "multipleOf": "C"},
                            {"type": "string", "multipleOf": "M"}
                        ]
                    },
                    "mv": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 10
                    },
                    "enableBalance": {
                        "type": "number",
                        "pattern": "^[0-9]{10}$",
                        "minimum": 0,
                        "maximum": 100000000000
                    },

                    "netAssets": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "cashAmt": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "freezeAmt": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "fetchBalance": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "buyAmt": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "sellAmt": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    },
                    "holdMv": {
                        "type": "number",
                        "minLength": 0,
                        "maxLength": 15
                    }
                }
            ]
        }
    }
}
