import datetime
import logging
import os
import time

from apies.exchange_rates_api import ExchangeRatesApi
from cache.json_cache import JSONCache


class CurrencyClient:
    """
    A class of currency client to work with Exchange Rates API and cache.

    Attributes
    ----------
    endpoint : str
        Exchange Rates API endpoint, which provides specific functionality.
    logger : class attribute of Logger class
        An attribute of Logger class for logging information.
    _interval : datetime.timedelta
        Current interval of requests frequency to API.
    _api_manager : instance attribute of ExchangeRatesApi class
    _cache_manager : instance attribute of JSONCache class.

    Methods
    -------
    set_interval(days=0, seconds=0, microseconds=0, milliseconds=0,
    minutes=0, hours=0, weeks=0)
        Sets the interval of requests frequency to API.
    get_interval()
        Returns the current interval of requests frequency to API.
    __send_request(base, *symbols, status_code=200)
        Method uses _api_manager functionality to send get-request and return
        the response from JSON object to main method.
    get_currency(*symbols, base="EUR")
        Method uses _cache_manager functionality to check the presence of
        cache folder, save response results in cache and get them from cache,
        if their 'timestamp' parameter is less than current time. Method passes
        cache filename to __send_request method and logs user output
        information.
    clear_cache(*symbols, base="EUR")
        Passes cache filename it to _cache_manager method of cache deleting.
    __prepare_filename_for_cache(base, symbols)
        Forms cache filename.
    """

    endpoint = "latest"
    logger = logging.getLogger("CurrencyClient")

    def __init__(self, days=0, seconds=0, microseconds=0, milliseconds=0,
                 minutes=0, hours=0, weeks=0):
        """
        Constructs all the necessary attributes for the ExchangeRatesApi object.

        By default, parameters are equal to 0, that means that _interval value
        is equal to 0 too and every request renews the older one in cache.

        Parameters (same as timedelta constructor parameters)
        ----------
        days : int
        seconds : int
        microseconds : int
        milliseconds : int
        minutes : int
        hours : int
        weeks : int
        """

        self._interval = datetime.timedelta(days, seconds, microseconds,
                                            milliseconds, minutes, hours, weeks)
        self._api_manager = ExchangeRatesApi(self.endpoint, os.environ.get(
            "SCHEME"), os.environ.get("HOST"), os.environ.get("API_VERSION"))
        self._cache_manager = JSONCache()

    def set_interval(self, days=0, seconds=0, microseconds=0, milliseconds=0,
                     minutes=0, hours=0, weeks=0):
        """
        Sets the interval of requests frequency to API.

        By default, parameters are equal to 0, that means that _interval value
        is equal to 0 too and every request renews the older one in cache.

        Parameters (same as timedelta constructor parameters)
        ----------
        days : int
        seconds : int
        microseconds : int
        milliseconds : int
        minutes : int
        hours : int
        weeks : int

        Returns
        -------
        None
        """

        self._interval = datetime.timedelta(days, seconds, microseconds,
                                            milliseconds, minutes, hours, weeks)

    def get_interval(self) -> datetime.timedelta:
        """
        Returns the current interval of requests frequency to API.

        Returns
        -------
        _interval : datetime.timedelta
            Current interval of requests frequency to API.
        """

        return self._interval

    def __send_request(self, base: str, *symbols: str, status_code=200) -> dict:
        """
        Method uses _api_manager functionality to send get-request and return
        the response from JSON object to main method.

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
        _api_manager.send_exchange_rate_request(base, *symbols,
        status_code=status_code) : dict
            The dict value of the JSON response.
        """

        return self._api_manager.send_exchange_rate_request(
            base, *symbols, status_code=status_code)

    def get_currency(self, *symbols: str, base="EUR"):
        """
        Method uses _cache_manager functionality to check the presence of
        cache folder, save response results in cache and get them from cache,
        if their 'timestamp' parameter is less than current time. Method passes
        cache filename to __send_request method and logs user output
        information.

        If the argument 'base' is passed, then the base currency for
        comparison is 'EUR'.

        Parameters
        ----------
        base : str, optional
            Base currency for comparison (three-letter currency code).
        *symbols : str
            A number of currencies for comparison with base one (three-letter
            currency code for each)

        Returns
        -------
        None
        """

        filename = self.__prepare_filename_for_cache(base=base,
                                                     symbols=symbols)
        try:
            data = self._cache_manager.get_from_cache(filename)
            if time.time() - data["timestamp"] <= \
                    self._interval.total_seconds():
                self.logger.info("Get cached data of {}:".format(
                    " - ".join(symbols)))
                self.logger.info(data["rates"])
            else:
                data = self.__send_request(base, *symbols)
                self.logger.info(data["rates"])
                self._cache_manager.save_in_cache(filename, data)
        except FileNotFoundError:
            data = self.__send_request(base, *symbols)
            self.logger.info(data["rates"])
            self._cache_manager.save_in_cache(filename, data)

    def clear_cache(self, *symbols: str, base="EUR"):
        """
        Passes cache filename to _cache_manager method of cache deleting.

        If the argument 'base' is passed, then the base currency for
        comparison is 'EUR'.

        Parameters
        ----------
        base : str, optional
            Base currency for comparison (three-letter currency code).
        *symbols : str
            A number of currencies for comparison with base one (three-letter
            currency code for each)

        Returns
        -------
        None
        """

        filename = self.__prepare_filename_for_cache(base=base,
                                                     symbols=symbols)
        self._cache_manager.clear_cache(filename)

    def __prepare_filename_for_cache(self, base: str, symbols: tuple) -> str:
        """
        Forms cache filename.

        Parameters
        ----------
        base : str
            Base currency for comparison (three-letter currency code).
        symbols : tuple
            A number of currencies for comparison with base one (three-letter
            currency code for each)

        Returns
        -------
        "{base}-{symbols}.json".format(base=base, symbols=",".join(symbols))
        : str
            Result filename.
        """

        symbols = [arg.upper() for arg in symbols]
        return "{base}-{symbols}.json".format(base=base,
                                              symbols=",".join(symbols))
