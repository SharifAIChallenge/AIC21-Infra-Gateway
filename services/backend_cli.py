import requests
from gateway.settings import BACKEND_URL

backend_address = BACKEND_URL + '/event/push'

class BackendCli:
    @staticmethod
    def send_event(data):
        try:
            requests.post(backend_address, json=data)
            return True
        except requests.exceptions.RequestException as e:
            return False
