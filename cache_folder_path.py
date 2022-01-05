import os


class CacheFolderPath:

    CACHE_FOLDER_NAME = "cache"
    CACHE_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__)) + "/" + \
        CACHE_FOLDER_NAME + "/"
