## weatherCrawler API

This is a simple API for requesting weather data from DarkSky.net. 

Data gathered is in JSON format and can be easily handeled depending on your needs.

In order to use the API, you will need to request a free a key from https://darksky.net/

## Example

This example shows how to use the API. 

```
key = "<Put your key here>"

setKey(key)
longitude, latitude = fetchCurrentPosition()
data = getForecast(longitude, latitude, "celsius")

print(data['currently'])
```

