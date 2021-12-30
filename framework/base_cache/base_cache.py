from abc import ABC, abstractmethod


class BaseCache(ABC):

    @abstractmethod
    def save_in_cache(self, path_to_file, data):
        pass

    @abstractmethod
    def get_from_cache(self, path_to_file):
        pass

    @abstractmethod
    def clear_cache(self, path_to_file):
        pass
