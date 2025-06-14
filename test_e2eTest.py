import time

from pyTestAutomationFramework.pageObjects.LoginPage import LoginPage
from pyTestAutomationFramework.pageObjects.ProductPage import ProductPage


def test_e2e(browserInstance):
    driver= browserInstance
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    loginPage=LoginPage(driver)
    loginPage.login()
   ## productPage=ProductPage(driver)
   ## productPage.selectProduct("Sauce Labs Backpack")
