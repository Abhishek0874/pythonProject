import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from test_data.HomePageData import HomePageData
from test_pageobj.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):

    def test_submissionForm(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("first name is " + getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPassword().send_keys("123456")
        homePage.getCheckBox()
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.getSubmit()
        message = homePage.getMessage()
        print(message)
        assert ("Success" in message)
        self.driver.refresh()
        self.driver.close()

    # to call data from excel
    @pytest.fixture(params=HomePageData.getTestDataExcel("testcase2"))
    def getData(self, request):
        return request.param
"""
# to call data from HomePageData.py
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
"""

"""
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Abhishek")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)
driver.close()
"""