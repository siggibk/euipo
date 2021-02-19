import express from 'express'
import { getDesignsController, getDesignDetailsController } from '../controllers/designs.js'

const router = express.Router()

router.get('', getDesignsController)
router.get('/:id', getDesignDetailsController)

export default router