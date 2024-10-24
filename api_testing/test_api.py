from api_testing.conftest import APISession, BASE_URL


def test_create_database(create_database):
    response = create_database
    assert response.status_code == 200, "Database Creation failed!!"
    assert "Database created successfully" in response.text, "Response text mismatch!!"


def test_add_entry():
    api_session = APISession(BASE_URL)
    endpoint = "entry"
    response = api_session.send_request("POST", endpoint)
    assert response.status_code == 200, ""