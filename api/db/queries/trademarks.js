import query from '../../db/index.js'

export const getTrademarks = async (applicant_identifier) => {
  const res = await query(
    `SELECT application_number, name, status, status_date, status_milestone
    FROM trademark WHERE applicant_identifier = $1
    `,
    [applicant_identifier]
  )
  console.log(res.rows)
  console.log(applicant_identifier)
  return res.rows
}

export const getTrademarkById = async (id) => {
  const res = await query(
    'SELECT * FROM trademark WHERE application_number = $1',
    [id]
  )
  return res.rows[0]
}

export const getTrademarkClasses = async (id) => {
  const res = await query(
    `SELECT json_agg(res.item) as classes
    FROM (
      SELECT json_build_object(
        'class', tc.number,
        'descriptions', jsonb_agg(tcd)
      ) as item
      FROM trademark_class tc
      LEFT JOIN trademarkclass_description tcd ON tc.id = tcd.trademark_class_id
      WHERE tc.application_number = $1
      GROUP BY tc.number
    ) res`,
    [id]
  )
  return res.rows[0].classes
}

export const getTrademarkWithClasses = async (id) => {
  let [trademark, trademarkClasses] = await Promise.all([getTrademarkById(id), getTrademarkClasses(id)])

  return {
    ...trademark,
    classes: trademarkClasses
  }
}