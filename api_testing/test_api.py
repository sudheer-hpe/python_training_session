"""
This module contains test cases for API endpoints using pytest.

The tests include:
- Creating a database
- Adding entries to the database
- Retrieving the count of entries in the database
- Retrieving individual entries from the database

Classes:
    TestAPI: Contains test methods for various API endpoints.

Functions:
    create_database: Pytest fixture to create a database.
    random_data: Generates random data for testing.
    APISession: Class to manage API session and send requests.
"""

import json

import pytest

from api_testing.conftest import APISession, BASE_URL, random_data, log

count = 0


class TestAPI:
    """
    A class to test various API endpoints.
    """

    @pytest.mark.dependency(name="create_database")
    def test_create_database(self, create_database):
        """
        Test the database creation endpoint.

        Args:
            create_database (Response): The response object from the database creation request.
        """
        response = create_database
        assert response.status_code == 200, "Database Creation failed!!"
        assert (
            "Database created successfully" in response.text
        ), "Response text mismatch!!"

    @pytest.mark.dependency(depends=["create_database"])
    @pytest.mark.parametrize(
        "data",
        [
            ({"name": random_data(9), "value": random_data(4)}),
            ({"name": random_data(10), "value": random_data(7)}),
            ({"name": random_data(23), "value": random_data(89)}),
            ({"name": random_data(230), "value": random_data(151)}),
        ],
    )
    def test_add_entry(self, data):
        """
        Test the entry addition endpoint with various data.

        Args:
            data (dict): The data to be added to the database.
        """
        api_session = APISession(BASE_URL)
        endpoint = "entry"
        response = api_session.send_request("POST", endpoint, data=json.dumps(data))
        assert response.status_code == 200, f"Entry addition failed for data: {data}"
        assert (
            "Entry added successfully" in response.text
        ), f"Response text mismatch for data: {data}"

    @pytest.mark.dependency(depends=["create_database"])
    def test_get_count(self):
        """
        Test the count retrieval endpoint.
        """
        api_session = APISession(BASE_URL)
        endpoint = "length"
        response = api_session.send_request("GET", endpoint)
        assert response.status_code == 200, "Count retrieval failed!!"
        assert "count" in response.json(), "Response JSON doesn't contain 'count' key!!"
        global count
        count = response.json()["count"]
        log.info(f"Found {count} entries in the database.")

    @pytest.mark.dependency(depends=["create_database"])
    def test_get_entry(self):
        """
        Test the entry retrieval endpoint.
        """
        api_session = APISession(BASE_URL)
        endpoint = "entry"
        global count
        log.info(f"Retrieving {count} entries from the database.")
        for id_ in range(1, count + 1):
            endpoint_url = f"{endpoint}?id={id_}"
            response = api_session.send_request("GET", endpoint_url)
            assert response.status_code == 200, "Entry retrieval failed!!"
            assert id_ == response.json()["id"], "Response JSON mismatch!!"

    @pytest.mark.dependency(depends=["create_database"])
    def test_update_entry(self):
        """
        Test the entry update endpoint.
        """
        api_session = APISession(BASE_URL)
        endpoint = "entry"
        data = {"id": count, "name": random_data(5), "value": random_data(3)}
        response = api_session.send_request("PUT", endpoint, data=json.dumps(data))
        assert response.status_code == 200, f"Entry update failed for data: {data}"
        assert (
            "Entry updated successfully" in response.text
        ), f"Response text mismatch for data: {data}"

    @pytest.mark.dependency(depends=["create_database"])
    def test_delete_entry(self):
        """
        Test the entry deletion endpoint.
        """
        api_session = APISession(BASE_URL)
        endpoint = "entry"
        endpoint_url = f"{endpoint}?id={count}"
        response = api_session.send_request("DELETE", endpoint_url)
        assert response.status_code == 200, f"Entry deletion failed!!"
        assert (
            "Entry deleted successfully" in response.text
        ), f"Response text mismatch!!"