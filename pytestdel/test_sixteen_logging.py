#in this we created a class in which all the logging code is stored so we can
#use it in which ever test case we want to to the logging for that test case
#by calling this class in that test case
import inspect
import logging

class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        #this is a method to get a object to ur logging feature, to print from which test case is ur log
        #if __name__ is not given it will print root not ut test file name

        fileHandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        #%()s - to print a value asctime to print time i.e timestamp
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        #filehandler object (Note:addhandler in which file to print, filehandler is the file)

        logger.setLevel(logging.DEBUG) #to what level u want to see in ur file
        return logger