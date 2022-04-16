import logging


class Logger(object):
    def __init__(self, file):
        if file:
            logging.basicConfig(
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.FileHandler(file),
                        logging.StreamHandler()
                        ]
                    )
        else:
            logging.basicConfig(
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.StreamHandler()
                        ]
                    )

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    def exec_function(self, level, *params):
        func_map = {
            "info": self.logger.info,
            "warning": self.logger.warning,
            "error": self.logger.error,
            "critical": self.logger.critical,
            "debug": self.logger.debug,
        }
        return func_map.get(level)(*params)

    def log(self, level, msg):
        self.exec_function(level, msg)

    def set_level(self, level):
        func_map = {
            "info": logging.INFO,
            "warning": logging.WARNING,
            "error": logging.ERROR,
            "critical": logging.CRITICAL,
            "debug": logging.DEBUG,
        }
        self.logger.setLevel(func_map.get(level))
