import time
from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from pageObjects.SignInPage import SignInPage
from pageObjects.ProductListingPage import ProductListingPage
from pageObjects.CustomerService import CustomerServicePage
from utilities.BaseClass import BaseClass
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class ORD_TC_01(BaseClass):
    @pytest.mark.run
    def test_orderpage_A(self):
        driver = self.lauchBrowser()
        driver.get("https://amazon.in")
        log = self.getLogger()
        log.info("User is verifying orderpage title")
        cs = CustomerServicePage(driver)
        cs.hamBurger().click()
        time.sleep(2)
        cs.customerSerButton().click()
        time.sleep(2)
        pg = cs.orderPgTitle().text
        print("Page Title: ",pg)
        log.info("Page Title: "+ pg)
        i = 10
        try:
            x =i/0
        except:
            log.error('NUMBER CANT DIVIDE BT ZERO')
        assert cs.orderPgTitle().text == "Hello. What can we help you with?"


#
# ord =ORD_TC_01()
# ord.test_orderpage_A()

#
# t = SIN_TC_01()
# t.test_SignIn()

