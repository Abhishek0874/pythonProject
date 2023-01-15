
from selenium.webdriver.common.by import By


class CheckOutPage2:

    def __init__(self,product):
        self.product = product

    # driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    ProductId = (By.XPATH, "div/button")

    def getProductId(self):
        return self.product.find_elements(*CheckOutPage2.ProductId)

