# Technical task

## Description

This application is designed for realization "CurrencyClient" class which 
includes objects of cache class (JSONCache) and api class (ExchangeRateApi). 
Object of the "CurrencyClient" provides several methods, such as:
- set_interval (sets the cache update time);
- get_interval (returns current cache update time);
- get_currency (looks for the presence of a user request in the cache and its 
  relevance; if the user's request is in the cache, but is out of date - a 
  new request to the api is initialized; the same happens if the user's 
  request is not in the cache);
- clear_cache (deletes the cache file by its name)

## Preparations

- Put the key (token for http://api.exchangeratesapi.io) as 
the environment variable named "ACCESS_KEY".
- Install the "requirements.txt" dependencies using command "pip install -r 
requirements.txt".

## Running smoke tests

Run smoke tests using the command "pytest -m smoke" or using Dockerfile.
