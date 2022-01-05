import pytest

from tests.clients.currency_client import CurrencyClient


@pytest.fixture()
def currency_client():
    client = CurrencyClient(minutes=60)
    yield client
