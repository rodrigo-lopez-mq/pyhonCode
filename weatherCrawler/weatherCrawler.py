#!/usr/bin/python

import requests

def forecast():
    # lat, lng = _check_lat_lng(lat, lng)
    # url = "https://api.darkskyapp.com/v1/forecast/%s/%s,%s" % (api_key, lat, lng)
    url = "https://api.darksky.net/forecast/9b57aee4f8a46306ea1b940ff31c1b5b/37.8267,-122.4233"
    print (requests.get(url).json())

# def location(place):
#     """Find the latitude and longitude for a location."""
#     map_key = mapquest()
#     if map_key == '':
#         raise Exception('No MAPQUEST_API_KEY found.')
#     results = mapq.latlng(place)
#     return (results['lat'], results['lng'])

print ("SUP")
#Client ID Client Sec
#dj0yJmk9V1hYTXg5Q1ZMcjFQJmQ9WVdrOVYydG9VVEJoTnpBbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD05MA--
#b0dd007bce9abbabdf7ecacf2a9c606c00748309

forecast()