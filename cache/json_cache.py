import json
import os

from cache.base_cache.base_cache import BaseCache
from cache_folder_path import CacheFolderPath


class JSONCache(BaseCache):
    """
    Implementation of cache class which works with cache JSON files.

    Attributes
    ----------
    _cache_path : str
        Full os cache folder path.
    _cache_name : str
        Cache folder name.

    Methods
    -------
    save_in_cache(path_to_file, data)
        Serialize data as JSON file in cache.
    get_from_cache(path_to_file)
        Deserialize data from JSON file from cache.
    clear_cache(path_to_file)
        Deletes the cache file from cache by the path to file.
    """
    _cache_path = CacheFolderPath.cache_folder_path
    _cache_name = CacheFolderPath.cache_folder_name

    def __init__(self):
        """Creates a cache folder if it is missing."""

        if not os.path.exists(self._cache_path):
            os.mkdir(self._cache_name)

    def save_in_cache(self, path_to_file: str, data: dict):
        """
        Serialize data as a JSON file in cache.

        Parameters
        ----------
        path_to_file : str
            Path to file to put data.
        data : dict
            A data object to put in cache.

        Returns
        -------
        None
        """

        with open(os.path.join(self._cache_path, path_to_file), "w") as \
                cache_file:
            json.dump(data, cache_file)

    def get_from_cache(self, path_to_file: str) -> dict:
        """
        Deserialize data from a JSON file from cache.

        Parameters
        ----------
        path_to_file : str
            Path to file to get data from.

        Returns
        -------
        json.load(cache_file) : dict
            Value of specific cached response.
        """

        with open(os.path.join(self._cache_path, path_to_file)) as cache_file:
            return json.load(cache_file)

    def clear_cache(self, path_to_file: str):
        """
        Deletes the cache file from cache by the path to file.

        Parameters
        ----------
        path_to_file : str
            Path to file to delete.

        Returns
        -------
        None
        """

        os.remove(os.path.join(self._cache_path, path_to_file))
