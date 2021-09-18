PurRecordListSchema = {
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
                        "type": "string"},
                    "type": {
                        "type": "number",
                        "anyOf": [  # 满足其中一个类型 就行
                            {"type": "integer", "pattern": 1},
                            {"type": "integer", "pattern": 2}
                        ]
                    },
                    "name": {
                        "type": "string",
                        "pattern": r"^[\u4E00-\u9FA5A-Za-z0-9_]+$"
                    },
                    "applyQty": {
                        "type": "number",
                        "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$ "
                    },
                    "moneyType": {
                        "type": "string",
                        "pattern": r"^[A-Z]+$"
                    },
                    "applyBalance": {
                        "type": "number",
                        "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                    },
                    "status": {
                        "type": "string",
                        "pattern": r"^[0-9]*$"
                    },
                    "statusCheck": {
                        "type": "string",
                        "pattern": r"^(0|[1-9][0-9]*)$"
                    },
                    "handlingFee": {
                        "type": "number",
                        "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                    },
                    "allottedQty": {
                        "type": "number",
                        "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                    },
                    "applyDatetime": {
                        "type": "number",
                        "pattern": r"^[0-9]*$"
                    },
                    "financingType": {
                        "type": "number",
                        "pattern": r"^(0|[1-9][0-9]*)$"
                    },
                    "financingInterest": {
                        "type": "number",
                        "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                    }
                }
            ]
        }
    }
}
