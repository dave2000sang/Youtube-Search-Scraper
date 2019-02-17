const express = require('express');
const bodyParser = require('body-parser');

// express obj
const app = express();

// middleware & routing
app.use(bodyParser.urlencoded({ extended:true}));
app.use(bodyParser.json());

// allow CORS to communicate between different domains
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });

var search;     // the string sent from HTML input
var result;     // json that contains name and links of youtube videos

// POST request to get search query from HTML script
app.post('/action', function(req,res) {
    search = req.body.search;

    // Run Python scraping script
    var spawn = require("child_process").spawn;
    var process = spawn('python',["../searchScraping.py"] );

    process.stdin.write(search);
    process.stdin.end();

    // get returned json from python script
    process.stdout.on('data', (data) => {
        // Do something with the data returned from python script
        console.log(JSON.parse(data));
        
        // Send response containing array of JSON data to client.
        res.send(JSON.parse(data));
    });

    // check for printed error in python file
    process.stderr.on('data', (data) => {
        // Do something with the data returned from python script
        console.log("error: " + data);
    });

    console.log(search);
});


// send POST response to python script with the search query
app.get('/toPython', function(req,res) {
    //send GET request to python file
    console.log(search + "  GET to Python")
    if(search != undefined)
        res.send(search);
    else
        res.send(null);

    result = req.body;
});


app.listen(3001, function() {
    console.log('Server running on port 3001');
})
