import axios from 'axios'
import qs from 'qs'

export const ajax = axios.create({
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  transformRequest: function (data){
    return qs.stringify(data)
  },
  withCredentials: true
})

ajax.interceptors.request.use(function (config) {
  
  return config
}, function (error) {
  return Promise.reject(error)
})

ajax.interceptors.response.use(function (response) {

  return response
}, function (error) {
  if (error.response) {
    if (error.response.status === 500){
      console.log('伺服器繁忙')
    }
  }
  return Promise.reject(error)
})