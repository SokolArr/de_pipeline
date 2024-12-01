import logging
from datetime import datetime


class MyLogger:
    def __init__(self, log_level: str = "INFO"):
        self.log_level = log_level.upper()
        self.formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        self.datefmt = "%Y-%m-%d %H:%M:%S"

    def configure_logger(self, logger_name: str = __name__):
        self.logger = logging.getLogger(logger_name)
        self.set_log_level()
        self.configure_console_handler()

    def set_log_level(self):
        if self.log_level == "DEBUG":
            self.logger.setLevel(logging.DEBUG)
        elif self.log_level == "INFO":
            self.logger.setLevel(logging.INFO)
        elif self.log_level == "WARNING":
            self.logger.setLevel(logging.WARNING)
        elif self.log_level == "ERROR":
            self.logger.setLevel(logging.ERROR)
        elif self.log_level == "CRITICAL":
            self.logger.setLevel(logging.CRITICAL)
        else:
            self.logger.setLevel(logging.INFO)

    def configure_console_handler(self):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.logger.level)
        console_handler.setFormatter(self.formatter)
        self.logger.addHandler(console_handler)

    @property
    def debug(self):
        return self.logger.debug

    @property
    def info(self):
        return self.logger.info

    @property
    def warning(self):
        return self.logger.warning

    @property
    def error(self):
        return self.logger.error

    @property
    def critical(self):
        return self.logger.critical
