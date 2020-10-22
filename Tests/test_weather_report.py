import pytest
from Tests.test_base import BaseTest
from Pages.HomePage import HomePage
from Config.config import TestData
from Pages.WeatherPage import WeatherPage
from API_layer.weather_api import TestWeatherApi
from Config.comparator import Comparator


class TestWeather(BaseTest,TestWeatherApi,Comparator):

    # def test_verify_the_title(self):
    #     self.HomePage=HomePage(self.driver)
    #     current_title=self.HomePage.get_title(TestData.TITLE_HOMEPAGE)
    #     assert current_title==TestData.TITLE_HOMEPAGE,"Title {} is not matching test cases :: failed".format(current_title)
    #     print("Title {} is matching test case passed".format(current_title))

    def test_verify_the_weather_detail(self):
        detail_api=self.get_the_weather_detail()
        self.WeatherPage=WeatherPage(self.driver)
        self.WeatherPage.click_on_sub_menu_symbol()
        self.WeatherPage.click_on_weather_option()
        self.WeatherPage.search_the_city(TestData.SEARCH_CITY)
        city_weather_detail_ui=self.WeatherPage.verify_the_weather_detail_of_city()
        self.compare_Ui_and_api_weather_detail(TestData.SEARCH_CITY,detail_api,city_weather_detail_ui)





