import requests
import json
import sys

sys.tracebacklimit = 0

intro_text = """\033[96m
 __        __            _    _                   ___          __        
 \ \      / /___   __ _ | |_ | |__    ___  _ __  |_ _| _ __   / _|  ___  
  \ \ /\ / // _ \ / _` || __|| '_ \  / _ \| '__|  | | | '_ \ | |_  / _ \ 
   \ V  V /|  __/| (_| || |_ | | | ||  __/| |     | | | | | ||  _|| (_) |
    \_/\_/  \___| \__,_| \__||_| |_| \___||_|    |___||_| |_||_|   \___/ 
			\033[93mBy https://github.com/clivelewis \033[0m
_________________________________________________________________________
"""


class WeatherInfo:
    def __init__(self, city: str, current_temp: float, feels_like: float, additional_info: str):
        self.city = city
        self.current_temp = current_temp
        self.feels_like = feels_like
        self.additional_info = additional_info

    def print_info(self):
        print('It\'s currently {}°C in {}. Feels like {}°C. Additional info: {}'
              .format(round(self.current_temp), self.city, round(self.feels_like), self.additional_info))


class WeatherApi:
    API_KEY = "https://home.openweathermap.org/api_keys --- GET YOUR KEY HERE"
    CURRENT_WEATHER_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
    DAILY_WEATHER_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

    def get_current_weather(self, city):
        params = {
            "q": city,
            "appid": self.API_KEY,
            "units": "metric"
        }
        response = requests.get(self.CURRENT_WEATHER_API_ENDPOINT, params)
        json_object = json.loads(response.text)

        if json_object is None:
            raise Exception("WeatherAPI didn't return anything")
        elif json_object['cod'] != 200:
            raise Exception(json_object['message'])
        else:
            return self.convert_json_to_weather_object(json_object)

    def convert_json_to_weather_object(self, json_object):
        additional_info = ""
        for weather_info in json_object['weather']:
            if len(additional_info) > 0:
                additional_info = additional_info + ", " + weather_info['description']
            else:
                additional_info = weather_info['description']

        current_temp = json_object['main']['temp']
        feels_like = json_object['main']['feels_like']
        city = json_object['name']
        return WeatherInfo(city, current_temp, feels_like, additional_info)


print(intro_text)

locations = []

if len(sys.argv) > 1:
    locations = sys.argv[1:]
else:
    locations = ['Riga', 'Kiev']

weatherApi = WeatherApi()

for location in locations:
    try:
        weatherInfo = weatherApi.get_current_weather(location)
        weatherInfo.print_info()
    except: print("\033[91mCan't get weather info for location '{}'\033[0m".format(location))