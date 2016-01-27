import sys, os.path, json
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
        data['latitude'] = location[1][0]
        data['longitud'] = location[1][1]
    print json.dumps(data, indent=4, sort_keys=True)
else:
    print "invalid number of arguments"
