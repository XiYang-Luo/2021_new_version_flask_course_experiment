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
          <el-input v-model='formBlast.db' placeholder='nt' :clearable='true'></el-input>
        </el-form-item>
        <el-form-item label='序列'>
          <el-input v-model='formBlast.sequence' placeholder='sequence' :clearable='true'></el-input>
        </el-form-item>
        <el-form-item label='名称'>
          <el-input v-model='formBlast.pro' placeholder='blastn' :clearable='true'></el-input>
        </el-form-item>
        <el-form-item  >
          <el-button type="primary" style='width:100%;' @click="submitBlast('blastform')">提交</el-button>
        </el-form-item>
      </el-form>
    </el-card>
    <div style='padding: 5px; margin: 30px 200px 5px 200px'>
    <el-divider content-position="left">历史记录</el-divider>
    <div v-for='(item, index) in blast_history' :key='index'>
      <div @click='historyDetails(item)' :data-id='item'>
      <el-card shadow='hover' style='font-size:16px;text-align:left;border-radius:7px;margin:0px;'>
        <template slot="extra">
          <el-button type="primary" size="small">操作</el-button>
        </template>
        <el-descriptions title='BALST'>
          <el-descriptions-item label='名称'>{{item['project_name'] | ellipsis}}</el-descriptions-item>
          <el-descriptions-item label='序列'>{{item['seq'] | ellipsis}}</el-descriptions-item>
          <el-descriptions-item label='DB'>{{item['db_ncbi']}}</el-descriptions-item>
          <el-descriptions-item label='备注'>
            <el-tag size='small'>--</el-tag>
          </el-descriptions-item>
        </el-descriptions>
      </el-card>
      <br>
    </div>
    </div>
    </div>

    <div style="margin :10px;">
    <el-drawer
      title='历史详情'
      :visible.sync='drawer'
      :append-to-body='true'
      :withHeader='true'
      size='70%'
      :with-header='false'>
      <el-divider></el-divider>
      <div style="margin :20px;">
      <el-form label-position="right" label-width="150px">
        <div v-for='(it, index1) in history_item_key' :key='index1'>
          <el-form-item :label="it">
            <el-input v-model="history_item_value[index1]" :readonly='true'></el-input>
          </el-form-item>
        </div>
      </el-form>
      </div>
    </el-drawer>
    </div>
  </div>
</template>

<script>
import { getBlast, getBlastHistory } from '@/api/blast'
import { Loading } from 'element-ui'
export default {
  name: 'Blast',
  filters: {
    ellipsis (value) {
      if (!value) return ''
      if (value.length > 14) {
        return value.slice(0, 14) + '...'
      }
      return value
    }
  },
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
      },
      blast_history: [],
      drawer: false,
      history_item: [],
      history_item_key: [],
      history_item_value: []
    }
  },
  created () {
    let d = window.localStorage.getItem('blastForm')
    console.log(d)
    if (d) {
      let dd = JSON.parse(d)
      this.formBlast.pro = dd.pro
      this.formBlast.db = dd.db
      this.formBlast.sequence = dd.sequence
    }
  },
  mounted () {
    this.token = this.$store.state.token
    this.getHistory()
  },
  methods: {
    // https://blog.csdn.net/qq_44472790/article/details/90273766
    historyDetails (item) {
      this.drawer = true
      console.log(item)
      let key = []
      let value = []
      for (let index in item) {
        // console.log(index)
        key.push(index)
        // console.log(item[index])
        value.push(item[index])
      }
      this.history_item = [item]
      this.history_item_key = key
      this.history_item_value = value
      // console.log(this.history_item, key, value)
    },
    getHistory () {
      let data = {
        token: this.token
      }
      getBlastHistory({blast_history: data}).then(resp => {
        console.log(resp)
        if (resp.data.code === 200) {
          this.blast_history = resp.data.data
        }
        if (resp.data.code === 500) {
          this.$store.state.token = ''
          this.$store.state.user = false
          this.$router.replace('/login')
        }
        console.log(this.blast_history)
      })
    },
    // 提交表单 在线blast
    submitBlast (formName) {
      let loadingInstance = Loading.service(this.options)
      let data = {
        token: this.$store.state.token,
        pro: this.formBlast.pro,
        db: this.formBlast.db,
        sequence: this.formBlast.sequence
      }
      console.log(data)
      window.localStorage.setItem('blastForm', JSON.stringify(data))
      getBlast({blast: data}).then(response => {
        console.log(response)
        if (response.data.code === 200) {
          this.$notify({
            title: '成功',
            message: 'blast 成功',
            type: 'success'
          })
        } else if (response.data.code === 500) {
          this.$store.state.user = false
          this.$store.state.token = ''
          this.$router.replace('/login')
          window.localStorage.setItem('token', JSON.stringify({token: ''}))
        } else {
          this.$notify({
            title: '失败',
            message: 'blast 失败',
            type: 'warning'
          })
        }
        this.getHistory()
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
