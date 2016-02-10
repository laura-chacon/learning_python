import falcon, gateway_service

api = application = falcon.API()
gateway_service = gateway_service.Resource()

api.add_route('/air_quality/countries/{country}/cities/{city}', gateway_service)
