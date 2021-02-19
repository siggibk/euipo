import { getDesigns, getDesignById }  from '../db/queries/designs.js'

export const getDesignsController = async (req, res) => {
  const { applicant_identifier } = req.query
  const result = await getDesigns(applicant_identifier)
  res.send(result)
}

export const getDesignDetailsController = async (req, res) => {
  const { id } = req.params
  const result = await getDesignDetailsController(id)
  res.send(result)
}
