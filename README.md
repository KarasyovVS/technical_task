# Technical task

## Description

This application is designed for realization "CurrencyClient" class which 
includes objects of cache class (JSONCache) and api class (ExchangeRateApi). 
Object of the "CurrencyClient" provides several methods, such as:
- set_interval (sets the cache update time);
- get_interval (returns current cache update time);
- get_currency (looks for the presence of a response of user request in the 
  cache and its 
  relevance; if the response is in the cache, but is out of date - a 
  new request to the api is initialized; the same happens if the response is 
  not in the cache);
- clear_cache (deletes the cache file by its name).

## Preparations

- Put the key (token for http://api.exchangeratesapi.io) as 
the environment variable named "ACCESS_KEY".
- Install the "requirements.txt" dependencies using command "pip install -r 
requirements.txt".

## Running smoke tests

Run smoke tests using the command "pytest -m smoke" or using Dockerfile 
("docker build ." -> "docker run -e "ACCESS_KEY=[your access key]" 
[image_number]").

### NOTES:
1. Cached responses have filenames formatted as "[base_currency]-[args_currency]
.json".
2. "Exchange Rates API for free" subscription plan provides hourly updates o 
   exchange rates, that is why by default  function currency_client in 
   conftest.py file passes CurrencyClient instance attribute to tests with
   requests frequency to API equal to 60 minutes 
