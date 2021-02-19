import express from 'express'
import { getTrademarksController, getTrademarkDetailsController } from '../controllers/trademarks.js'

const router = express.Router()

// all routes getting matched here start with /trademarks
router.get('', getTrademarksController)
router.get('/:id', getTrademarkDetailsController)

export default router