var router = require('express').Router()

var controller = require('../controllers/product.controller')
router.get('/',controller.getProducts)
router.get('/:id',controller.viewProduct)
router.post('/products', controller.postProduct)
module.exports = router