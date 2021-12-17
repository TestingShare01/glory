<template>
  <div>
    <div class="addbtn">
      <el-button type="primary" size="mini" class="btn" @click="dialogFormVisible = true;"
        >添加接口</el-button
      >
    </div>
      <div>列表页面{{model_id}}</div>
  </div>
</template>

<script>
export default {
    created(){
        this.getdata()
    },
    data(){
        return{
            model_id:0
        }
    },
    methods:{
        getdata(){
            this.model_id = this.$route.query.model
        }
    }
}
</script scoped>

<style>
.addbtn {
  width: 100%;
  height: 50px;
}
.btn {
  float: left;
  margin-top: 10px;
  margin-left: 10px;
}
</style>