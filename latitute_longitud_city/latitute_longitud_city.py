import sys, os.path
from geopy.geocoders import Nominatim

if len(sys.argv) > 2:
    city = sys.argv[1]
    country = sys.argv[2]
    geolocator = Nominatim()
    location = geolocator.geocode(city + " " + country)
    if location is None:
        print location[1]
    else:
        print "invalid value"
else:
    print "invalid number of arguments"
