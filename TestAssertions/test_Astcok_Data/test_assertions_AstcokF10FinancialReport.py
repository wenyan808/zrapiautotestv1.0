result = {
    # 该关键字限制了JSON对象中必须包含哪些一级key。
    # 如果一个JSON对象中含有required关键字所指定的所有一级key，则该JSON对象能够通过校验。
    "required": [
        "code",
        "msg",
        "data",
        "mainBusinessReport",
        "profitReport",
        "liabilistyReport",
        "cashFlowReport",
        "profitDetailUrl",
        "liabilDetailUrl",
        "cashFlowDetailUrl"
    ],
    # 该关键字用于限定待校验JSON元素所属的数据类型，取值可为：object，array，integer，number，string，boolean，null
    # 约束对象是object，也就是在 properties{ } 中的数据
    "type": "object",
    # 用于指定JSON对象中的各种不同key应该满足的校验逻辑，# object中具体属性的约束，
    # 如果待校验JSON对象中所有值都能够通过该关键字值中定义的对应key的校验逻辑，每个key对应的值，都是一个JSON Schema，则待校验JSON对象通过校验。
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
                "mainBusinessReport": {
                    "type": "object",
                    "properties": {
                        "type": "array",
                        "items": [
                            {
                                "yearEndDate": {"type": "integer",
                                                "minLength": 13},
                                "reportType": {
                                    "type": "number",
                                    "anyOf": [
                                        {"type": "number", "reportType": 12},
                                        {"type": "number", "reportType": 9},
                                        {"type": "number", "reportType": 6},
                                        {"type": "number", "reportType": 1}
                                    ]},
                                "businessCate": {
                                    "type": "string",
                                    "minLength": 4
                                },
                                "currency": {
                                    "type": "string",
                                    "minLength": 3
                                },
                                "currentYearTurnover": {
                                    "type": "float"
                                },
                                "currentYearTurnoverRate": {
                                    "type": "float"
                                },

                            },

                            {
                                "yearEndDate": {"type": "integer",
                                                "minLength": 13},
                                "reportType": {
                                    "type": "number",
                                    "anyOf": [
                                        {"type": "number", "reportType": 12},
                                        {"type": "number", "reportType": 9},
                                        {"type": "number", "reportType": 6},
                                        {"type": "number", "reportType": 1}
                                    ]},
                                "businessCate": {
                                    "type": "string",
                                    "minLength": 4
                                },
                                "currency": {
                                    "type": "string",
                                    "minLength": 3
                                },
                                "currentYearTurnover": {
                                    "type": "float"
                                },
                                "currentYearTurnoverRate": {
                                    "type": "float"
                                },
                            }
                        ]

                    }
                }
            },

        }

    }
}
