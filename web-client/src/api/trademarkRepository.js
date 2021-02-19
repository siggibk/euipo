import client from './client'

export default {
  get(params) {
    return client.get('trademarks/', {
      params: params
    })
  },
  getDetails(application_number) {
    return client.get(`trademarks/${application_number}`)
  }
}