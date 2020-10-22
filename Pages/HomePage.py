from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
import time

class HomePage(BasePage):

    #locators OR
    SUB_MENU_SYMBOL=(By.XPATH,"//a[@id='h_sub_menu']")
    WEATHER_OPTION=(By.XPATH,"//a[text()='WEATHER']")

    '''Constructor of the page class'''
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        time.sleep(15)
        self.driver.maximize_window()


    '''Page Actions for Home Page'''

    '''This method is used to get the title'''
    def get_home_page_title(self,title):
        return self.get_title(title)


