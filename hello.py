'''
import googlemaps 
from datetime import datetime
print("HELLO")
gmaps = googlemaps.Client(key='AIzaSyDtmwf9U6VVRuSqS2aYz6ymhdJKHq9Fl3w')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
print(geocode_result)
# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
print(reverse_geocode_result)
# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

<iframe
  width="600"
  height="450"
  style="border:0"
  loading="lazy"
  allowfullscreen
  src="https://www.google.com/maps/embed/v1/place?key=AIzaSyDtmwf9U6VVRuSqS2aYz6ymhdJKHq9Fl3w
    &q=Space+Needle,Seattle+WA">
</iframe>
'''
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from urllib.parse import urljoin

# The maps_key defined below isn't a valid Google Maps API key.
# You need to get your own API key.
# See https://developers.google.com/maps/documentation/timezone/get-api-key
API_KEY = "AIzaSyDtmwf9U6VVRuSqS2aYz6ymhdJKHq9Fl3w"
TIMEZONE_BASE_URL = "https://maps.googleapis.com/maps/api/directions/json?origin="


def timezone(origin, destination):
    url=TIMEZONE_BASE_URL+origin+'&destination='+destination+'&alternate=true&key='+API_KEY
    
    response = urllib.request.urlopen(url)

    result = json.load(response)
    
    return result

       


tz = timezone("Sector+60+Noida+India","Sector+21+Noida+India")
print(f"Timezone: {tz}")
