from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time

"""
This class is the parent of all the pages.
It contains all the generic method and utilities.
"""


class BasePage:

    TIMEOUT = 30
    def __init__(self,driver):
        self.driver=driver

    def click_webelement(self,by_locator):
        WebDriverWait(self.driver,timeout=self.TIMEOUT).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self,by_locator,value):
        WebDriverWait(self.driver,timeout=self.TIMEOUT).until(EC.visibility_of_element_located(by_locator)).send_keys(value)

    def wait_for_presence_of_all_element(self,by_locator):
        return WebDriverWait(self.driver,timeout=self.TIMEOUT).until(EC.presence_of_all_elements_located(by_locator))

    def wait_for_presence_of_element(self,by_locator):
        return WebDriverWait(self.driver,timeout=self.TIMEOUT).until(EC.visibility_of_element_located(by_locator))

    def get_element_text(self,by_locator):
        return WebDriverWait(self.driver, timeout=self.TIMEOUT).until(EC.visibility_of_element_located(by_locator)).text

    def get_title(self,title):
        WebDriverWait(self.driver,timeout=self.TIMEOUT).until(EC.title_is(title))
        return self.driver.title

    def maximize_the_window(self):
        time.sleep(15)
        self.driver.maximize_window()