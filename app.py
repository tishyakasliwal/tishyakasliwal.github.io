from flask import Flask, request, render_template, url_for, redirect 
from datetime import datetime
import json
import requests
import config 
import csv 
import pandas as pd

'''
#receives directions for multiple routes
params = {
'key':  config.API_KEY,
'origin': 'Sector+60+Noida+India',
'destination': 'Sector+21+Noida+India','alternatives':'true'
}
url ='https://maps.googleapis.com/maps/api/directions/json?'
response = requests.get(url,params)
print(response.status_code == 200)
print(response.text)
result = json.loads(response.text)
'''
'''
#reverse geocode
params = {
'key':  config.API_KEY,
'latlng': '28.6058509,77.36835239999999'
}
url ='https://maps.googleapis.com/maps/api/geocode/json?'
response = requests.get(url,params)
print(response.status_code == 200)
print(response.text)
resultt = json.loads(response.text)
'''
'''
#retreives only sector from resultt
for i in (resultt['results']):
    l=i['address_components']
    break
print(l[2]['long_name'])
'''

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        #print(form_data)
        x=form_data.get('Origin')
        y=form_data.get('Destination')
    
        x=x.replace(' ','+')
        y=y.replace(' ','+')
        
        api_key= config.API_KEY
        #receives directions for multiple routes
        params = {
        'key': config.API_KEY,
        'origin': x,
        'destination': y,'alternatives':'true'
        }
        url ='https://maps.googleapis.com/maps/api/directions/json?'
        response = requests.get(url,params)
        #print(response.status_code == 200)
        #print(response.text)
        result = json.loads(response.text)

        #url for embedding map

        map="https://www.google.com/maps/embed/v1/directions?key={}&origin={}&destination={}"
        html_map=map.format(api_key,x,y)
        #print(html_map)

       
        routes=result.get('routes')
        #print(routes)
        l=len(routes)
        forone=routes[0].get('summary')

        #print(l)

        if l==1:
            print("There is only one route available via",routes[0].get('summary'))
        

        #print(routes[0][2].get('steps'))
        if l!=1:
            safetylevels=[]
            for i in range(l):
                legs=routes[i].get('legs')
                #print('1')
                print(legs)
                #print('2')
                steps = legs[0].get('steps')
                #print('3')
                print(steps)
                #(print('4'))
                

                l1=[]
                
                
                for x in steps:
                    
                    latlng=x.get('end_location')
                    #print(latlng)
                    #print(latlng.values())
                    lat,lng=latlng.get('lat'),latlng.get('lng')
                    #print(lat,lng)
                    

                    #reverse geocode
                    params = {
                    'key':  config.API_KEY,
                    'latlng': str(lat)+','+ str(lng)
                    }
                    url ='https://maps.googleapis.com/maps/api/geocode/json?'
                    response = requests.get(url,params)
                    #print(response.status_code == 200)
                    #print(response.text)
                    resultt = json.loads(response.text)
                    
                    for m in (resultt['results']):
                        #print(m)
                        l=m['address_components']
                        #print(l)
                        break
                    
                    l1.append(l[2]['long_name'])
                #print(l1)
                s=[]
                col_list=['Sector ','Crime ','Population','Crime Level']
                r=pd.read_csv("Noida data.csv",usecols=col_list)
               
                for x in l1:
                    for i in r['Sector ']:
                        if x== "Sector "+ str(i):

                            
                            m=r.loc[r['Sector '] == i, 'Crime Level'].iloc[0]
                            
                            break

                            
                    
                    s.append(m)
                avg=sum(s)/len(s)
                safetylevels.append(avg)
            
            minimum=min(safetylevels)
            print(safetylevels)
            routeindex=safetylevels.index(minimum)
            print("The safest route is via",routes[routeindex].get('summary'))
            formultiple=routes[routeindex].get('summary')

                 

        return render_template('result.html',form_data = form_data,l=l,forone=forone,formultiple=formultiple,html_map=html_map)
 
  


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
