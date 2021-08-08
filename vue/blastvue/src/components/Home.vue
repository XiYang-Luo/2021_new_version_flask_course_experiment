<template>
  <div>
    <el-carousel indicator-position='outside' height='800px' style='margin:0;padding:0;'>
      <el-carousel-item v-for='(item, index) in images' :key='index' indicator-position="none">
        <!-- <h3>{{item}}</h3> -->
        <el-image :src='item.src' style='height:100%;width:100%;' alt='图片丢失了' fit='cover'></el-image>
        <div>test</div>
      </el-carousel-item>
    </el-carousel>
    <el-footer >
      <div>
      <h3>NCBI BLAST ON LINE</h3><br>
      <h5>The program compares nucleotide or protein sequences to sequence databases and calculates the statistical significance.</h5>
      </div>
    </el-footer>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      images: [{'src': '@/../static/q1.jpg'}, {'src': '@/../static/q2.jpg'}],
      text: [
        {'t1': 'NCBI Blast on line', 't2': 'BLAST finds regions of similarity between biological sequences.'},
        {'t1': 'Basic Local Alignment Search Tool', 't2': 'The program compares nucleotide or protein sequences to sequence databases and calculates the statistical significance.'}
      ]
    }
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
