var app = require('express')();
var bodyParser = require("body-parser");
var {conn, sql} = require('./connect');

//require Routes
var userRoute = require('./Routes/customer.route')
var productRoute = require('./Routes/product.route')

//view engine
app.set('view engine','pug');
app.set('views','./views')

app.use(bodyParser.json());
//routes
app.get('/',async (req,res)=>{
    // var pool = await conn;
    // var sqlString = "Select * from KHACHHANG";
    // return await pool.request().query(sqlString, (err,data) => {
    //     var i = 0;
    //     for(i=0;i<data.recordset.length;i++)
    //         res.send(`<h3>${data.recordset[i]}</h3>`)
    // })
    res.send("Hien")
})
//routes
app.use('/user',userRoute);
app.use('/products',productRoute);
//open gate
app.listen(3000, function(){
    console.log("Server is listening at port 3000...")
})