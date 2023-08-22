from selenium.webdriver.common.by import By


class HomePage:
    #self.driver.find_element(By.XPATH, "//a[contains(.,'Shop')]").click()
    #variable = (kind of locator, actual locator) -->> syntax of the POM
    shop = (By.XPATH, "//a[contains(.,'Shop')]")

    def __init__(self, driver):         #creating constructor to link the driver object to the test case file
        self.driver = driver

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)      #shop is a class variable so using classname.variable = HomePage.shop
        #using * helps to deserialise and read the tuple
