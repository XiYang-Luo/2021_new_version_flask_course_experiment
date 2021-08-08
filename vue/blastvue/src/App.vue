<template>
  <div id='app'>
    <div id='nav'>
    <el-menu
      class='el-menu-demo'
      mode='horizontal'
      style='margin:0;padding:0px 10px;width:100%;'
    >
      <el-menu-item index='1'>
        <router-link to='/' class='router-style'>首页</router-link>
      </el-menu-item>
      <el-submenu index='2'>
        <template slot='title'>
          <router-link to='/helloworld' class='router-style'>工具</router-link>
        </template>
        <el-menu-item index='2-1' @click="toBlast">
          BLAST
        </el-menu-item>
        <el-menu-item index='2-2'>待定...</el-menu-item>
        <el-menu-item index='2-3'>待定...</el-menu-item>
      </el-submenu>
      <el-menu-item index='3'>
        <router-link to='/login' class='router-style'>
        <el-button  icon="el-icon-menu" size='small' style='border:solid red 0px;'>{{this.$store.state.login}}</el-button>
        </router-link>
      </el-menu-item>
    </el-menu>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Home from './components/Home.vue'
import Blast from './components/Blast.vue'
import Login from './components/Login.vue'
// import { mapState } from 'vuex'
export default {
  name: 'app',
  components: {
    HelloWorld,
    Home,
    Blast,
    Login
  },
  data () {
    return {
    }
  },
  created () {
  },
  mounted () {
    console.log('ssss')
  },
  computed: {
    isLogin () {
      return this.$store.state.login
    }
  },
  watch: {
    isLogin (newVal, oldVal, deep = 'true') {
      // console.log('sssssssss', newVal, oldVal)
    }
  },
  methods: {
    // 判断是否登录 未登录则跳转到登录页面
    toBlast () {
      if (this.$store.state.user === true) {
        this.$router.replace('/blast')
      } else {
        this.$notify({
          title: '提示',
          message: '您还未登录，请先登录',
          type: 'warning'
        })
        this.$router.replace('/login')
      }
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  font-size: 22px;
}
/**占满全屏 */
*{
  margin:0;
  padding:0;
  border:0;
}
#nav {
  position: fixed;
  width: 100%;
  left: 0;
  top: 0;
  z-index: 1000;
}
.router-style {
  text-decoration: none;
  color: black;
}
</style>
