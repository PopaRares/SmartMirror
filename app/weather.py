from app import Config
import requests


def getWeatherNow(location_key):
    URL = Config.WEATHER_URL + 'currentconditions/v1/' + location_key
    PARAMS = {'apikey': Config.WEATHER_API_KEY}

    data = requests.get(url=URL, params=PARAMS).json()
    return data


def getForecast(location_key):
    URL = Config.WEATHER_URL + 'forecasts/v1/hourly/12hour/' + location_key
    PARAMS = {'apikey': Config.WEATHER_API_KEY, 'metric': True}

    data = requests.get(url=URL, params=PARAMS).json()
    return data


def getLocation():
    ip = requests.get('https://api.ipify.org').text
    URL = Config.WEATHER_URL + 'locations/v1/cities/ipaddress'
    PARAMS = {'apikey': Config.WEATHER_API_KEY, 'q': ip}

    data = requests.get(url=URL, params=PARAMS).json()
    return data
