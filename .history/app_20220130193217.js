var http = require('http')
// console.log(http)
var server = http.createServer(function(res, req){
    req.statusCode = 404
})
server.listen(3000,function(){
    console.log("Server is listening at port 3000...")
})