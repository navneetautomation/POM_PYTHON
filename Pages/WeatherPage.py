from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
import time

class WeatherPage(BasePage):

    #locators OR
    SUB_MENU_SYMBOL=(By.XPATH,"//a[@id='h_sub_menu']")
    WEATHER_OPTION=(By.XPATH,"//a[text()='WEATHER']")
    CITY_PIN_SEARCH_FIELD=(By.XPATH,"//input[@id='searchBox']")
    LIST_OF_CITY=(By.XPATH,"//div[@class='cityText']")
    WEATHER_DETAIL_CITY=(By.XPATH,"//div[@class='leaflet-popup-content']//span//b")
    CLOSE_ICON = (By.XPATH, "//a[@class='leaflet-popup-close-button']")

    '''Constructor of the page class'''
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        time.sleep(15)
        self.driver.maximize_window()


    '''Page Actions for weather Page'''

    '''This method is used to click the sub menu symbol'''
    def click_on_sub_menu_symbol(self):
        self.click_webelement(self.SUB_MENU_SYMBOL)

    '''This method is used to click the sub menu symbol'''
    def click_on_weather_option(self):
        self.click_webelement(self.WEATHER_OPTION)


    '''This method is used to search the city name '''
    def search_the_city(self,city_name):
        self.do_send_keys(self.CITY_PIN_SEARCH_FIELD,city_name)

    '''This method is used to verify the weather report of city...'''
    def verify_the_weather_detail_of_city(self):
        list_of_city=self.wait_for_presence_of_all_element(self.LIST_OF_CITY)
        for i in range(len(list_of_city)):
            if list_of_city[i].text == TestData.SEARCH_CITY:
                print("city has been added ::")
                list_of_city[i].click()
                weather_detail_list = self.wait_for_presence_of_all_element(self.WEATHER_DETAIL_CITY)
                time.sleep(2)
                detail_list = []
                for i in range(len(weather_detail_list)):
                    detail_list.append(weather_detail_list[i].text)
                time.sleep(5)
                print(detail_list)
                self.click_webelement(self.CLOSE_ICON)
                break
        return detail_list

