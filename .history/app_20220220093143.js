var app = require('express')()
var bodyParser = require("body-parser")
var connect = require('./connect')
console.log(connect)
app.use(bodyParser.json())
//routes
app.get('/',(req,res)=>{
    // res.statusCode = 200
    res.send("Hien")
})
//open gate
app.listen(3000, function(){
    console.log("Server is listening at port 3000...")
})