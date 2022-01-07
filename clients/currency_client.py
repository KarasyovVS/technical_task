import datetime
import logging
import sys
import time

from typing import Tuple

from apies.exchange_rates_api import ExchangeRatesApi
from cache.json_cache import JSONCache


class CurrencyClient:
    """
    A class of currency client to work with Exchange Rates API and cache.

    Attributes
    ----------
    endpoint : str
        An endpoint gor getting the latest exchange rates information.
    logger : class attribute of Logger class
        An attribute of Logger class for logging information.
    __interval : Tuple[int, int, int, int, int, int, int]
        A tuple with the same parameters as timedelta constructor.
    __api_manager : instance attribute of ExchangeRatesApi class
    __cache_manager : instance attribute of JSONCache class.


    Methods
    -------
    set_interval(days=0, seconds=0, microseconds=0, milliseconds=0,
                 minutes=0, hours=0, weeks=0)
        Set the interval of requests frequency to API.
    get_interval()
        Returns the current interval of requests frequency to API.
    __send_request(base, *args)
        Method uses __api_manager functionality to send get-request, log the
        results of the request and return them from JSON object to main method,
        if status code is 'success'(200). Otherwise, it interrupts the program
        execution.
    get_currency(*args, base="EUR")
        Method uses __cache_manager functionality to check the presence of
        cache folder, save response results in cache and get them from cache,
        if their 'timestamp' parameter is less than current time. It also
        forms cache filename, passes it to __send_request method and log user
        output information.
    clear_cache(*args, base="EUR")
        Forms cache filename and passes it to __cache_manager method of cache
        deleting.
    """

    endpoint = "latest"
    logger = logging.getLogger("CurrencyClient")

    def __init__(self, days=0, seconds=0, microseconds=0, milliseconds=0,
                 minutes=0, hours=0, weeks=0):
        """
        Constructs all the necessary attributes for the ExchangeRatesApi object.

        By default parameters equal to 0, that means that __interval value
        is equal to 0 too and every request renews the older one in cache.

        Parameters (same is timedelta constructor)
        ----------
        days : int, optional
        seconds : int, optional
        microseconds : int, optional
        milliseconds : int, optional
        minutes : int, optional
        hours : int, optional
        weeks : int, optional
        """

        self.__interval = days, seconds, microseconds, milliseconds, minutes,\
                          hours, weeks
        self.__api_manager = ExchangeRatesApi(self.endpoint)
        self.__cache_manager = JSONCache()

    def set_interval(self, days=0, seconds=0, microseconds=0, milliseconds=0,
                     minutes=0, hours=0, weeks=0):
        """
        Set the interval of requests frequency to API.

        By default parameters equal to 0, that means that __interval value
        is equal to 0 too and every request renews the older one in cache.

        Parameters (same is timedelta constructor)
        ----------
        days : int, optional
        seconds : int, optional
        microseconds : int, optional
        milliseconds : int, optional
        minutes : int, optional
        hours : int, optional
        weeks : int, optional

        Returns
        -------
        None
        """

        self.__interval = days, seconds, microseconds, milliseconds, minutes, \
                          hours, weeks

    def get_interval(self) -> Tuple[int, int, int, int, int, int, int]:
        """
        Returns the current interval of requests frequency to API.

        Returns
        -------
        __interval : Tuple[int, int, int, int, int, int, int]
            Current interval of requests frequency to API as a tuple of 7
            integers same as timedelta constructor.
        """

        return self.__interval

    def __send_request(self, base: str, *symbols: str) -> dict:
        """
        Method uses __api_manager functionality to send get-request, log the
        results of the request and return them from JSON object to main method,
        if status code is 'success'(200). Otherwise, it interrupts the program
        execution.

        Parameters
        ----------
        base : str
            Base currency for comparison (three-letter currency code).
        *symbols : str
            A number of currencies for comparison with base one (three-letter
            currency code for each)

        Returns
        -------
        __api_manager.get_info_from_json() : dict
            The dict value of JSON response.
        """

        self.__api_manager.send_exchange_rate_request(base, *symbols)
        if self.__api_manager.get_status_code() == 200:
            self.logger.info("{api_url_and_endpoint} - GET - 200:".format(
                api_url_and_endpoint="/".join([self.__api_manager.get_url(),
                                               self.endpoint])))
        else:
            self.logger.error("An error occurred, status code: {}".format(
                self.__api_manager.get_status_code()))
            sys.exit()
        return self.__api_manager.get_info_from_json()

    def get_currency(self, *symbols: str, base="EUR"):
        """
        Method uses __cache_manager functionality to check the presence of
        cache folder, save response results in cache and get them from cache,
        if their 'timestamp' parameter is less than current time. It also
        forms cache filename, passes it to __send_request method and log user
        output information.

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

        if not self.__cache_manager.check_cache_folder():
            self.__cache_manager.make_cache_folder()
        symbols = [arg.upper() for arg in symbols]
        filename = "{base}-{args}.json".format(base=base, args=",".join(
            symbols))
        try:
            data = self.__cache_manager.get_from_cache(filename)
            if time.time() - data["timestamp"] <= datetime.timedelta(
                    *self.__interval).total_seconds():
                self.logger.info("Get cached data of {}:".format(
                    " - ".join(symbols)))
                self.logger.info(data["rates"])
            else:
                data = self.__send_request(base, *symbols)
                self.logger.info(data["rates"])
                self.__cache_manager.save_in_cache(filename, data)
        except FileNotFoundError:
            data = self.__send_request(base, *symbols)
            self.logger.info(data["rates"])
            self.__cache_manager.save_in_cache(filename, data)

    def clear_cache(self, *symbols: str, base="EUR"):
        """
        Forms cache filename and passes it to __cache_manager method of cache
        deleting.

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

        filename = "{base}-{args}.json".format(base=base, args=",".join(
            symbols))
        self.__cache_manager.clear_cache(filename)
