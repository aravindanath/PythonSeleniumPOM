import time

from pageObjects.HomePage import HomePage
from pageObjects.SignInPage import SignInPage
from pageObjects.ProductListingPage import ProductListingPage
from utilities.BaseClass import BaseClass
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class PLP_TC_01(BaseClass):

    def test_SignIn(self):
        driver = Chrome(ChromeDriverManager().install())
        driver.get("https://amazon.in")
        log = self.getLogger()
        hp = HomePage(driver)
        plp = ProductListingPage(driver)
        log.info(driver.title)
        hp.searchField().send_keys("watch")
        hp.searchButton().click()
        plp.primeCheckBox().click()
        driver.execute_script("arguments[0].scrollIntoView();", plp.brandCb())
        plp.timexCb().click()
        log.info(driver.title)
        time.sleep(3)


        # title = sign.signPageTitle().text
        # print(title)




t = PLP_TC_01()
t.test_SignIn()

