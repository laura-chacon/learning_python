import falcon, requests, sys, os.path, json
from geopy.geocoders import Nominatim

class Resource(object):

    def on_get(self, req, resp, country, city):
        geolocator = Nominatim()
        location = geolocator.geocode(city + " " + country)
        latitude = location[1][0]
        longitude = location[1][1]
        data = {'latitude': latitude, 'longitude': longitude}
        resp.body = json.dumps(data)
        resp.status = falcon.HTTP_200
