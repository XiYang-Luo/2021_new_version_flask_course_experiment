import Vuex from 'vuex'
import Vue from 'vue'
Vue.use(Vuex)
// https://www.cnblogs.com/mica/p/10757965.html
export default new Vuex.Store({
  state: {
    count: 0,
    user: false,
    login: '登录/注册',
    token: ''
  },
  mutations: {
    increment (state) {
      state.count++
    }
  }
})
