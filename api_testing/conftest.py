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
    """
    Pytest fixture to create a database by sending a GET request to the create-database endpoint.

    Returns:
        Response: The response object from the GET request.
    """
    return requests.get(f"{BASE_URL}/create-database")
    # OR
    # resp = requests.get(f"{BASE_URL}/create-database")
    # return resp

def random_data(length=10):
    """
    Generates a random string of the specified length.

    Args:
        length (int): The length of the random string to generate. Default is 10.

    Returns:
        str: A random string consisting of ASCII letters and digits.
    """
    return "".join(choices(string.ascii_letters + string.digits, k=length))


class APISession:
    """
    A class to manage API sessions and send requests to specified endpoints.

    Attributes:
        base_url (str): The base URL for the API.
    """

    def __init__(self, base_url):
        """
        Initializes the APISession with the given base URL.

        Args:
            base_url (str): The base URL for the API.
        """
        self.base_url = base_url

    def send_request(self, request_type="GET", endpoint="", data=None, params=None):
        """
        Sends an HTTP request to the specified endpoint.

        Args:
            request_type (str): The type of HTTP request (e.g., "GET", "POST"). Default is "GET".
            endpoint (str): The API endpoint to send the request to.
            data (str, optional): The data to send in the body of the request. Default is None.
            params (dict, optional): The URL parameters to send with the request. Default is None.

        Returns:
            Response: The response object from the HTTP request.
        """
        log.info(f"Sending request: {self.base_url}/{endpoint}")
        return requests.request(request_type, f"{self.base_url}/{endpoint}", data=data, params=params)