import request from '@/api/request'
// blast
export function getBlast (params) {
  return request({
    url: '/api/blast/blast-server/get-blast',
    method: 'post',
    params
  })
}
export function getBlastHistory (params) {
  return request({
    url: '/api/blast/blast-server/get-blast-history',
    method: 'get',
    params
  })
}
