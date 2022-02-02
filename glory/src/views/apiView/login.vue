<template>
  <div class="bodiv">
    <div class="logdiv">
      <h1 class="title">Glory Go</h1>

      <el-form
        :model="ruleForm"
        status-icon
        label-width="50px"
        class="demo-ruleForm"
      >
        <el-form-item label="账号">
          <el-input v-model="ruleForm.user" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input
            type="password"
            v-model="ruleForm.pwd"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm" style="width: 100%"
            >提交</el-button
          >
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import { login } from "@/api/common.js";
export default {
  data() {
    return {
      ruleForm: {
        user: "",
        pwd: "",
      },
    };
  },
  methods: {
    submitForm() {
      login(this.ruleForm.user, this.ruleForm.pwd).then((res) => {
        if (res.data.code === 0) {
          localStorage.setItem("user",res.data.user)
          this.$router.push("/");
        } else {
          this.$message.error(res.data.msg);
        }
      });
    },
  },
};
</script>

<style scoped>
.el-form-item__label {
  width: 60px;
}
.demo-ruleForm {
  padding: 10px 10px 10px -20px;
}
.title {
  margin-top: 10px;
}
.logdiv {
  height: 280px;
  width: 400px;
  background-color: #e0e0e0;
  margin: 0 auto;
  margin-top: 200px;
  border-radius: 10px;
  padding: 20px 20px 0px 20px;
  opacity: 0.9;
}
.bodiv {
  position: absolute;

  text-align: center;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
  height: 100%;
  width: 100%;
  background-image: url(../../../public/logback.jpeg);
}
</style>