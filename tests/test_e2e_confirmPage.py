"""
import pytest
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from test_pageobj.HomePage import HomePage
from test_pageobj.CheckoutPage import CheckOutPage
from test_pageobj.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixture("setup") or this usefixture can be given in class like
# given below in BaseClass as @pytest.mark.usefixture("setup") is stored i class BaseClass
class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        #checkOutPage = CheckOutPage(self.driver)
        products = checkoutpage.getProductTitles()

        for product in products:

            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmpage = checkoutpage.getCheckOutItems()
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        checkoutpage.getCheckOutItem2()
        confirmPage = ConfirmPage(self.driver)
        #self.driver.find_element(By.ID, "country").send_keys("ind")
        confirmPage.getCountryNames()
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")
        #self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmPage.getCountryName()
        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirmPage.getCheckBox()
        #self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        confirmPage.getSubmit()
        #successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        successText = confirmPage.getSuccessMsg()
        assert "Success! Thank you!" in successText
        self.driver.close()
"""

# The below code is after all optimization this is how ur code should look

from selenium.webdriver.common.by import By
from test_pageobj.HomePage import HomePage
from test_pageobj.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("Getting all the product titles")
        products = checkoutpage.getProductTitles()

        for product in products:

            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        confirmpage = checkoutpage.getCheckOutItems()
        log.info("Entering country name as ind")
        checkoutpage.getCheckOutItem2()
        confirmPage = ConfirmPage(self.driver)
        confirmPage.getCountryNames()
        self.verifyLinkPresence("India")
        confirmPage.getCountryName()
        confirmPage.getCheckBox()
        confirmPage.getSubmit()
        successText = confirmPage.getSuccessMsg()
        assert "Success! Thank you!" in successText
        log.info("Text received from application is " + successText)
        self.driver.close()
