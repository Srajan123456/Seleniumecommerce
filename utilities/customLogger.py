import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        path = "../logs/automation.log"
        filehandler = logging.FileHandler(path)
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger