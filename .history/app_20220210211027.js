var app = require('express')()
//routes
app.get('/',(req,res)=>{
    // res.statusCode = 200
    res.send("Hien")
})
//open gate
app.listen(3000, function(){
    console.log("Server is listening at port 3000...")
})