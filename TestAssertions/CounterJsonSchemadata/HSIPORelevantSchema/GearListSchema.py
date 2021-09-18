GearListSchema = {
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
            "type": "array",
            "items": [
                {
                    "ipoQtys": {
                        "type": "array",
                        "items": [
                            {
                                "applyQty": {
                                    "type": "number",
                                    "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                                },
                                "applyBalance": {
                                    "type": "number",
                                    "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                                },
                            }
                        ]
                    },
                    "financingRatios": {
                        "type": "array"},
                    "items": [
                        {
                            "ratio": {
                                "type": "number",
                                "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                            },
                            "lever": {
                                "type": "number",
                                "pattern": r"^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$"
                            },
                        }
                    ]
                }
            ]
        }
    }
}
