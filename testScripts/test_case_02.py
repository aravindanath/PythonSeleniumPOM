import time

from pageObjects.HomePage import HomePage
from pageObjects.SignInPage import SignInPage
from utilities.BaseClass import BaseClass
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


class TestOne(BaseClass):

    def test_SignIn(self):
        print("demo")
        #
        # hp = HomePage(self.driver)
        # # hp.pinCode().send_keys("560037")
        # hp.searchField().send_keys("iphone")
        #
        # # hp.startShopping().click()
        # sign = SignInPage(self.driver)
        # # sign.mobileNumField().send_keys("134513454")
        #
        # sign.singIn().click()
        # time.sleep(3)





# t = TestOne()
# t.test_SignIn()

