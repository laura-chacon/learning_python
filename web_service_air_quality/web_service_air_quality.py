import falcon
import json

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': 'I\'ve always been more interested in the future than in the past.',
            'author': 'Grace Hopper'
        }
        resp.body = json.dumps(quote)

# That creates your WSGI application and aliases it as api. 
# WSGI: Interface between web servers and web applications or frameworks for the Python programming language.
api = falcon.API()
# Adds a route between /quote and class QuoteResorce. This class will handle requests for the given URI.
api.add_route('/quote', QuoteResource())
