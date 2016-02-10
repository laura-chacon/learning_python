import falcon, requests, sys, os.path, json
from geopy.geocoders import Nominatim

class Resource(object):

    def on_get(self, req, resp, country, city):
        payload = {'country': country, 'city': city}
        r = requests.get("http://127.0.0.1:8001/location/"+ str(country) +"/"+ str(city))
        json_data = json.loads(r.text)
        latitude = json_data['latitude']
        longitude = json_data['longitud']
        r = requests.get("http://127.0.0.1:8002/air_quality/"+ str(latitude)+"/"+ str(longitude))
        resp.body = json.dumps(r.content)
        resp.status = falcon.HTTP_200
