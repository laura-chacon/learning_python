import falcon, requests, sys, os.path, json
from geopy.geocoders import Nominatim

class Resource(object):

    def on_get(self, req, resp, country, city):
        geolocator = Nominatim()
        location = geolocator.geocode(city + " " + country)
        payload = {'lat': location[1][0], 'lon': location[1][1], 'key': '2eef42863d814355b3e7f5f0cbff2efb'}
        r = requests.get("http://api.breezometer.com/baqi/", params=payload)
        json_data = json.loads(r.text)
        country_aqi = json_data['country_aqi']
        country_description = json_data['country_description']
        data = {'air_quality_index' : country_aqi, 'description': country_description}
        resp.body = json.dumps(data)
        resp.status = falcon.HTTP_200
