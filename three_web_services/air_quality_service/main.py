import falcon, air_quality_service

api = application = falcon.API()
air_quality_service = air_quality_service.Resource()
api.add_route('/air_quality/{latitude}/{longitude}', air_quality_service)
