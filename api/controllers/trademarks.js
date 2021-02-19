import { getTrademarks, getTrademarkWithClasses }  from '../db/queries/trademarks.js'

export const getTrademarksController = async (req, res) => {
  const { applicant_identifier } = req.query
  const result = await getTrademarks(applicant_identifier)
  res.send(result)
}

export const getTrademarkDetailsController = async (req, res) => {
  const { id } = req.params
  const result = await getTrademarkWithClasses(id)
  res.send(result)
}
