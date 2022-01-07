import pytest

from clients.currency_client import CurrencyClient


@pytest.fixture()
def currency_client():
    """Method is used to pass CurrencyClient instance attribute to tests."""

    client = CurrencyClient(minutes=60)
    yield client
