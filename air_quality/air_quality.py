import sys, os.path, json, requests
from geopy.geocoders import Nominatim

if len(sys.argv) > 2:
    city = sys.argv[1]
    country = sys.argv[2]
    data = {}
    geolocator = Nominatim()
    location = geolocator.geocode(city + " " + country)
    if location is None:
        data['error'] = "invalid value"
    else:
        payload = {'lat': location[1][0], 'lon': location[1][1], 'key': '2eef42863d814355b3e7f5f0cbff2efb'}
        r = requests.get("http://api.breezometer.com/baqi/", params=payload)
        json_data = json.loads(r.text)
        data['air_quality_index'] = json_data['country_aqi']
        data['description']= json_data['country_description']
    print data
else:
    print "invalid number of arguments"
