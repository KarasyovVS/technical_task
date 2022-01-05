import json
import os

from framework.base_cache.base_cache import BaseCache
from cache_folder_path import CacheFolderPath


class JSONCache(BaseCache):

    CACHE_PATH = CacheFolderPath.CACHE_FOLDER_PATH
    CACHE_NAME = CacheFolderPath.CACHE_FOLDER_NAME

    def save_in_cache(self, path_to_file, data):
        with open(self.CACHE_PATH + path_to_file, "w") as cache_file:
            json.dump(data, cache_file)

    def get_from_cache(self, path_to_file):
        with open(self.CACHE_PATH + path_to_file) as cache_file:
            return json.load(cache_file)

    def clear_cache(self, path_to_file):
        os.remove(self.CACHE_PATH + path_to_file)

    def check_cache_folder(self):
        return os.path.exists(self.CACHE_PATH)

    def make_cache_folder(self):
        os.mkdir(self.CACHE_NAME)
