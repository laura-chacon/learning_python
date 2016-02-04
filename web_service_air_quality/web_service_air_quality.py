import falcon
import air_quality

api = application = falcon.API()

air_quality = air_quality.Resource()
api.add_route('/air_quality/countries/{country}/cities/{city}', air_quality)
