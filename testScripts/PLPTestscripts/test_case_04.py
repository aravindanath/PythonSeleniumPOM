import time


from pageObjects.HomePage import HomePage
from pageObjects.SignInPage import SignInPage
from pageObjects.ProductListingPage import ProductListingPage
from utilities.BaseClass import BaseClass
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class SIN_TC_01(BaseClass):

    def test_SignIn(self):
        driver = Chrome(ChromeDriverManager().install())
        driver.get("https://amazon.in")
        log = self.getLogger()
        sg = SignInPage(driver)
        log.info(driver.title)
        sg.singIn().click()
        time.sleep(3)
        log.info(driver.title)
        sg.needHelpLink().click()
        time.sleep(3)
        # log.info("Forget passsword link is displayed?",sg.forgotPassLink().is_displayed())
        assert sg.forgotPassLink().is_displayed() == True



        # title = sign.signPageTitle().text
        # print(title)




t = SIN_TC_01()
t.test_SignIn()

