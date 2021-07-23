from jsonschema import draft7_format_checker, validate, SchemaError, ValidationError


def assert_data(code, msg, schema, jsonSchema):
    assert code == "000000"
    assert msg == "ok"
    try:
        validate(instance=jsonSchema, schema=schema, format_checker=draft7_format_checker)
    except SchemaError as e:
        return 1, f"验证模式schema出错：\n出错位置：{'--> '.join([i for i in e.path])}\n提示信息：{e.message}"
    except ValidationError as e:
        return 1, f"json数据不符合schema规定：\n出错字段：{'-->'.join([i for i in e.path])}\n提示信息：{e.message}"
    else:
        return 0, "success!"
