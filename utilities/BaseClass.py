import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from configparser import ConfigParser

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select



@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('/Users/aravindanathdm/PycharmProjects/MarvelAutomationFramework/reports/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def acceptAlert(driver):
        al = driver.switch_to.alert
        print("Title:", al.text)
        al.accept()

    def dismissAlert(driver):
        al = driver.switch_to.alert
        print("Title:", al.text)
        al.dismiss()

    def mouseHover(driver,element):
        act = ActionChains(driver)
        act.move_to_element(element).perform()

    def actionClick(driver,element):
        act = ActionChains(driver)
        act.click(element).perform()

    def actionClickAndHold(driver,element):
        act = ActionChains(driver)
        act.click_and_hold(element).perform()

    def rightClick(driver, element):
        act = ActionChains(driver)
        act.context_click(element).perform()

    def dragAndDrop(driver, src, tgt):
        act = ActionChains(driver)
        act.drag_and_drop(src,tgt).perform()

    def doubleClick(driver, element):
        act = ActionChains(driver)
        act.double_click(element).perform()

    def takeScreenShot(driver,path):
        driver.save_screenshot(path)

    def selectDropdownByindex(element,index):
        sel = Select(element)
        sel.select_by_index(index)

    def selectDropdownByVal(element, value):
        sel = Select(element)
        sel.select_by_value(value)

    def selectDropdownByVisibleText(element, value):
        sel = Select(element)
        sel.select_by_visible_text(value)


    def deSelectDropdownByVal(element, value):
        sel = Select(element)
        sel.deselect_by_value(value)

    def deSelectDropdownByindex(element, index):
        sel = Select(element)
        sel.deselect_by_index(index)

    def deSelectDropdownByVisibleText(element, value):
        sel = Select(element)
        sel.deselect_by_visible_text(value)

    def deSelectAllValues(element):
        sel = Select(element)
        sel.deselect_all()


    def writeToIni(filePath,header,key,value):
        config = ConfigParser()
        config.add_section(header)
        config.set(header, key, value)
        with open(filePath, 'a') as dt:
            config.write(dt)

    def readData(header,key):
        config = ConfigParser()
        config.read("../testdata/data.ini")
        val = config.get(header,key)
        return val

    def scrollToElement(driver,element):
        driver.execute_script("arguments[0].scrollIntoView();", element)

    def scrollToEnd(driver):
        driver.execute_script("arguments[0].scrollHeight;")

    def highlightElement(driver,element,colour):
        driver.execute_script("arguments[0].style.border='6px solid " + colour + "'", element)

