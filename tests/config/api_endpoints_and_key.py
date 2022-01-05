import os


class APIEndpointsAndKey:

    KEY = os.environ.get("ACCESS_KEY")

    ENDPOINT = "/latest"
    SYMBOL_ENDPOINT = "/symbols"
