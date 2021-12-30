import logging


class Logger(object):
    __logger = logging.getLogger("Logger")
    __br = '<br>'
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d-%m-%y %H:%M:%S')

    @staticmethod
    def info(message):
        Logger.__logger.info(msg=message)
