var http = require('http')
// console.log(http)
var server = http.createServer(function(res, req){
    // res.statusCode(200);
    res.send('<h1>Hien</h1>')
})
server.listen(3000, function(){
    console.log("Server is listening at port 3000...")
})