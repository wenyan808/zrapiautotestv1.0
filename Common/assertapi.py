def assert_data(response: object, code: object, msg: object) -> object:
    assert code == response.json().get("code")
    assert msg == response.json().get("msg")
