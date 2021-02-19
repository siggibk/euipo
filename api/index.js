import express from 'express'
import bodyParser from 'body-parser'
import cors from 'cors'
import trademarkRoutes from './routes/trademarks.js'
import designRoutes from './routes/designs.js'

const app = express()
const PORT = 5000

// init bodyparser middleware with json
app.use(bodyParser.json())
app.use(cors())

// define top level routes
app.use('/trademarks', trademarkRoutes)
app.use('/designs', designRoutes)

app.listen(PORT, () => {
  console.log(`Server up and running on http://localhost:${PORT}`)
})