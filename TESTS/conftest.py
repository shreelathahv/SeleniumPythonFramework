#creating a fixture and linking that to a file with test cases will optimise the script without reusing the basic codes.

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#to be able to select the browser at runtime, need to set the hook as below

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")         #to retrive command line key value
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        service_obj = Service("C:/Users/Vishwanath/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    elif browser_name == "firefox":
        service_obj = Service("C:/Users/Vishwanath/Downloads/geckodriver-v0.33.0-win-aarch64/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
        #gecko driver code
    elif browser_name == "IE":
        print("IE")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
