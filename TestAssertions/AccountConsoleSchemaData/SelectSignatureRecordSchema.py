SelectSignatureRecordSchema ={  # required表示数据里必须有这2个字段"msg", "code"
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
                    "signatureUrl": {
                        "type": "string",
                        "pattern": r"[^\s]*"
                    },
                    "submitTime": {
                        "type": "number",
                        "pattern": r"^\d{13}$"
                    }
                }
            ]
        }
    }
}
