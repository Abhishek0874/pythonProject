"""
#Note : if its a class variable u need to call it by class variable,
#if its  a instance variable like in defu have to call it by self.variable
# The below is the code withhow we optimized the code
from selenium.webdriver.common.by import By
from test_pageobj.CheckoutPage import CheckOutPage

class HomePage:

    def __init__(self,driver):
        self.driver = driver

    # self.driver.find_element(By.CSS_SELECTOR, " a[href*='shop']").click()
    shop = (By.CSS_SELECTOR,  " a[href*='shop']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
"""

# The below is the actual code after optimization this is how ur code should look
from selenium.webdriver.common.by import By
from test_pageobj.CheckoutPage import CheckOutPage

class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR,  " a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name = 'name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    successmsg = (By.CLASS_NAME, 'alert-success')
    gender = (By.ID, "exampleFormControlSelect1")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkbox).click()

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit).click()

    def getMessage(self):
        return self.driver.find_element(*HomePage.successmsg).text

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)