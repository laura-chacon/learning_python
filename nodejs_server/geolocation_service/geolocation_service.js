var express = require('express');
const http = require('http');
var app = express();
var geocoderProvider = 'google';
var httpAdapter = 'https';
var extra = {
    apiKey: 'AIzaSyASW_GofCX4xY2T_1dKn11tNcaluuMzWpU',
    formatter: 'gpx'
};
var geocoder = require('node-geocoder')(geocoderProvider, httpAdapter, extra);



app.get('/location/:country/:city', function(req,result) {
    var direction = req.params.country;
    var lat, lon;
    direction = direction.concat(" ", req.params.city);
    geocoder.geocode({'address': direction}, function(err, res) {
        lat = (res[38+245] + res[38+246] + res[38+247] + res[38+248] + res[38+249] + res[38+250]);
        lon = (res[38+262] + res[38+263] + res[38+264] + res[38+265] + res[38+266] + res[38+267]);

        result.send({latitude: lat, longitud: lon});
    });
}
       );
app.listen(8001);

/*
const http = require('http');
var url = require('url');
var geocoderProvider = 'google';
var geocoder = require('node-geocoder')(geocoderProvider, http, extra);

var express = require('express');
var app = express.createServer();

var extra = {
    apiKey: 'AIzaSyASW_GofCX4xY2T_1dKn11tNcaluuMzWpU',
    formatter: 'string'
};


http.createServer( (request, response) => {
    var url_parts = url.parse(request.url, true);
    var query = url_parts.query;
    console.log(query);
    var country = query["country"]
    var city = query["city"]
    var direction = country.concat(' ', city);
    geocoder.geocode(direction, function(err, res) {
        console.log(res["latitude"]);
    });



*/
