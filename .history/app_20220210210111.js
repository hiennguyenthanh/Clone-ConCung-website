// var http = require('http')

// var server = http.createServer(function(res, req){
//     // res.statusCode(200);
//     res.send('<h1>Hien</h1>');
// })
// server.listen(3000, function(){
//     console.log("Server is listening at port 3000...")
// })

var app = require('express')()
app.get('/',(req,res)=>{
    // res.statusCode = 200
    res.send("Hien")
})
app.listen(3000, function(){
    console.log("Server is listening at port 3000...")
})