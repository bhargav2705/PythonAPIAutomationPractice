from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self,driver):
        self.driver = driver
        self.products=(By.XPATH,".//a//div[@class='inventory_item_name ']")
        self.backpack = (By.XPATH, ".//button[contains(@id,'backpack')]")
    def selectProduct(self,productName):
        if productName.casefold in "backpack":
            self.driver.find_element(*self.backpack).click()

       ## productNameDetails=self.driver.find_element(*self.products).get_attribute("name")
        ##productName=productName.lower()
        ##for products in productNameDetails:
          ##  if productName in products:
             ##   self.driver.find_element(By.XPATH,"//button[contains(@id,'"+productName.slice(3)+"')]").click()







