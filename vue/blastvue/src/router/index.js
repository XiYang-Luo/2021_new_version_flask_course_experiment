import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import Blast from '@/components/Blast'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: '主页面',
      redirect: '/home'
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/blast',
      name: 'Blast',
      component: Blast
    },
    {
      path: '/helloworld',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ],
  mode: 'history'
})
