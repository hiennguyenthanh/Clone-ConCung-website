// require conn
var {conn, sql}=require('../connect');

// add a new product
module.exports.postProduct = async function(req,res, next){
    var pool = await conn
    //.input(<var name>,<sql data type>, req.body.<var name saved in SQL server>)
    var sqlString = "INSERT INTO SANPHAM VAlUES (@masp, @tensp, @mota, @giagoc, @giamgia, @madm, @mancc) "
    .input('masp', sql.NVarChar, req.body.MaSP)
    .input('tensp',sql.NVarChar, req.body.TenSP)
    .input('masp',sql., req.body)
    .input('masp',sql., req.body)
    .input('masp',sql., req.body)
    .input('masp',sql., req.body)
    .query(sqlString, (req, res)=>{

    })
}