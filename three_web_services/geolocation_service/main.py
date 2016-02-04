import falcon, geolocation_service

api = application = falcon.API()
geolocation_service = geolocation_service.Resource()

api.add_route('/location/countries/{country}/cities/{city}', geolocation_service)
