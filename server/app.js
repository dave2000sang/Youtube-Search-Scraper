const express = require('express');
const bodyParser = require('body-parser');

// express obj
const app = express();
const app2 = express();

// middleware & routing
app.use(bodyParser.urlencoded({ extended:true}));
app2.use(bodyParser.urlencoded({ extended:true}));


var search;     // the string sent from HTML input


// actual POST request to get search query from HTML script
app.post('/action', function(req,res){      // req=request, res=response
    
    search = req.body.search;
    res.send(req.body.search);
    console.log(search);

});


// send POST response to python script with the search query
app2.get('/toPython', function(req,res){
    //send GET request to python file
    console.log(search + "  GET")
    if(search != undefined)
        res.send(search);
    else
        res.send(null);
});


app.listen(3000, function() {
    console.log('HTML Server running on port 3000');
});

app2.listen(3001, function() {
    console.log('Python Server running on port 3001');
})