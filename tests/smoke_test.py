import logging
import pytest

from clients.currency_client import CurrencyClient
from tests.smoke_data import IntervalCheckData


class TestSmoke:
    """
    A class of smoke tests of CurrencyClient main functionality.

    Methods
    -------
    test_currency_client(self, currency_client, data)
        The method checks the ability of CurrencyClient instance attribute to
        send get-requests, receive data, save it in cache and return it from
        cache, if it is still relevant.
    test_currency_client_clear_cache(currency_client, data)
        The method checks the ability of CurrencyClient instance attribute to
        clear the cache.
    test_currency_client_xfail(currency_client, data)
        The method checks the correct respond of CurrencyClient instance
        attribute to incorrect input data.
    test_currency_client_intervals_getter_and_setter(default_value,
    time_parameter)
        The method checks the ability of CurrencyClient instance attribute to
        get and set time intervals of requests frequency to API.
    """

    logger = logging.getLogger("TestSmoke")

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", [("RUB", "USD"), ("RuB", "uSd"), ()])
    def test_currency_client(self, currency_client, data):
        currency_client.get_currency(*data)

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", [("SEK", "BOB"), ("SEK", "BOB")])
    def test_currency_client_clear_cache(self, currency_client, data):
        currency_client.get_currency(*data)
        currency_client.clear_cache(*data)

    @pytest.mark.smoke
    @pytest.mark.xfail
    def test_currency_client_xfail(self, currency_client):
        currency_client.get_currency("wrong", "data")

    @pytest.mark.smoke
    @pytest.mark.parametrize("default_value, time_parameter",
                             IntervalCheckData.interval_check_smoke_data)
    def test_currency_client_intervals_getter_and_setter(self, default_value,
                                                         time_parameter):
        currency_client = CurrencyClient()
        assert currency_client.get_interval() == default_value
        self.logger.info("Currency client's get_interval function works "
                         "correctly")
        currency_client.set_interval(*time_parameter)
        assert currency_client.get_interval() == time_parameter
        self.logger.info("Currency client's set_interval function works "
                         "correctly")
