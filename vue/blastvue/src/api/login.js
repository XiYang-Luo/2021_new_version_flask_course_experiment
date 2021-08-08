import request from '@/api/request'

// 查询用户
export function getTUser (params) {
  return request({
    url: '/api/login/login-server/users',
    method: 'get',
    params
  })
}

// 用户注册
export function getTUserLogon (params) {
  return request({
    url: '/api/login/login-server/users',
    method: 'post',
    params
  })
}
