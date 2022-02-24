// require conn
var {conn, sql}=require('../connect');
// view all products
module.exports.getProducts = async function(req, res, next){
    var pool = await conn;
    var sqlString = "SELECT * FROM SANPHAM where MaSP='SP000030'";
    return await pool.request().query(sqlString, (err, data)=>{
        res.send({result: data.recordset})
    })
}

// view product
module.exports.viewProduct = async function(req, res, next){
    var id = req.params;
    console.log(req.params)
    var pool = await conn;
    var sqlString = "SELECT * FROM SANPHAM where MaSP="+id;
    return await pool.request().query(sqlString, (err, data)=>{
        res.send({result: data.recordset})
    })
}
// add a new product
module.exports.postProduct = async function(req,res, next){
    var pool = await conn;
    //.input(<var name>,<sql data type>, req.body.<var name saved in SQL server>)
    var sqlString = "INSERT INTO SANPHAM VAlUES (@masp, @tensp, @mota, @giagoc, @giamgia, @madm, @mancc) "
    .input('masp', sql.VarChar, req.body.MaSP)
    .input('tensp',sql.NVarChar, req.body.TenSP)
    .input('mota',sql.NVarChar, req.body.MoTa)
    .input('giagoc',sql.Int, req.body.GiaGoc)
    .input('giamgia',sql.TinyInt, req.body.PhanTramGiamGia)
    .input('madm',sql.VarChar, req.body.MaDM)
    .input('mancc',sql.VarChar, req.body.MaNCC)
    .query(sqlString, (req, res)=>{

    })
}