<template>
  <div>
    <el-card class='box-card' style='padding: 5px; margin: 100px 200px 5px 200px'>
      <div slot='header' class='clearfix'>
        <span>BLAST ONLINE</span>
        <el-button style='float: right; padding: 3px 0' type='text'
          >操作按钮</el-button
        >
      </div>
      <el-form label-position='left' label-width='80px' :model='formLabelAlign'>
        <el-form-item label='数据库'>
          <el-input v-model='formLabelAlign.name'></el-input>
        </el-form-item>
        <el-form-item label='序列'>
          <el-input v-model='formLabelAlign.region'></el-input>
        </el-form-item>
        <el-form-item label='名称'>
          <el-input v-model='formLabelAlign.type'></el-input>
        </el-form-item>
        <el-form-item  >
          <el-button type="primary" style='width:100%;'>提交</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'Blast',
  data () {
    return {
      formLabelAlign: {
        name: '',
        region: '',
        type: ''
      }
    }
  }
}
</script>
<style scoped>
</style>
