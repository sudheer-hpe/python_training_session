import pytest
import requests

BASE_URL = "http://localhost:8080"

@pytest.fixture
def create_database():
    return requests.get(f"{BASE_URL}/create-database")
    # OR
    # resp = requests.get(f"{BASE_URL}/create-database")
    # return resp


class APISession:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, request_type="GET", endpoint="", data=None, params=None):
        return requests.request(request_type, f"{self.base_url}/{endpoint}", data=data, params=params)
