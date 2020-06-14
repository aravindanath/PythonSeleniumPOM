from selenium.webdriver.common.by import By


class SignInPage:

    def __init__(self, driver):
        self.driver = driver

    singInButton = (By.XPATH,"//span[text()='Hello, Sign in']")
    signPageTitle =(By.XPATH,"//*[contains(text(),'Sign In / Sign Up')]")
    mobileNumField =(By.XPATH,"//input[@id='loginfirst_mobileno']")
    useOtpButton = (By.XPATH,"//button[contains(text(),'USE OTP')]")
    createAccountTitle =(By.XPATH,"//h2[contains(text(),'Create Account')]")
    emailTextField=(By.CSS_SELECTOR,"#reg_email")
    firstnameTextField=(By.CSS_SELECTOR,"#reg_firstname")
    lastnameTextField=(By.CSS_SELECTOR,"#reg_lastname")
    pwdTextField=(By.CSS_SELECTOR,"#register_pwd")
    confirm_pwdTextField=(By.CSS_SELECTOR,"#register_confirm_pwd")
    EnterOTPTextField=(By.CSS_SELECTOR,".singalotpcol.logotp.ng-untouched.ng-pristine.ng-invalid")
    verifyButton=(By.XPATH,"//button[contains(text(),'verify')]")
    needHelp =(By.XPATH,"//span[contains(text(),'Need help?')]")
    forgotPass = (By.XPATH,"//a[contains(text(),'Forgot Password')]")


    def signPgTitle(self):
       return self.driver.find_element(*SignInPage.signPageTitle)

    def mobileNumberField(self):
       return self.driver.find_element(*SignInPage.mobileNumField)

    def singIn(self):
       return self.driver.find_element(*SignInPage.singInButton)

    def needHelpLink(self):
       return self.driver.find_element(*SignInPage.needHelp)

    def needHelpLink(self):
        return self.driver.find_element(*SignInPage.needHelp)

    def forgotPassLink(self):
        return self.driver.find_element(*SignInPage.forgotPass)


