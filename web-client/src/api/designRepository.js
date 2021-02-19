import client from './client'

export default {
  get(params) {
    return client.get('designs/', {
      params: params
    })
  },
  getDetails(design_identifier) {
    return client.get(`designs/${design_identifier}`)
  }
}