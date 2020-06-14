from selenium.webdriver.common.by import By


class ProductListingPage:

    def __init__(self, driver):
        self.driver = driver

    search = (By.CSS_SELECTOR,"#twotabsearchtextbox")
    primecb= (By.XPATH,"//i[@aria-label='Prime Eligible']")
    timex = (By.XPATH,"//span[text()='TIMEX']")
    brand = (By.XPATH,"//span[text()='Brand']")

    # * will help in deSerilation > driver.find_element_by_CSS_SELECTOR("#rel_pincode")
    def seachBox(self):
        return self.driver.find_element(*ProductListingPage.search)

    def primeCheckBox(self):
        return self.driver.find_element(*ProductListingPage.primecb)

    def timexCb(self):
        return self.driver.find_element(*ProductListingPage.timex)

    def brandCb(self):
        return self.driver.find_element(*ProductListingPage.brand)




