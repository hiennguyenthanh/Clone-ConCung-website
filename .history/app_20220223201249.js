var app = require('express')()
var bodyParser = require("body-parser")
var {conn, sql} = require('./connect')
app.use(bodyParser.json())
//routes
app.get('/',async (req,res)=>{
    var pool = await conn;
    var sqlString = "Select * from KHACHHANG";
    return await pool.request().query(sqlString, (err,data) => {
        var i = 0;
        for(i=0;i<data.recordset.length;i++)
            res.send({data: data.recordset[i] })
    })
    // res.send("Hien")
})
//open gate
app.listen(3000, function(){
    console.log("Server is listening at port 3000...")
})