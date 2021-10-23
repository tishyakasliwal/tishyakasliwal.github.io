
'''
import urllib
from urllib.request import urlopen

def main():
# open a connection to a URL using urllib2
   webUrl = urllib2.urlopen("https://maps.googleapis.com/maps/api/directions/json?origin=H8MW%2BWP%20Kolkata%20Indi&destination=GCG2%2B3M%20Kolkata%20India&alternatives=true&key=AIzaSyDtmwf9U6VVRuSqS2aYz6ymhdJKHq9Fl3w")
  
#get the result code and print it
   print "result code: " + str(webUrl.getcode()) 
  
# read the data from the URL and print it
   data = webUrl.read()
   print data

if __name__ == "__main__":
  main()



link = 'http://www.somesite.com/details.pl?urn=2344'
f = urlopen(link)           
myfile = f.read()  
print (myfile)
'''
'''
import json
import requests



params = {
'key': 'AIzaSyDtmwf9U6VVRuSqS2aYz6ymhdJKHq9Fl3w',
'origin': 'Sector+60+Noida+India',
'destination': 'Sector+21+Noida+India','alternatives':'false'
}
url ='https://maps.googleapis.com/maps/api/directions/json?'
response = requests.get(url,params)
print(response.status_code == 200)
print(response.text)
result = json.loads(response.text)
'''

'''
l=[]
for i in result["routes"]:
    x=i['legs']
    for z in x:
        print(z)
        if z=="start_location" or x=="end_location":
            print("Yes")
            l.append(x.values())
print(l)
'''

'''
params = {
'key': 'AIzaSyDtmwf9U6VVRuSqS2aYz6ymhdJKHq9Fl3w',
'latlng': '28.6058509,77.36835239999999'
}
url ='https://maps.googleapis.com/maps/api/geocode/json?'
response = requests.get(url,params)
print(response.status_code == 200)
print(response.text)
result = json.loads(response.text)



for i in (result['results']):
    l=i['address_components']
    break
print(l[2]['long_name'])



{"plus_code" : {"compound_code" : "J949+88 Noida, Uttar Pradesh, India","global_code" : "7JWVJ949+88"},
   "results" : [
      {
         "address_components" : [
            {"long_name" : "33", "short_name" : "33","types" : [ "premise" ]},
            
            {"long_name" : "Block A","short_name" : "Block A", "types" : [ "political", "sublocality", "sublocality_level_2" ]},
            
            {"long_name" : "Sector 60","short_name" : "Sector 60", "types" : [ "political", "sublocality", "sublocality_level_1" ]},

            {
               "long_name" : "Noida",
               "short_name" : "Noida",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "Ghaziabad",
               "short_name" : "Ghaziabad",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "Uttar Pradesh",
               "short_name" : "UP",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "India",
               "short_name" : "IN",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "201301",
               "short_name" : "201301",
               "types" : [ "postal_code" ]
            }
         ],
         '''
from flask import Flask, request, render_template, url_for, redirect 
from datetime import datetime
import json
import requests

#receives directions for multiple routes
params = {
        'key': 'AIzaSyDtmwf9U6VVRuSqS2aYz6ymhdJKHq9Fl3w',
        'origin': 'Sector+60+Noida',
        'destination': 'Sector+21+Noida','alternatives':'true'
        }
url ='https://maps.googleapis.com/maps/api/directions/json?'
response = requests.get(url,params)
print(response.status_code == 200)
print(response.text)
result = json.loads(response.text)
