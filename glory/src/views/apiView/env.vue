<template>
  <div class="bodiv">
    <!-- 顶部添加 -->
    <el-row class="btndiv">
      
      <el-col :span="24">
        <el-button
          type="primary"
          size="mini"
          style="margin-right: 20px"
          @click="dialogVisible = true"
          >添加环境</el-button
        >
      </el-col>
    </el-row>

    <!--  列表数据 -->
    <el-row class="tablediv">
      <el-col :span="24">
        <el-table
          :data="tableData"
          style="width: 100%"
          :row-class-name="tableRowClassName"
        >
          <el-table-column prop="id" label="ID" width="180"> </el-table-column>
          <el-table-column prop="name" label="名称" width="180">
          </el-table-column>
          <el-table-column prop="createtime" label="日期"> </el-table-column>

          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button
                type="primary"
                size="mini"
                @click="handleEdit(scope.row.id)"
                >进入</el-button
              >
              <el-button
                size="mini"
                type="danger"
                @click="handleDelete(scope.$index, scope.row)"
                >删除</el-button
              >
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>

    <!-- 弹框添加 --><el-dialog
      title="环境名称"
      :visible.sync="dialogVisible"
      width="30%"
    >
      <el-input placeholder="请输入环境名称" v-model="name"></el-input>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addName">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { envSet, getEnv } from "@/api/common.js";
export default {
  created() {
    this.getData();
  },
  data() {
    return {
      dialogVisible: false,
      name: "",
      tableData: [],
    };
  },
  methods: {
    tableRowClassName({ row, rowIndex }) {
      if (rowIndex === 1) {
        return "warning-row";
      } else if (rowIndex === 3) {
        return "success-row";
      }
      return "";
    },
    addName() {
      if (this.name != "") {
        envSet(this.name).then((res) => {
          console.log(res.data);
        });
        this.dialogVisible = false;
      }
    },
    getData() {
      getEnv().then((res) => {
        console.log(res.data);
        this.tableData = res.data;
      });
    },
    handleEdit(id){
        this.$router.push("/envList?id="+id)
    }
  },
};
</script>

<style scoped>
.btndiv {
  height: 60px;
  width: 100%;
  text-align: right;
  line-height: 60px;
}
.el-table .warning-row {
  background: oldlace;
}

.el-table .success-row {
  background: #f0f9eb;
}
</style>