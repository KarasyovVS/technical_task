import os

from apies.base_api.base_api import BaseAPI


class ExchangeRatesApi(BaseAPI):
    """
    Exchange Rates API class

    Attributes
    ----------
    _key : str
        API key for requests access (obtained from the environment
        variable named 'ACCESS KEY').
    _endpoint_and_key : str
        A part of Exchange Rates API path.

    Methods
    -------
    send_exchange_rate_request(base, *symbols)
        Forms a dictionary of parameters and passes it with '_endpoint_and_key'
        variable to the 'send_get_request' method.
    """

    _key = os.environ.get("ACCESS_KEY")

    def __init__(self, endpoint: str):
        """
        Constructs all the necessary attributes for the ExchangeRatesApi object.

        Parameters
        ----------
        endpoint : str
            Exchange Rates API endpoint, which provides specific functionality.
        """

        super().__init__(scheme="http", host="api.exchangeratesapi.io",
                         api_version="v1")
        self._endpoint_and_key = "{api_endpoint}?access_key={api_key}".format(
            api_endpoint=endpoint, api_key=self._key)

    def send_exchange_rate_request(self, base: str, *symbols: str,
                                   status_code: int):
        """
        Forms a dictionary of parameters and passes it with '_endpoint_and_key'
        variable to the 'send_get_request' method.

        Parameters
        ----------
        base : str
            Base currency for comparison (three-letter currency code).
        *symbols : str
            A number of currencies for comparison with base one (three-letter
            currency code for each)
        status_code : int
            An expected status code or the response.

        Returns
        -------
        super().send_get_request(path=self._endpoint_and_key, params=params,
        status_code=status_code) : dict
            Dictionary with data taken from the response.
        """

        params = {"base": base}
        if len(symbols):
            params["symbols"] = ",".join([symbol.upper() for symbol in symbols])
        return super().send_get_request(path=self._endpoint_and_key,
                                        params=params, status_code=status_code)
