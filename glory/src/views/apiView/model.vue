<template>
  <div>
    <div class="addbtn">
      <el-button type="primary" size="mini" class="btn" @click="dialogFormVisible = true;"
        >添加模块</el-button
      >
    </div>
    <div class="tablelist" :header-cell-style="{background:'#eef1f6',color:'#606266'}">
      <el-table :data="tableData" border style="width: 100%">
        <el-table-column  prop="name" label="模块名称" min-width="20%">
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

    <el-dialog title="创建项目" :visible.sync="dialogFormVisible" width="25%">
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
import {modelAdd, modelGet} from "@/api/common.js"
export default {
  created(){
      let id = this.$route.query.id
      this.id = id
      this.getdata()
  },
  data() {
    return {
      form: {
        name: "",
        describe:""
      },
      dialogFormVisible: false,
      tableData: [],
      id:0
    };
  },
  methods: {
    addproject() {
      this.dialogFormVisible = false;

      modelAdd(this.form.name,this.form.describe,this.id).then(res=>{
          if(res.data.code ===0){
            this.$message.success(res.data.msg);
              this.getdata()
          }else{
            this.$message.error(res.data.msg);
          }

      })
    },
    getdata(){
        modelGet(this.id).then(res=>{
            this.tableData = res.data.data
        })
    },
    handleClick(id){
        this.$router.push("/caselist?model="+id)
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