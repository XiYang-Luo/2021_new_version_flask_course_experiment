import request from '@/api/request'
// blast
export function getBlast (params) {
  return request({
    url: '/api/blast/blast-server/get-blast',
    method: 'post',
    params
  })
}
