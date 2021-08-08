<template>
  <div style='margin-top:120px;'>
    <el-row :gutter="20">
  <el-col :span="8"><div class="grid-content bg-purple"></div></el-col>
  <el-col :span='8'>
    <el-card :body-style="{ padding: '0px' }">
      <img src='@/../static/X22.jpg' class='image'>
      <!-- 登录-->
      <div style='padding: 5px;' v-show='sign_in'>
        <div style='padding:15px;'>
        <div style='display:block;width:100%;'>
            <span style='float:left;font-size:20px;padding:0px;'><a @click="signIn">登录</a> / <a @click="Logon">注册</a></span><br>
        </div>
        <br>
        <el-form :model="signInForm" status-icon ref="signINForm" label-width="60px" class="demo-ruleForm" label-position="left" >
        <el-form-item label="用户名" prop="name0">
            <el-input type="name" v-model="signInForm.name0"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="pass0">
            <el-input type="password" v-model="signInForm.pass0" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item style='float:left;'>
            <el-button type="primary" @click="submitSignInForm('signINForm')">提交</el-button>
            <el-button @click="resetForm('signINForm')">重置</el-button>
        </el-form-item>
        </el-form>
        </div>
      </div>
      <!-- 注册-->
      <div style='padding: 5px;' v-show='logon'>
        <div style='padding:15px;'>
        <div style='display:block;width:100%;'>
            <span style='float:left;font-size:20px;padding:0px;'><a @click="Logon">注册</a> / <a @click="signIn">登录</a></span><br>
        </div>
        <br>
        <el-form :model="logonForm" status-icon ref="logonForm" label-width="60px" class="demo-ruleForm" label-position="left" >
        <el-form-item label="用户名" prop="name">
            <el-input type="name" v-model="logonForm.name"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="pass">
            <el-input type="password" v-model="logonForm.pass" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="确认" prop="checkPass">
            <el-input type="password" v-model="logonForm.checkPass" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item style='float:left;'>
            <el-button type="primary" @click="submitLogonForm('logonForm')">提交</el-button>
            <el-button @click="resetForm('logonForm')">重置</el-button>
        </el-form-item>
        </el-form>
        </div>
      </div>
    </el-card>
  </el-col>
  <el-col :span="8"><div class="grid-content bg-purple"></div></el-col>
</el-row>
  </div>
</template>

<script>
import { getTUser, getTUserLogon } from '@/api/login'
export default {
  name: 'Login',
  data () {
    return {
      sign_in: true,
      logon: false,
      signInForm: {
        pass0: '',
        name0: ''
      },
      logonForm: {
        pass: '',
        checkPass: '',
        name: ''
      }
    }
  },
  created () {
    if (this.$store.state.user === true) {
      this.$notify({
        title: '成功',
        message: '您已登陆成功！请勿重复登录',
        type: 'warning'
      })
      this.$router.replace('/home')
    }
  },
  methods: {
    // 点击登录按钮显示登陆表单
    signIn () {
      this.sign_in = true
      this.logon = false
    },
    // 点击注册按钮显示注册表单
    Logon () {
      this.sign_in = false
      this.logon = true
    },
    // 重置表单
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    // 提交表单 登录
    submitSignInForm (formName) {
      let data = {
        name: this.signInForm.name0,
        password: this.signInForm.pass0
      }
      getTUser({users: data}).then(response => {
        console.log(response)
        console.log(this.$store.state.user)
        if (response.data.code === 200) {
          this.$store.state.user = true
          this.$store.state.login = '登陆成功'
          this.$store.state.token = response.data.token
          this.$notify({
            title: '成功',
            message: '登陆成功！',
            type: 'success'
          })
          console.log(this.$store.state.user)
          this.$router.replace('/home')
        } else {
          this.$notify({
            title: '失败',
            message: '登陆失败！密码/账号不正确',
            type: 'warning'
          })
        }
      }).catch(err => {
        console.log(err)
        this.$notify({
          title: '失败',
          message: '服务器连接失败',
          type: 'error'
        })
      })
    },
    // 提交表单 注册
    submitLogonForm (formName) {
      let data = {
        name: this.logonForm.name,
        password: this.logonForm.pass
      }
      getTUserLogon({users: data}).then(response => {
        console.log(response)
        if (response.data.code === 200) {
          this.$store.state.user = true
          this.$store.state.login = '登陆成功'
          this.$store.state.token = response.data.token
          this.$notify({
            title: '成功',
            message: '注册成功！',
            type: 'success'
          })
          this.$router.replace('/home')
        } else {
          this.$notify({
            title: '失败',
            message: '注册失败！账号已存在',
            type: 'warning'
          })
        }
      }).catch(err => {
        console.log(err)
        this.$notify({
          title: '失败',
          message: '服务器连接失败',
          type: 'error'
        })
      })
    }
  }
}
</script>
<style scoped>
a {
    text-decoration:none;
    color: black;
}
.el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #ffffff;
  }
  .bg-purple {
    background: #ffffff;
  }
  .bg-purple-light {
    background: #ffffff;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #ffffff;
  }

  .time {
    font-size: 13px;
    color: #999;
  }
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }
  .button {
    padding: 0;
    float: right;
  }
  .image {
    width: 100%;
    display: block;
  }
  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  .clearfix:after {
      clear: both
  }
</style>
