<template>
  <div>
    <div class="addbtn">
      <el-button type="primary" size="mini" class="btn" @click="dialogFormVisible = true;"
        >添加项目</el-button
      >
    </div>
    <div class="tablelist" :header-cell-style="{background:'#eef1f6',color:'#606266'}">
      <el-table :data="tableData" border style="width: 100%">
        <el-table-column  prop="name" label="项目名称" min-width="20%">
        </el-table-column>
        <el-table-column prop="describe" label="描述" min-width="20%">
        </el-table-column>
        <el-table-column prop="jk_num" label="接口数" min-width="20%">
        </el-table-column>
        <el-table-column prop="case_num" label="用例数" min-width="20%">
        </el-table-column>
     
        <el-table-column  label="操作" min-width="20%">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row.id)" type="primary" size="small"
              >进入</el-button
            >
            <el-button type="success" size="small">编辑</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <el-dialog title="创建项目" :visible.sync="dialogFormVisible" :append-to-body="true" width="25%">
      <template slot="title">
        <div style="font-size: 18px; font-weight: bold; float: left">
          添加项目
        </div>
      </template>

      <el-form :model="form" label-width="45px">
        <el-form-item label="名称">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
      </el-form>

      <el-form :model="form" label-width="45px">
        <el-form-item label="描述">
          <el-input
            v-model="form.describe"
            placeholder="请输入内容"
            type="textarea"
          ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="addproject"
          >确 定</el-button
        >
      </div>
    </el-dialog>
  </div>
</template>

<script>
import {projectAdd, projectGet} from "@/api/common.js"
export default {
  created(){
      this.getdata()
  },
  data() {
    return {
      form: {
        name: "",
        describe:""
      },
      dialogFormVisible: false,
      tableData: []
    };
  },
  methods: {
    addproject() {
      this.dialogFormVisible = false;
      projectAdd(this.form.name,this.form.describe).then(res=>{
          if(res.data.code ===0){
            this.$message.success(res.data.msg);
              this.getdata()
          }else{
            this.$message.error(res.data.msg);
          }

      })
    },
    getdata(){
        projectGet().then(res=>{
            this.tableData = res.data.data
        })
    },
    handleClick(id){
        this.$router.push("/model?id="+id)
    }
  },
};
</script>

<style scoped>
.addbtn {
  width: 100%;
  height: 50px;
}
.btn {
  float: left;
  margin-top: 10px;
  margin-left: 10px;
}
.input {
  width: 300px;
  float: left;
}
.tablelist{
    margin-left: 10px;
}
</style>