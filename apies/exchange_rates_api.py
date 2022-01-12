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
    _endpoint : str
        Exchange Rates API endpoint, which provides specific functionality.

    Methods
    -------
    send_exchange_rate_request(base, *symbols)
        Forms a dictionary of parameters and passes it with '_key' variable
        to the 'send_get_request' method.
    """

    _key = os.environ.get("ACCESS_KEY")

    def __init__(self, endpoint: str, scheme: str, host: str, api_version: str):
        """
        Constructs all the necessary attributes for the ExchangeRatesApi object.

        Parameters
        ----------
        endpoint : str
            Exchange Rates API endpoint, which provides specific functionality.
        scheme : str
            Host scheme.
        host : str
            Base API host to work with.
        api_version : str
            Version of using API.
        """

        super().__init__(scheme=scheme, host=host, api_version=api_version)
        self._endpoint = endpoint

    def send_exchange_rate_request(self, base: str, *symbols: str,
                                   status_code: int) -> dict:
        """
        Forms a dictionary of parameters and passes it with '_key' variable
        to the 'send_get_request' method.

        Parameters
        ----------
        base : str
            Base currency for comparison (three-letter currency code).
        *symbols : str
            A number of currencies for comparison with base one (three-letter
            currency code for each)
        status_code : int
            An expected status code of the response.

        Returns
        -------
        self.send_get_request(path=self._endpoint_and_key, params=params,
        status_code=status_code).json() : dict
            Dictionary with data taken from the response.
        """

        params = {"access_key": self._key, "base": base}
        if len(symbols):
            params["symbols"] = ",".join([symbol.upper() for symbol in symbols])
        return self.send_get_request(path=self._endpoint, params=params,
                                     status_code=status_code).json()
