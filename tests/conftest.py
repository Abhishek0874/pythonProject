import pytest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

#below conftest code is so that when u need to run program with chrome IE or firebox, etc. u
#can run by the keyvalue i.e chrome firefox, etc.
#code for cmd to run - py.test --browser_name chrome
#--browser_name can be anything eg: --browser_id , --startup , --runBrowser_name
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup1(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:\Program Files\chromedriver")
    #elif browser_name == "firefox":
        service_obj = Service("C:\Program Files\chromedriver")
        #firefox invocation Gecko Driver (code- driver=webdriver.Firefox(executable_path = ))
    #elif browser_name == "IE":
        service_obj = Service("C:\Program Files\chromedriver")
        #IE Driver
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver

