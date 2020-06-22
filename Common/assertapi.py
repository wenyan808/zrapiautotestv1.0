def assert_data(response, code, msg):
    assert code == response.json().get("code")
    assert msg == response.json().get("msg")
    if "data" in response.json():
        assert response.json().get("data")