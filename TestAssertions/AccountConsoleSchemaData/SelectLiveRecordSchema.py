SelectLiveRecordSchema = {  # required表示数据里必须有这2个字段"msg", "code"
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
                    "liveId": {
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
                    "videoUrl": {
                        "type": "string",
                        "pattern": r"[a-zA-z]+://[^\s]*"
                    },
                    "cardNo": {
                        "type": "string",
                        "pattern": r"(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)"
                    },
                    "cardName": {
                        "type": "string",
                        "pattern": r"^[\u4E00-\u9FA5A-Za-z0-9]+$"
                    },
                    "result": {
                        "type": "string",
                        "pattern": r"^\d{6}$"
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
