var router = require('express').Router()

var controller = require('../controllers/product.controller')
router.get('/',controller.getProducts)
router.get('/:id',controller.viewProduct)

module.exports = router