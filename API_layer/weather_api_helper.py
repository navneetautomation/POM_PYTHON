import requests

class WeatherApiHelper():
    HEADERS = {'Content-Type': 'application/json'}

    def get_the_response(self,url):
        return requests.get(url,self.HEADERS)

    def response_format_in_json(self,response):
        return response.json()