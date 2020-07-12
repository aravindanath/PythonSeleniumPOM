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

class ORD_TC_03(BaseClass):

    def test_orderpage_A(self):
        driver = self.lauchBrowser()
        driver.get("https://google.com")
        log = self.getLogger()
        log.info("User is verifying orderpage title")



#
ord =ORD_TC_03()
ord.test_orderpage_A()

#
# t = SIN_TC_01()
# t.test_SignIn()

