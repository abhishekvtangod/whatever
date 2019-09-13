var express = require('express');
var bodyParser = require('body-parser');
const fs = require('fs');
var fileOutputName = require('./data.json');
var cors = require('cors');
var axios = require('axios');
var app = express();
// configure body parser
app.use(cors());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 8080; // set our port

// create our router
var router = express.Router();

// middleware to use for all requests
router.use(function(req, res, next) {
  // do logging
  console.log('Something is happening.');
  next();
});

// test route to make sure everything is working (accessed at GET http://localhost:8080/api)
router.get('/', function(req, res) {
  res.header('Content-Type', 'application/json');
  res.send(fileOutputName);
});
let apiKaData;
let godownLat = 12.967195;
let godownlon = 80.127865;
router.get('/distance-cal', function(req, res) {
  let address;

  axios
    .get(
      `https://maps.googleapis.com/maps/api/geocode/json?address=${req.query.lat},${req.query.long}&key=AIzaSyCfQ0EjpxAe8P7UBFtQ74kxZIRZsEyL4G4`
    )
    .then(function(response) {
      // handle success
      apiKaData = response.data;
      address = apiKaData.results[0].formatted_address.split(' ').join('+');
    })
    .catch(function(error) {
      // handle error
      console.log(error);
    })
    .finally(function() {
      console.log(address);
      axios
        .get(
          `https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=Plot+No.60,+8th+St,+Shankar+Nagar,+Pammal,+Chennai&destinations=${address}&key=AIzaSyCfQ0EjpxAe8P7UBFtQ74kxZIRZsEyL4G4`
        )
        .then(function(response) {
          // handle success
          res.header('Content-Type', 'application/json');
          res.send(response.data);
        });
    });
});
// REGISTER OUR ROUTES -------------------------------
app.use('/', router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Magic happens on port ' + port);
