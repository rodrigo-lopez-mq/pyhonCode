#!/usr/bin/python
import os
import requests


def setKey(api_key=None):
    if api_key:
        os.environ['DARKSKY_KEY'] = api_key
    else:
        print("ERROR: Key not specified")
        return None
    return api_key


def getKey():
    api_key = os.getenv('DARKSKY_KEY', '')
    if api_key:
        return api_key
    else:
        print("ERROR: Key not found")
        return None


def getForecast(longitude, latitude, units="auto"):
    key = getKey()
    if(key == None):
        print("ERROR: Key not found")
        return None
    else:
        key = getKey()
    if units == "celsius":
        units = "?&units=si"
    elif units == "fahrenheit":
        units = "?&units=us"
    else:
        units = ""
    forecast_url = "https://api.darksky.net/forecast/"+key+"/"+str(latitude)+","+str(longitude)+units
    return requests.get(forecast_url).json()


def fetchCurrentPosition():
    data = requests.get('http://freegeoip.net/json/').json()
    longitude = data['longitude']
    latitude = data['latitude']
    return longitude, latitude


key = "9b57aee4f8a46306ea1b940ff31c1b5b"

setKey(key)
longitude, latitude = fetchCurrentPosition()
data = getForecast(longitude, latitude, "celsius")

print(data['currently'])