
from Pages.WeatherPage import WeatherPage
class Comparator:
    def compare_Ui_and_api_weather_detail(self,search_city,api_weather_detail,ui_weather_detail):
        assert search_city==api_weather_detail['name'],"searched city {} is not matched with API city name {} test case :: failed".format(search_city,api_weather_detail['name'])
        print("searched city {} is matched with API city name {} test case :: failed".format(search_city,api_weather_detail['name']))



