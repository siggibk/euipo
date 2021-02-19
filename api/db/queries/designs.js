import query from '../../db/index.js'

export const getDesigns = async (applicant_identifier) => {
    const res = await query(
      `SELECT design_identifier, application_number, indication, status, renewal_status, status_date
      FROM design WHERE applicant_identifier = $1`,
      [applicant_identifier]
    )
    return res.rows
  }
  
  export const getDesignById = async (id) => {
    const res = await query(
      'SELECT * FROM design WHERE design_identifier = $1',
      [id]
    )
    return res.rows[0]
  }