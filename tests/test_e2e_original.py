#end to end automation
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj = Service("C:\Program Files\chromedriver");
#driver = webdriver.Chrome(service=service_obj)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#chrome_options.add_argument("headless") #to run the code without any browser opening, code running in background
chrome_options.add_argument("--ignore-certificate-errors") # to ignore the errors while going to a webpage
# like site is not safe , site may be dangerous etc...
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Shop").click()
# regular exp : XPATH, "//a[contains(@href,'shop')]"   CSSSelector, "a[href*='shop']"
# driver.find_element(By.XPATH, "//app-card[1]//div[1]//div[2]//button[1]").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
# or XPATH, "//app-card-list//app-card//div[@class='card h-100']"
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    # or XPATH, "//app-card-list//app-card//div[@class='card h-100']//div/h4/a" full path
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
        #or XPATH, "//app-card-list//app-card//div[@class='card h-100']//div/button" full path
        # but as half path is located in line 29 therefore we can continue after that
#driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click() or below
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
# Note : in console if we dont have selector hub:
#        for XPATH $x("//button[@class='btn btn-success']")
#        for CSSSelector : $("button[class='btn btn-success']")
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in successText #for partial text use in for full text use ==
driver.close()
























