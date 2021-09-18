SubscribeListSchema = {
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
            "type": "string",
            "minLength": 6,
            "maxLength": 6
        }
    },
    "data": {
        "type": "array",
        "items": [
            {
                "ts": {
                    "type": "string"
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
                "volunit": {
                    "type": "number",
                    "pattern": "^(0|[1-9][0-9]*)$"
                },
                "minPrice": {
                    "type": "number",
                    "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                },
                "maxPrice": {
                    "type": "number",
                    "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                },
                "endTime": {
                    "type": "number",
                    "pattern": r"^[0-9]*$"
                },
                "entranceFee": {
                    "type": "number",
                    "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                },
                "handlingFee": {
                    "type": "number",
                    "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                },
                "favor": {
                    "anyOf": [  # 满足其中一个类型 就行
                        {"type": "boolean", "pattern": True},
                        {"type": "boolean", "pattern": False}
                    ]
                },
                "analyzeUrl": {
                    "type": "string",
                    "pattern": r"[a-zA-z]+://[^\s]*"
                },
                "compFinancingBalance": {
                    "type": "number",
                    "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                },
                "financingHandlingFee": {
                    "type": "number",
                    "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                },
                "stopFinancingFlag": {
                    "anyOf": [  # 满足其中一个类型 就行
                        {"type": "string", "pattern": "N"},
                        {"type": "string", "pattern": "Y"}
                    ]
                },
                "ipoIntrate": {
                    "type": "number",
                    "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                },
                "financingDays": {
                    "type": "number",
                    "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                },
                "cashRatio": {
                    "type": "number",
                    "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                }
            }
        ]
    }
}
