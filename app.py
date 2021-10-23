from flask import Flask, request, render_template, url_for, redirect 
from datetime import datetime
import json
import requests

'''
#receives directions for multiple routes
params = {
'key': 'AIzaSyDtmwf9U6VVRuSqS2aYz6ymhdJKHq9Fl3w',
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
'key': 'AIzaSyDtmwf9U6VVRuSqS2aYz6ymhdJKHq9Fl3w',
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
        print(form_data)
        x=form_data.get('Origin')
        y=form_data.get('Destination')
    
        x=x.replace(' ','+')
        y=y.replace(' ','+')
        print(x,y)

        #receives directions for multiple routes
        params = {
        'key': 'AIzaSyDtmwf9U6VVRuSqS2aYz6ymhdJKHq9Fl3w',
        'origin': x,
        'destination': y,'alternatives':'true'
        }
        url ='https://maps.googleapis.com/maps/api/directions/json?'
        response = requests.get(url,params)
        print(response.status_code == 200)
        print(response.text)
        result = json.loads(response.text)

        print('123')
        routes=result.get('routes')
        print(routes)
        l=len(routes)
        forone=routes[0].get('summary')

        print(l)

        if l==1:
            print("There is only one route available via",routes[0].get('summary'))
        

        #print(routes[0][2].get('steps'))
        if l!=1:
            for i in range(l):
                legs=routes[i].get('legs')
                print('1')
                print(legs)
                print('2')
                steps = legs[0].get('steps')
                print('3')
                print(steps)
                (print('4'))
                

                l1=[]
                
                
                for x in steps:
                    
                    latlng=x.get('end_location')
                    #print(latlng)
                    #print(latlng.values())
                    lat,lng=latlng.get('lat'),latlng.get('lng')
                    #print(lat,lng)
                    

                    #reverse geocode
                    params = {
                    'key': 'AIzaSyDtmwf9U6VVRuSqS2aYz6ymhdJKHq9Fl3w',
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
                print(l1)

                 

        return render_template('result.html',form_data = form_data,l=l,forone=forone)
 
  


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

'''
@app.route('/', methods=['POST'])
def my_form_post():
    Variable = request.form['variable']
    return render_template('style.html')
'''

'''
@app.route('/map')
def index():
    return render_template('result.html')
'''
   

