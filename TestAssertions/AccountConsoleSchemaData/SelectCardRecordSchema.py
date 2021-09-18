SelectCardRecordSchema = {  # required表示数据里必须有这2个字段"msg", "code"
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
            "type": "string",
            "pattern": r"^\d{6}$"
        },
        "data": {
            "type": "array",
            "items": [
                {
                    "cardId": {
                        "type": "string",
                        "pattern": "^[A-Za-z0-9]+$"
                    },
                    "userId": {
                        "type": "string",
                        "pattern": "^[A-Za-z0-9]+$"
                    },
                    "openId": {
                        "type": "string",
                        "pattern": "^[A-Za-z0-9]+$"
                    },
                    "cardType": {
                        "type": "string",
                        "pattern": r"^\d{4}$"
                    },
                    "cardSide": {
                        "type": "number",
                        "pattern": "^[0-9]*$"
                    },
                    "url": {
                        "type": "string",
                        "pattern": r"[^\s]*"
                    },
                    "cardNo": {
                        "type": "string",
                        "pattern": r"(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)"
                    },
                    "cardName": {
                        "type": "string",
                        "pattern": r"^[\u4E00-\u9FA5A-Za-z0-9]+$"
                    },
                    "cardAuthority": {
                        "type": "string"
                    },
                    "cardLastNamePinyin": {
                        "type": "string",
                        "pattern": r"^[A-Z]+$"
                    },
                    "cardNamePinyin": {
                        "type": "string",
                        "pattern": r"^[A-Z]+$"
                    },
                    "cardSex": {
                        "type": "string",
                        "oneOf": [
                            {"type": "string", "multipleOf": "男"},
                            {"type": "string", "multipleOf": "女"}
                        ]
                    },
                    "cardNation": {
                        "type": "string",
                        "pattern": r"^[\u4E00-\u9FA5A-Za-z0-9]+$"
                    },
                    "cardAddress": {
                        "type": "string",
                        "pattern": r"^[\u4E00-\u9FA5A-Za-z0-9]+$"
                    },
                    "cardBirth": {
                        "type": "string",
                        "pattern": r"^\d{4}-\d{1,2}-\d{1,2} "
                    },
                    "result": {
                        "type": "string",
                        "pattern": r"^\d{6}$"
                    },
                    "lastTime": {
                        "type": "number",
                        "pattern": r"^\d{13}$"
                    },
                    "createTime": {
                        "type": "number",
                        "pattern": r"^\d{13}$"
                    },
                    "updateTime": {
                        "type": "number",
                        "pattern": r"^\d{13}$"
                    },
                }
            ]
        }
    }
}
