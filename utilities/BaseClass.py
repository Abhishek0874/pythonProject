import inspect
import logging
import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup1")
class BaseClass:

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 6)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger
