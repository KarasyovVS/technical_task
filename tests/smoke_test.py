import datetime
import logging
import pytest

from clients.currency_client import CurrencyClient


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
    test_currency_client_wrong_data(currency_client)
        The method checks the correct respond of CurrencyClient instance
        attribute using incorrect input data.
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
    def test_currency_client_wrong_data(self, currency_client):
        with pytest.raises(RuntimeError):
            currency_client.get_currency("wrong", "data")

    @pytest.mark.smoke
    def test_currency_client_intervals_getter_and_setter(self):
        currency_client = CurrencyClient()
        assert currency_client.get_interval() == datetime.timedelta()
        self.logger.info("Currency client's get_interval function works "
                         "correctly")
        interval = dict(days=9, seconds=8, microseconds=7, milliseconds=6,
                        minutes=5, hours=4, weeks=3)
        currency_client.set_interval(**interval)
        assert currency_client.get_interval() == datetime.timedelta(**interval)
        self.logger.info("Currency client's set_interval function works "
                         "correctly")
