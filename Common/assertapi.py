def assert_data(response, code, msg):
    assert code == response.json().get("code")
    assert msg == response.json().get("msg")