import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        self.driver.implicitly_wait(4)
        homepage = HomePage(self.driver)        #using POM class to initiate driver object
        homepage.shopItems().click()
        #self.driver.find_element(By.XPATH, "//a[contains(.,'Shop')]").click()  # using regular expression to get xpath
        checkOutPage = CheckOutPage(self.driver)
        AllProducts = checkOutPage.itemTitles()
        #AllProducts = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in AllProducts:
            productname = product.find_element(By.XPATH, "div/h4/a").text
            if productname == 'iphone X':
                product.find_element(By.XPATH, "div/button").click()

        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        checkOutPage.checkoutButtonPrimary().click()
        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        checkOutPage.checkoutButtonSecond().click()
        #self.driver.find_element(By.ID, "country").send_keys("Uni")
        confirmPage = ConfirmPage(self.driver)
        confirmPage.country().send_keys("Uni")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "United Kingdom")))
        #self.driver.find_element(By.LINK_TEXT, "United Kingdom").click()
        confirmPage.selectCountry().click()
        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirmPage.finalCountry().click()
        #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        confirmPage.countrySubmit().click()
        message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in message

