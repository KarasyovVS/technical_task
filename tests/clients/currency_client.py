import datetime
import time

from tests.apies.exchange_rates_api import ExchangeRateApi
from tests.cache.json_cache import JSONCache
from tests.config.api_endpoint_and_token import APIEndpointAndKey
from tests.config.urls import URLs
from framework.utils.logger import Logger


class CurrencyClient(metaclass=):

    def __init__(self, days=0, seconds=0, microseconds=0, milliseconds=0,
                 minutes=0, hours=0, weeks=0):
        self.__INTERVAL = days, seconds, microseconds, milliseconds, minutes, \
                          hours, weeks
        self.__API_MANAGER = ExchangeRateApi(APIEndpointAndKey.ENDPOINT)
        self.__CACHE_MANAGER = JSONCache()

    def set_interval(self, days=0, seconds=0, microseconds=0, milliseconds=0,
                     minutes=0, hours=0, weeks=0):
        self.__INTERVAL = days, seconds, microseconds, milliseconds, minutes, \
                          hours, weeks

    def get_interval(self):
        return self.__INTERVAL

    def __send_request(self, base, *args):
        self.__API_MANAGER.send_exchange_rate_request(base, *args)
        Logger.info(URLs.EXCHANGE_RATE_API_URL +
                    APIEndpointAndKey.ENDPOINT + " - GET - " +
                    str(self.__API_MANAGER.get_status_code()) + ":")
        data = self.__API_MANAGER.get_info_from_json()
        Logger.info(self.__API_MANAGER.get_info_from_json()["rates"])
        return data

    def get_currency(self, *args, base="EUR"):
        if not self.__CACHE_MANAGER.check_cache_folder():
            self.__CACHE_MANAGER.make_cache_folder()
        filename = base + "-" + ",".join(args) + ".json"
        try:
            data = self.__CACHE_MANAGER.get_from_cache(filename)
            if time.time() - data["timestamp"] <= datetime.timedelta(
                    *self.__INTERVAL).total_seconds():
                Logger.info("Get cached data of {}".format(" - ").join(args)
                            + ":")
                Logger.info(data["rates"])
            else:
                data = self.__send_request(base, *args)
                self.__CACHE_MANAGER.save_in_cache(filename, data)
        except FileNotFoundError:
            data = self.__send_request(base, *args)
            self.__CACHE_MANAGER.save_in_cache(filename, data)
