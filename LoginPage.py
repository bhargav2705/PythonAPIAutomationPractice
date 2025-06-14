###self is an instance of class variable. Its life is entire class and can be used within the entire class
### * is the operator which breaks down/unpacks the tuple and seperates locator and notation at run time
###in the test_e2eTest.py class we can see that the driver instance is passed and the same will be instatiated using self.driver=driver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_input=(By.ID,"user-name")
        self.password=(By.NAME,"password")
        self.loginBtn=(By.XPATH,".//input[@type='submit']")

    def login(self):
        self.driver.find_element(*self.username_input).send_keys("standard_user")
        self.driver.find_element(*self.password).send_keys("secret_sauce")
        self.driver.find_element(*self.loginBtn).click()
