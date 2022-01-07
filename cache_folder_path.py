import os


class CacheFolderPath:
    """A class with cache folder name and path."""

    cache_folder_name = "test_cache"
    cache_folder_path = os.path.join(os.path.dirname(os.path.abspath(
        __file__)), cache_folder_name)
