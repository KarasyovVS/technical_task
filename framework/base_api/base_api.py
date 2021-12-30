import requests


class BaseAPI:

    def __init__(self, url):
        self._URL = url

    def send_get_request(self, path=""):
        self._RESPONSE = requests.get(self._URL + path)
        print(self._URL + path)
