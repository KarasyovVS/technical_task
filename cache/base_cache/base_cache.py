from abc import ABC, abstractmethod


class BaseCache(ABC):
    """
    Abstract class which includes a number of abstract methods to work with
    cache.

    Methods
    -------
    save_in_cache(path_to_file, data)
        Saves some data in cache.
    get_from_cache(path_to_file)
        Gets some data from cache.
    clear_cache(path_to_file)
        Deletes the cache file from cache by the name of the file.
    """

    @abstractmethod
    def save_in_cache(self, path_to_file, data):
        """
        Saves data in cache.

        Method depends on the specific implementation, so it must be
        implemented in inheritor class.
        """

        pass

    @abstractmethod
    def get_from_cache(self, path_to_file):
        """
        Gets data from cache.

        Method depends on the specific implementation, so it must be
        implemented in inheritor class.
        """

        pass

    @abstractmethod
    def clear_cache(self, path_to_file):
        """
        Deletes the cache file from cache by the name of the file.

        Method depends on the specific implementation, so it must be
        implemented in inheritor class.
        """
        pass
