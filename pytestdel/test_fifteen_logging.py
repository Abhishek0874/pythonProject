"""
# Logging or Logs : logging levels
debug
Info
Warning
Error
Critical

"""
import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    #this is a method to get a object to ur logging feature, to print from which test case is ur log
    #if __name__ is not given it will print root not ut test file name

    fileHandler = logging.FileHandler('logfile.log')

    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    #%()s - to print a value asctime to print time i.e timestamp
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    #filehandler object (Note:addhandler in which file to print, filehandler is the file)

    logger.setLevel(logging.DEBUG) #to what level u want to see in ur file

    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")
# after u run this code logfile.log file is created in which all ur logs are saved.

"""
log-file output-
2023-01-09 06:37:21,659 : DEBUG : test_fifteen_logging : A debug statement is executed
2023-01-09 06:37:21,660 : INFO : test_fifteen_logging : Information statement
2023-01-09 06:37:21,660 : WARNING : test_fifteen_logging : Something is in warning mode
2023-01-09 06:37:21,660 : ERROR : test_fifteen_logging : A major error has happened
2023-01-09 06:37:21,660 : CRITICAL : test_fifteen_logging : Critical issue
"""







