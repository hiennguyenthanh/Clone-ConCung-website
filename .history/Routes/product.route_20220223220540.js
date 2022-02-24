var router = require('express').Router()

var controller = require('../controllers/product.controller')
router.get('/products',controller.getProducts)
router.get('/products/:id',controller.viewProduct)
// module.exports = router('/product/:id',controller.viewProduct)
module.exports = router