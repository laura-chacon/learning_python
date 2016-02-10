import falcon, requests, sys, os.path, json
from geopy.geocoders import Nominatim

class Resource(object):

    def on_get(self, req, resp, latitude, longitude):
        print 1
        payload = {'lat': latitude, 'lon': longitude, 'key': '2eef42863d814355b3e7f5f0cbff2efb'}
        r = requests.get("http://api.breezometer.com/baqi/", params=payload)
        json_data = json.loads(r.text)
        country_aqi = json_data['country_aqi']
        country_description = json_data['country_description']
        data = {'air_quality_index' : country_aqi, 'description': country_description}
        resp.body = json.dumps(data)
        resp.status = falcon.HTTP_200
#<?xml version="1.0" encoding="UTF-8"?>
#<gpx version="1.1" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd" creator="geocoder.js"><wpt lat="25.7616798" lon="-80.1917902"><name></name></wpt><wpt lat="36.8745146" lon="-94.8774554"><name></name></wpt><wpt lat="36.3500355" lon="-104.7930509"><name></name></wpt><wpt lat="33.3992217" lon="-110.8687232"><name></name></wpt><wpt lat="40.6140514" lon="-86.1064885"><name></name></wpt><wpt lat="35.6914327" lon="-100.6381933"><name></name></wpt></gpx>
