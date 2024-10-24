import logging
import string
from random import choices

import pytest
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

BASE_URL = "http://localhost:8080"

@pytest.fixture
def create_database():
    return requests.get(f"{BASE_URL}/create-database")
    # OR
    # resp = requests.get(f"{BASE_URL}/create-database")
    # return resp

def random_data(length=10):
    return "".join(choices(string.ascii_letters + string.digits, k=length))


class APISession:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, request_type="GET", endpoint="", data=None, params=None):
        log.info(f"Sending request: {self.base_url}/{endpoint}")
        return requests.request(request_type, f"{self.base_url}/{endpoint}", data=data, params=params)
