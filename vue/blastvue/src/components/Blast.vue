<template>
  <div>
    <el-card class='box-card' style='padding: 5px; margin: 100px 200px 5px 200px'>
      <div slot='header' class='clearfix'>
        <span>BLAST ONLINE</span>
        <el-button style='float: right; padding: 3px 0' type='text'
          >操作按钮</el-button
        >
      </div>
      <el-form label-position='left' label-width='80px' :model='formBlast' ref='blastform'>
        <el-form-item label='数据库'>
          <el-input v-model='formBlast.db'></el-input>
        </el-form-item>
        <el-form-item label='序列'>
          <el-input v-model='formBlast.sequence'></el-input>
        </el-form-item>
        <el-form-item label='名称'>
          <el-input v-model='formBlast.pro'></el-input>
        </el-form-item>
        <el-form-item  >
          <el-button type="primary" style='width:100%;' @click="submitBlast('blastform')">提交</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import { getBlast } from '@/api/blast'
import { Loading } from 'element-ui'
export default {
  name: 'Blast',
  data () {
    return {
      formBlast: {
        pro: '',
        db: '',
        sequence: ''
      },
      token: '',
      options: {
        lock: true,
        text: '拼命 BLAST 中...',
        background: 'rgba(0,0,0,.7)'
      }
    }
  },
  mounted () {
    this.token = this.$store.state.token
    console.log(this.token)
  },
  methods: {
    // 提交表单 在线blast
    submitBlast (formName) {
      let loadingInstance = Loading.service(this.options)
      let data = {
        pro: this.formBlast.pro,
        db: this.formBlast.db,
        sequence: this.formBlast.sequence
      }
      console.log(data)
      getBlast({blast: data}).then(response => {
        console.log(response)
        if (response.data.code === 200) {
          this.$notify({
            title: '成功',
            message: 'blast 成功',
            type: 'success'
          })
        } else {
          this.$notify({
            title: '失败',
            message: 'blast 失败',
            type: 'warning'
          })
        }
        loadingInstance.close()
      }).catch(err => {
        console.log(err)
        this.$notify({
          title: '失败',
          message: '服务器连接失败',
          type: 'error'
        })
        loadingInstance.close()
      })
    }
  }
}
</script>
<style scoped>
</style>
