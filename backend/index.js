var express = require('express');
var bodyParser = require('body-parser');
const csv = require('csv-parser');
const fs = require('fs');
const csvToJson = require('convert-csv-to-json');

var app = express();
// configure body parser
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 8080; // set our port

// create our router
var router = express.Router();
var fileInputName = 'S.csv'; 
var fileOutputName = 'data.json';
csvToJson.generateJsonFileFromCsv(fileInputName,fileOutputName);

fs.createReadStream('S.csv')
  .pipe(csv())
  .on('data', row => {
    console.log(row);
  })
  .on('end', () => {
    console.log('CSV file successfully processed');
  });

// middleware to use for all requests
router.use(function(req, res, next) {
  // do logging
  console.log('Something is happening.');
  next();
});

// test route to make sure everything is working (accessed at GET http://localhost:8080/api)
router.get('/', function(req, res) {
  res.json({ message: 'hooray! welcome to our api!' });
});

// REGISTER OUR ROUTES -------------------------------
app.use('/', router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Magic happens on port ' + port);
