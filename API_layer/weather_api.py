import pytest
from API_layer.weather_api_helper import WeatherApiHelper
from API_layer import constant as input

class TestWeatherApi(WeatherApiHelper):

    def get_the_weather_detail(self):
        url=input.URL
        response=self.get_the_response(url)
        if response.status_code == 200:
            print('Success!')
            print("Response is ::",response.text)
            json_response=self.response_format_in_json(response)
        elif response.status_code == 404:
            print('Not Found.')
            assert False

        return json_response