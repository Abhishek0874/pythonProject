"""
The below is the code withhow we optimized the code
from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    #self.driver.find_element(By.ID, "country").send_keys("ind")
    CountryTitles = (By.ID, "country")
    #self.driver.find_element(By.LINK_TEXT, "India").click()
    CountryTitle = (By.LINK_TEXT, "India")
    #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    CheckBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    Submit = (By.CSS_SELECTOR, "[type='submit']")
    #self.driver.find_element(By.CLASS_NAME, "alert-success").text
    SuccessMsg = (By.CLASS_NAME, "alert-success")

    def getCountryNames(self):
        return self.driver.find_element(*ConfirmPage.CountryTitles).send_keys("ind")

    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.CountryTitle).click()

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.CheckBox).click()

    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.Submit).click()

    def getSuccessMsg(self):
        return self.driver.find_element(*ConfirmPage.SuccessMsg).text
"""
# The below is the actual code after optimization this is how ur code should look
from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    CountryTitles = (By.ID, "country")
    CountryTitle = (By.LINK_TEXT, "India")
    CheckBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    Submit = (By.CSS_SELECTOR, "[type='submit']")
    SuccessMsg = (By.CLASS_NAME, "alert-success")

    def getCountryNames(self):
        return self.driver.find_element(*ConfirmPage.CountryTitles).send_keys("ind")

    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.CountryTitle).click()

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.CheckBox).click()

    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.Submit).click()

    def getSuccessMsg(self):
        return self.driver.find_element(*ConfirmPage.SuccessMsg).text


