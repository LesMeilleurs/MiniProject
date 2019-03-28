from flask import Flask, request, jsonify
import json
import requests
from pprint import pprint
import requests_cache
from cassandra.cluster import Cluster


requests_cache.install_cache('air_api_cache', backend='sqlite', expire_after=36000)
# cache file air_api_cache.sqlite 
# data stored in cache will expire after 36000s

cluster = Cluster(['cassandra'])
session = cluster.connect()
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py') # API_Key storage

air_url_template = 'https://api.breezometer.com/air-quality/v2/current-conditions?lat={lat}&lon={lng}&key={API_KEY}'

# @ welcome page
@app.route('/')
def welcome():
    name = request.args.get("name", "World")
    return('<h1>Hello, {}!</h1>'.format(name))

# get air quality data resource from external API
@app.route('/airqualitychart', methods=['GET'])
def airchart():
    my_latitude = request.args.get('lat', '51.52369')  #altitude
    my_longitude = request.args.get('lng', '-0.0395857') #longtitude
    air_url = air_url_template.format(lat=my_latitude, lng=my_longitude, API_KEY=app.config['MY_API_KEY'])
    resp = requests.get(air_url)
    if resp.ok:
        resp = requests.get(air_url)
        # pprint(resp.json())
        result = jsonify(resp.json()) #resp.json() is a dict obj. 
        return result
    else:
        print(resp.reason)
        return("false!")

# get data from Cassandra database
@app.route('/airqualitychart/<datetime>')
def profile(datetime):
    rows = session.execute("""Select * From airquality.Data WHERE datetime = '{}' Allow Filtering""".format(datetime))
    # indicate the result in webpage in json format.
    # ALLOW FILTERING is essential!
    for data in rows:
        # return('<h1>The air quality index at the time {} is {}</h1>'.format(datetime, data.aqi))
        temp = {}
        temp[datetime] = data.aqi
        result = jsonify(temp)
        return(result)
    return('<h1>The datetime {} has no aqi information!</h1>')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
