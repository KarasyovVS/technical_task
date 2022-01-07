import os

from apies.base_api.base_api import BaseAPI


class ExchangeRatesApi(BaseAPI):
    """
    Exchange Rates API class

    ...

    Attributes
    ----------
    __key : str
        API key for requests access (obtained from the environment
        variable named 'ACCESS KEY').
    __exchange_rates_api_url : str
        Exchange Rates API base URL.
    __exchange_rates_api_base_path : str
        Exchange Rates API base currency path (prefix).
    __exchange_rates_api_symbols_path : str
        Exchange Rates API symbols path (prefix)
    endpoint_and_key : str
        A part of Exchange Rates API path.


    Methods
    -------
    send_exchange_rate_request(base, *symbols)
        Forms a path and passes it to the 'send_get_request' method.
    get_status_code()
        Returns the status code from the '_response' attribute after
        get-request is made.
    get_info_from_json()
        Returns the json as a dict object from the '_response' attribute after
        get-request is made.
    get_url()
        Returns '__exchange_rates_api_url' variable.
    """

    __key = os.environ.get("ACCESS_KEY")
    __exchange_rates_api_url = "http://api.exchangeratesapi.io/v1"
    __exchange_rates_api_base_path = "&base="
    __exchange_rates_api_symbols_path = "&symbols="

    def __init__(self, endpoint: str):
        """
        Constructs all the necessary attributes for the ExchangeRatesApi object.

        Parameters
        ----------
        endpoint : str
            Exchange Rates API endpoint, which provides specific functionality.
        """

        super().__init__(self.__exchange_rates_api_url)
        self.endpoint_and_key = "{api_endpoint}?access_key={api_key}".format(
            api_endpoint=endpoint, api_key=self.__key)

    def send_exchange_rate_request(self, base: str, *symbols: str):
        """
        Forms a path and passes it to the 'send_get_request' method.

        Parameters
        ----------
        base : str
            Base currency for comparison (three-letter currency code).
        *symbols : str
            A number of currencies for comparison with base one (three-letter
            currency code for each)

        Returns
        -------
        None
        """

        symbols_path = ""
        if len(symbols) > 0:
            symbols_path = "{api_path}{symbols}".format(
                api_path=self.__exchange_rates_api_symbols_path,
                symbols=",".join([symbol.upper() for symbol in symbols]))
        request_path = "{endpoint_and_key}{api_path}{base}{symbols_path}".\
            format(endpoint_and_key=self.endpoint_and_key,
                   api_path=self.__exchange_rates_api_base_path,
                   base=base, symbols_path=symbols_path)
        super().send_get_request(request_path)

    def get_status_code(self) -> int:
        """
        Returns the status code from the '_response' attribute after
        get-request is made.

        Returns
        -------
        _response.status_code : int
            Value of response status code.
        """

        return self._response.status_code

    def get_info_from_json(self) -> dict:
        """
        Returns the JSON as a dict object from the '_response' attribute after
        get-request is made.

        Returns
        -------
        _response.json() : dict
            JSON as a 'dict' python object.
        """

        return self._response.json()

    def get_url(self) -> str:
        """
        Returns '__exchange_rates_api_url' variable value.

        Returns
        -------
        __exchange_rates_api_url : str
            Returns '__exchange_rates_api_url' variable value.
        """

        return self.__exchange_rates_api_url
