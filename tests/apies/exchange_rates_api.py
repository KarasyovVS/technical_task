from framework.base_api.base_api import BaseAPI
from tests.config.api_endpoints_and_key import APIEndpointsAndKey
from tests.config.paths import Paths
from tests.config.urls import URLs


class ExchangeRateApi(BaseAPI):

    def __init__(self, endpoint):
        super().__init__(URLs.EXCHANGE_RATE_API_URL)
        self.TOKEN_ENDPOINT = "{api_endpoint}?access_key={api_key}".format(
            api_endpoint=endpoint, api_key=APIEndpointsAndKey.KEY)

    def send_exchange_rate_request(self, base, *symbols):
        symbols_path = ""
        if len(symbols) > 0:
            symbols_path = Paths.EXCHANGE_RATES_API_SYMBOLS_PATH
            symbols_path += ",".join([symbol.upper() for symbol in symbols])
        path = self.TOKEN_ENDPOINT + Paths.EXCHANGE_RATES_API_BASE_PATH + base \
            + symbols_path
        super().send_get_request(path)

    def get_status_code(self):
        return self._RESPONSE.status_code

    def get_info_from_json(self):
        return self._RESPONSE.json()
