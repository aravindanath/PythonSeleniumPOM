from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    search = (By.CSS_SELECTOR,"#twotabsearchtextbox")
    searchBtn = (By.XPATH,"//input[@type='submit']")
    pinCodeTextField = (By.CSS_SELECTOR,"#rel_pincode")
    startShoppingButton = (By.XPATH,"//button[contains(text(),'Start Shopping')]")
    signInLink = (By.XPATH,"//a[contains(text(),' Sign In ')]")
    signInToYourAddress = (By.XPATH,"//button[text()='Sign in to see Your Addresses']")
    mobileNumField = (By.CSS_SELECTOR,"#loginfirst_mobileno")

    singInButton = (By.XPATH, "//span[text()='Hello, Sign in']")




    # * will help in deSerelation > driver.find_elements_by_CSS_SELECTOR("#rel_pincode")
    def pinCode(self):
        return self.driver.find_element(*HomePage.pinCodeTextField)

    def startShopping(self):
        return self.driver.find_element(*HomePage.startShoppingButton)

    def signIn(self):
        return self.driver.find_element(*HomePage.signInLink)

    def signInYourAddress(self):
        return self.driver.find_element(*HomePage.signInToYourAddress)

    def mobileNumField(self):
        return self.driver.find_element(*HomePage.mobileNumField)

    def searchField(self):
        return self.driver.find_element(*HomePage.search)

    def searchButton(self):
        return self.driver.find_element(*HomePage.searchBtn)

    def singIn(self):
        return self.driver.find_element(*HomePage.singInButton)
