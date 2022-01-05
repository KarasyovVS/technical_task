import pytest

from tests.clients.currency_client import CurrencyClient
from tests.smoke_data import SmokeData


class TestSmoke:

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", SmokeData.SMOKE_DATA)
    def test_currency_client(self, currency_client, data):
        currency_client.get_currency(*data)

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", SmokeData.CLEAR_CACHE_SMOKE_DATA)
    def test_currency_client_clear_cache(self, currency_client, data):
        currency_client.get_currency(*data)
        currency_client.clear_cache(*data)

    @pytest.mark.smoke
    @pytest.mark.xfail
    @pytest.mark.parametrize("data", SmokeData.WRONG_SMOKE_DATA)
    def test_currency_client_xfail(self, currency_client, data):
        currency_client.get_currency(*data)

    @pytest.mark.smoke
    @pytest.mark.parametrize("default_value, time_parameter",
                             SmokeData.INTERVAL_CHECK_SMOKE_DATA)
    def test_currency_client_intervals(self, default_value, time_parameter):
        currency_client = CurrencyClient()
        assert currency_client.get_interval() == default_value
        currency_client.set_interval(*time_parameter)
        assert currency_client.get_interval() == time_parameter
