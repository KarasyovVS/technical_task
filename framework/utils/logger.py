import logging


class Logger(object):
    __logger = logging.getLogger("Logger")

    @staticmethod
    def info(message):
        Logger.__logger.info(msg=message)

    @staticmethod
    def error(message):
        Logger.__logger.error(msg=message)
