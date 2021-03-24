import requests
from gateway.settings import BACKEND_URL

backend_url = BACKEND_URL
auth = ('user', 'pass')


class BackendCli:
    @staticmethod
    def send_event(data):
        try:
            requests.post(backend_url, json=data)
            return True
        except requests.exceptions.RequestException as e:
            return False
