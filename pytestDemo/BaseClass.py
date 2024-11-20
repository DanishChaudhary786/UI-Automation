import inspect
import logging
class BaseClass:
    def getLogger(self, loggerName):
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        fileHandler.setFormatter(logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s"))
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger