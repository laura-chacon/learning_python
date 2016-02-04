import falcon, requests, sys, os.path, json
from geopy.geocoders import Nominatim

class Resource(object):

    def on_get(self, req, resp, country, city):
        r = requests.get("http://127.0.0.1:8001/location/countries/"+ str(country) +"/cities/"+ str(city))
        json_data = json.loads(r.text)
        latitude = json_data['latitude']
        longitude = json_data['longitude']
        r = requests.get("http://127.0.0.1:8002/air_quality/"+ str(latitude)+"/"+ str(longitude))
        resp.body = json.dumps(r.content)
        resp.status = falcon.HTTP_200
