from selenium.webdriver.common.by import By


class CustomerServicePage:

    def __init__(self, driver):
        self.driver = driver


    hamburgerMenu = (By.CSS_SELECTOR,"#nav-hamburger-menu")
    customerServiceButton= (By.XPATH,"(//a[text()='Customer Service'])[2]")
    orderPageTitle =(By.XPATH,"//h1[contains(text(),'What can we help you with?')]")
    searchBox =(By.CSS_SELECTOR,"#helpsearch")
    goBtn = (By.XPATH,"//input[@type='submit' and @class='a-button-input']")


    def hamBurger(self):
        return self.driver.find_element(*CustomerServicePage.hamburgerMenu)

    def customerSerButton(self):
        return self.driver.find_element(*CustomerServicePage.customerServiceButton)

    def orderPgTitle(self):
        return self.driver.find_element(*CustomerServicePage.orderPageTitle)

    def searchBoxField(self):
        return self.driver.find_element(*CustomerServicePage.searchBox)

    def goButton(self):
        return self.driver.find_element(*CustomerServicePage.goBtn)
