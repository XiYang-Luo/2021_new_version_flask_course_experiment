import axios from 'axios'
// import store from '@/store'
// 创建axios实例
const service = axios.create({
  // 解决跨域请求 https://www.bilibili.com/video/BV15K4y1C78C?from=search&seid=6231093023760267093
  baseURL: '',
  timeout: 1800000 // 请求超时时间
})

service.interceptors.response.use(
  function (response) {
    return Promise.resolve(response)
  },
  function (error) {
    return Promise.reject(error)
  }
)

export default service
