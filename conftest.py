import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


###Request is a common option to read details from the cli
###Config is used to read the parameters like browser etc from cli.
###pytest test_e2eTest.py --browser_name chrome
##Register the options--use addoption

def pytest_addoption(parser):
        parser.addoption(
            "--browser_name",
            action="store",
            default="chrome",
            help="Browser selection for instantiation",
        )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # service_obj = Service("C:\\Users\\UU33GU\\PycharmProjects\\pythonAutomationPractice\\chromedriver.exe")
     #driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(4)
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
       # service_obj = Service("C:\\Users\\UU33GU\\PycharmProjects\\pythonAutomationPractice\\chromedriver.exe")
       # driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(4)
    yield driver ###Before the test execution
    driver.close() ###Post function def_e2etest execution this is called
