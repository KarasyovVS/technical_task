import pytest

from tests.apies.exchange_rates_api import ExchangeRateApi
from tests.cache.json_cache import JSONCache
from tests.clients.currency_client import CurrencyClient


class TestSmoke:
    pass

    @pytest.mark.smoke
    def test_currency_client(self):
        client = CurrencyClient(minutes=60)
        client.get_currency("RUB", "USD")
        client.get_currency("RUB", "USD")
        client.get_currency("JPY", "USD")
        client.get_currency("JPY", "USD")
        client.get_currency()
        client.get_currency("XXX", "YYY")
        assert False

    # @pytest.mark.smoke
    # def test_currency_client(self):
    #     client = CurrencyClient(minutes=5)
    #     client.get_currency()
    #     b = JSONCache()
    #     b.save_in_cache("cache/cache_file.json", {"line": 2, 3: 4})
    #     print(b.get_from_cache("cache/cache_file.json"))
    #     b.clear_cache("cache/cache_file.json")
    #     assert False

    # def test_cache(self):
    #     b = JSONCache()
    #     b.save_in_cache("cache_file.json", {"line": 2, 3: 4})
    #     print(b.get_from_cache("cache_file.json"))
    #     # b.clear_cache("cache_file.json")
    #     assert b.check_cache_folder()

    # def test_sth(self):
    #     a = ExchangeRateApi()
    #     a.get_exchange_rate_response("USD", "rub", "bTn")
    #     print(a.get_info_from_json())
    #     print(type(a.get_info_from_json()))
    #     print(a.get_status_code())
    #     assert False