"""
The below is the code whic we have optimized with how we optimized
from selenium.webdriver.common.by import By
from test_pageobj.ConfirmPage import ConfirmPage

class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    # driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    ProductTitle = (By.XPATH, "//div[@class='card h-100']")
    #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    checkOut2 = (By.XPATH, "//button[@class='btn btn-success']")

    def getProductTitles(self):
        return self.driver.find_elements(*CheckOutPage.ProductTitle)

    def getCheckOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkOut).click()

    def getCheckOutItem2(self):
        self.driver.find_element(*CheckOutPage.checkOut2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
"""
# The below is the code after optimization this is how the code should look
from selenium.webdriver.common.by import By
from test_pageobj.ConfirmPage import ConfirmPage

class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    ProductTitle = (By.XPATH, "//div[@class='card h-100']")
    checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut2 = (By.XPATH, "//button[@class='btn btn-success']")

    def getProductTitles(self):
        return self.driver.find_elements(*CheckOutPage.ProductTitle)

    def getCheckOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkOut).click()

    def getCheckOutItem2(self):
        self.driver.find_element(*CheckOutPage.checkOut2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
