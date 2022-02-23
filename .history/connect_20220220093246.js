var sql = require('mssql/msnodesqlv8')

var config = {
    server:"localhost",
    user:"sa",
    password:"123456",
    database:"Quanlycuahang",
    driver: "msnodesqlv8",
}

const conn = new sql.ConnectionPool(config).connect().then(pool=>pool)

module.exports={
    conn: conn,
    sql: sql
}
