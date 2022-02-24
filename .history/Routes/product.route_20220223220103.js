var router = require('express').Router()

var controller = require('../controllers/product.controller')
router.get('/product/:id',controller.viewProduct)
// module.exports = router('/product/:id',controller.viewProduct)
