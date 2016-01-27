import sys, os.path
from geopy.geocoders import Nominatim
#from geopy.exc import GeocoderTimedOut

if len(sys.argv) > 2:
    city_name = sys.argv[1]
    country_name = sys.argv[2]
    geolocator = Nominatim()
    location = geolocator.geocode(city_name + " " + country_name)
    print location[1]
    #except GeocoderTimedOut as e:
    #    print "input doesn't exist"
else:
    print "invalid number of arguments"
