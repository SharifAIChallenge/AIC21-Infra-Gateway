import requests
from gateway.settings import BACKEND_URL


class BackendCli:
    @staticmethod
    def send_event(data):
        try:
            requests.post(BACKEND_URL, json=data)
            return True
        except requests.exceptions.RequestException as e:
            print(e)
            return False
