var app = require('express')()
var bodyParser = require("body-parser")
var {conn, sql} = require('./connect')
app.use(bodyParser.json())
//routes
app.get('/',async (req,res)=>{
    var pool = await conn;
    var sqlString = "Select MaKH from KHACHHANG where Makh = 'KH00503'";
    return await pool.request().query(sqlString, (err,data) => 
        res.send({data: data.recordset })
    )
    res.send("Hien")
})
//open gate
app.listen(3000, function(){
    console.log("Server is listening at port 3000...")
})