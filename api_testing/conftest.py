import requests

class APISession:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, request_type="GET", endpoint=""):
        return requests.request(request_type)
