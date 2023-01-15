"""
--Selenium pyton framework implementation from scratch:
#Standars of writing selenium tests in framework ?
#Creating browser invocation fixtures in conftest.py ?
#Setting up base class to hold all common utlities ?
#Inheriting base class to all tests to remove fixture redundant code ?
#Passing command line options to select browser at run time ?
#Implementing page object mechanism ?
#Smarter way of returning pageobjects from navigation methods ?
#Creating selenium webdriver custom utilites in base class ?
#Parameterizing webdriver tests with multiple data sets ?
#Orgainizingdata from seperate data files and injecting into fixture at run time ?
#Implementing logging feature to webdriver tests ?
#Test execution html reporting ?
#Automatic screenshot capture on tests failure ?
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

from utilities.BaseClass import BaseClass

#@pytest.mark.usefixture("setup") or this usefixture can be given in class like
#given below in BaseClass as @pytest.mark.usefixture("setup") is stored i class BaseClass
class TestOne(BaseClass):

    def test_e2e(self):
        self.driver.find_element(By.CSS_SELECTOR, " a[href*='shop']").click()
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in products:

            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in successText
        self.driver.close()


























