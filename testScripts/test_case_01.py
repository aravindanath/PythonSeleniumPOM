import time

from pageObjects.HomePage import HomePage
from pageObjects.SignInPage import SignInPage
from utilities.BaseClass import BaseClass
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import pytest

# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_SignIn(self):
        driver = Chrome(ChromeDriverManager().install())
        driver.get("https://amazon.in")
        log = self.getLogger()
        hp = HomePage(driver)
        log.info(driver.title)
        # hp.pinCode().send_keys("560037")
        hp.searchField().send_keys("iphone")

        # hp.startShopping().click()
        sign = SignInPage(driver)
        # sign.mobileNumField().send_keys("134513454")

        sign.singIn().click()
        time.sleep(3)


        # title = sign.signPageTitle().text
        # print(title)




t = TestOne()
t.test_SignIn()

