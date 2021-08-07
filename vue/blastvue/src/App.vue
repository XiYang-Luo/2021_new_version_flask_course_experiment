<template>
  <div id='app'>
    <div id='nav'>
    <el-menu
      class='el-menu-demo'
      mode='horizontal'
      style='margin:0;padding:0;width:100%;'
    >
      <el-menu-item index='1'>
        <router-link to='/home'>首页</router-link>
      </el-menu-item>
      <el-submenu index='2'>
        <template slot='title'>我的工作台</template>
        <el-menu-item index='2-1'>
          <router-link to='/helloworld'>选项1</router-link>
        </el-menu-item>
        <el-menu-item index='2-2'>选项2</el-menu-item>
        <el-menu-item index='2-3'>选项3</el-menu-item>
      </el-submenu>
      <el-menu-item index='3'>
        <router-link to='/helloworld'>测试</router-link>
      </el-menu-item>
    </el-menu>
    </div>
    <router-view></router-view>
    <el-footer >Footer</el-footer>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Home from './components/Home.vue'

export default {
  name: 'app',
  components: {
    HelloWorld,
    Home
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
</style>
