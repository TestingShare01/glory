<template>
  <div class="bodiv">
    <!-- 顶部添加 -->
    <el-row class="btndiv">
      <el-col :span="12" style="text-align:left;">
        <el-input style="width:300px" size="mini" placeholder="筛选域名"></el-input>
        <el-button size="mini" style="margin-left:10px" > 筛选</el-button>
      </el-col>

      <el-col :span="12">
        <el-button
          type="primary"
          size="mini"
          style="margin-right: 20px"
          @click="dialogVisible = true"
          >添加配置</el-button
        >
        <el-button
          type="info"
          @click="dialogURL = true"
          size="mini"
          style="margin-right: 20px"
          >URL导入</el-button
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
          <el-table-column prop="urlName" label="域名" width="250">
          </el-table-column>

          <el-table-column prop="ip" label="IP" width="250"> </el-table-column>
          <el-table-column prop="createtime" label="日期" width="250">
          </el-table-column>

          <el-table-column label="操作">
            <template slot-scope="scope">
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
      <el-row style="line-height: 40px">
        <el-col :span="3">域名:</el-col>
        <el-col :span="15"
          ><el-input placeholder="请输入环境名称" v-model="envName"></el-input
        ></el-col>
      </el-row>

      <el-row style="line-height: 40px; margin-top: 5px">
        <el-col :span="3">IP:</el-col>
        <el-col :span="15"
          ><el-input placeholder="请输入环境名称" v-model="ip"></el-input
        ></el-col>
      </el-row>

      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addName">确 定</el-button>
      </span>
    </el-dialog>

    <!-- URL导入弹框 -->
    <el-dialog :visible.sync="dialogURL" width="30%" title="URL导入域名IP">
      <el-input v-model="urls"></el-input>

      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="urladd">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { envIp, getIp, addurl } from "@/api/common.js";
export default {
  created() {
    this.getData();
  },
  data() {
    return {
      dialogVisible: false,
      name: "",
      tableData: [],
      envId: 0,
      envName: "",
      ip: "",
      dialogURL: false,
      urls: "",
    };
  },
  methods: {
    urladd() {
      let id = this.$route.query.id;
      addurl(id, this.urls).then((res) => {
        console.log(res.data);
      });
      this.dialogURL = false;
    },
    tableRowClassName({ row, rowIndex }) {
      if (rowIndex === 1) {
        return "warning-row";
      } else if (rowIndex === 3) {
        return "success-row";
      }
      return "";
    },
    addName() {
      let id = this.$route.query.id;
      console.log(id);
      if (id != 0 && this.envName != "" && this.ip != "") {
        envIp(id, this.envName, this.ip).then((res) => {
          console.log(res.data);
        });
        this.dialogVisible = false;
      }
    },
    getData() {
      let id = this.$route.query.id;
      getIp(id).then((res) => {
        console.log(res.data);
        this.tableData = res.data;
      });
    },
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