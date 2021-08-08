<template>
  <div>
    <el-carousel indicator-position='outside' height='800px' style='margin:0;padding:0;'>
      <el-carousel-item v-for='item in 4' :key='item'>
        <h3>{{ item }}</h3>
      </el-carousel-item>
    </el-carousel>
    <el-footer >Footer</el-footer>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {}
  },
  created () {
    console.log(this.$store.state.user)
  },
  methods: {
  }
}
</script>
<style scoped>
.el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 800px;
    margin: 0;
  }
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
