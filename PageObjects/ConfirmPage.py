from selenium.webdriver.common.by import By


class ConfirmPage:

    country = (By.ID, "country")                                #self.driver.find_element(By.ID, "country").send_keys("Uni")
    selectCountry = (By.LINK_TEXT, "United Kingdom")            #self.driver.find_element(By.LINK_TEXT, "United Kingdom").click()
    finalCountry = (By.XPATH, "//div[@class='checkbox checkbox-primary']") #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    submit = (By.XPATH, "//input[@type='submit']")              #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def __init__(self, driver):
        self.driver = driver

    def countryName(self):
        return self.driver.find_element(*ConfirmPage.country)

    def countrySelect(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def countryFinal(self):
        return self.driver.find_element(*ConfirmPage.finalCountry)
    def countrySubmit(self):
        return self.driver.find_element(*ConfirmPage.submit)



