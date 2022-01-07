class SmokeData:
    """A class with data for smoke tests of CurrencyClient main
    functionality."""

    pos_smoke_data = [("RUB", "USD"), ("RuB", "uSd"), ()]
    clear_cache_smoke_data = [("SEK", "BOB"), ("SEK", "BOB")]
    neg_smoke_data = [("wrong", "data")]
    interval_check_smoke_data = [((0, 0, 0, 0, 0, 0, 0),
                                  (9, 8, 7, 6, 5, 4, 3))]
