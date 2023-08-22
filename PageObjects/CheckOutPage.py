from selenium.webdriver.common.by import By


class CheckOutPage:
    itemTitles = (By.XPATH, "//div[@class='card h-100']")   # for -->> self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    checkoutButtonPrimary = (By.CSS_SELECTOR, "a[class*='btn-primary']")      #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    checkoutButtonSecond = (By.XPATH, "//button[@class='btn btn-success']")  #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.itemTitles)

    def checkOutButton1(self):
        return self.driver.find_element(*CheckOutPage.checkoutButtonPrimary)

    def checkOutButton2(self):
        return self.driver.find_element(*CheckOutPage.checkoutButtonSecond)






