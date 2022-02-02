<template>
  <div>
    <!-- 顶部按钮功能 -->
    <div class="addbtn">
      <el-button type="primary" size="small" class="btn" @click="casedite"
        >添加接口</el-button
      >

      <el-button
        type="warning"
        size="small"
        class="btn"
        @click="dialogmaketask = true"
        >创建任务</el-button
      >

      <el-input
        class="input"
        placeholder="标签"
        size="small"
        style="width: 200px"
        v-model="SelectTag"
      ></el-input>

      <el-select
        class="selects"
        v-model="SelectModel"
        placeholder="请选择模块"
        size="small"
      >
        <el-option
          v-for="item in model_list"
          :key="item.id"
          :label="item.name"
          :value="item.name"
        >
        </el-option>
      </el-select>

      <el-select
        class="selects"
        v-model="SelectPriority"
        placeholder="请选择优先级"
        size="small"
      >
        <el-option
          v-for="item in options"
          :key="item"
          :label="item"
          :value="item"
        >
        </el-option>
      </el-select>
      <el-button
        type="success"
        size="small"
        style="margin-left: 10px"
        @click="selectResult"
        >筛选</el-button
      >
    </div>

    <!-- 列表数据 -->
    <div>
      <el-table
        :data="tableData"
        border
        style="width: 100%"
        @selection-change="handleSelectionChange"
        size="small"
      >
        <el-table-column type="selection" width="55"> </el-table-column>
        <el-table-column prop="name" label="名称" width="150">
        </el-table-column>
        <el-table-column prop="url" label="URL" width="500" :show-overflow-tooltip="true"> </el-table-column>
        <el-table-column prop="methods" label="请求方法" width="100">
          <template slot-scope="scope">
            <el-tag
              :type="scope.row.methods === 'POST' ? 'success' : 'warning'"
              >{{ scope.row.methods }}</el-tag
            >
          </template>
        </el-table-column>
        <el-table-column prop="priority" label="优先级" width="100">
        </el-table-column>
        <el-table-column prop="tag" label="标签" width="150">
          <template slot-scope="scope">
            <el-tag
              type="success"
              v-for="item in tagsfor(scope.row.tag)"
              style="margin-left: 5px"
              >{{ item }}</el-tag
            >
          </template>
        </el-table-column>
        <el-table-column prop="mokuai" label="模块" width="120">
        </el-table-column>

        <el-table-column prop="user" label="负责人" width="100">
        </el-table-column>

        <el-table-column prop="remark" label="备注" width="200">
        </el-table-column>

        <el-table-column fixed="right" label="操作" width="200">
          <template slot-scope="scope">
            <el-button
              type="primary"
              size="mini"
              @click="edite(scope.row.id)"
              style="margin-left: 10px; margin-bottom: 5px"
              >编辑</el-button
            >

            <el-button type="danger" size="mini" @click="del(scope.row.id)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </div>

    <!-- 分页 -->
    <div class="pages">
      <el-pagination
        background
        layout="prev, pager, next"
        :total="count"
        page-size="20"
        @current-change="handleCurrentChange"
      >
      </el-pagination>
    </div>

    <el-dialog title="创建任务" :visible.sync="dialogmaketask" width="30%">
      <template slot="title">
        <div style="font-size: 18px; font-weight: bold; float: left">
          创建任务
        </div>
      </template>
      <el-input placeholder="任务名称" v-model="taskName"></el-input>

      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogmaketask = false">取 消</el-button>
        <el-button type="primary" @click="makeTask">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import {
  getApiList,
  makeTasks,
  delCaseApi,
  getModel,
  selectApi,
} from "@/api/common.js";
export default {
  created() {
    this.getapilist();
    this.user = localStorage.getItem("user");
    this.getSelectData();
  },
  data() {
    return {
      SelectModel: "",
      SelectPriority: "",
      SelectTag: "",
      user: "",
      id_list: [],
      taskName: "",
      dialogmaketask: false,
      model_id: 0,
      tableData: [],
      tag: ["1", "2"],
      options: ["P0", "p1", "P2", "P3"],
      priority: "",
      model_list: [],
      count: 0,
    };
  },
  methods: {
    getdata() {
      this.model_id = this.$route.query.model;
    },
    getapilist() {
      getApiList().then((res) => {
        console.log(res.data);
        if (res.data.code === 0) {
          this.tableData = res.data.api_list;
          this.count = res.data.countNum;
        } else {
          console.log(res.data.msg);
        }
      });
    },
    casedite() {
      this.$router.push("/case");
    },

    //编辑接口
    edite(id) {
      this.$router.push("/case?id=" + id);
    },

    //删除接口
    del(id) {
      delCaseApi(id).then((res) => {
        console.log(res.data);
        this.getapilist();
      });
    },

    //勾选框
    handleSelectionChange(val) {
      this.id_list = [];
      val.forEach((element) => {
        this.id_list.push(element.id);
      });
      console.log(this.id_list);
    },

    //创建任务
    makeTask() {
      console.log(this.id_list);
      if (this.id_list.length != 0 && this.taskName != "") {
        makeTasks(this.id_list, this.taskName, this.user).then((res) => {
          console.log(res.data);
          if (res.data.code === 1) {
            this.$message.warning(res.data.msg);
          }
          this.dialogmaketask = false;
        });
      } else {
        this.$message.error("请检查是否勾选接口或填写任务名称");
      }
    },
    tagsfor(tags) {
      return eval(tags);
    },

    //获取筛选模块数据
    getSelectData() {
      getModel().then((res) => {
        console.log(res.data);
        this.model_list = res.data.data;
      });
    },

    //筛选结果集
    selectResult() {
      selectApi(this.SelectTag, this.SelectModel, this.SelectPriority, 1).then(
        (res) => {
          this.tableData = res.data.api_list;
        }
      );
    },

    //分页点击
    handleCurrentChange(val) {
      let id = this.$route.query.id;
      getReport(id, val).then((res) => {
        console.log(res.data);
        if (res.data.code === 0) {
          this.tableData = res.data.data_list;
          this.count = res.data.countNum;
        }
      });
    },
  },
};
</script scoped>

<style>
.addbtn {
  text-align: left;
  width: 100%;
  height: 50px;
  line-height: 50px;
}
.btn {
  float: right;
  margin-top: 10px;
  margin-right: 10px;
}
.input {
  margin-left: 10px;
}
.selects {
  margin-left: 10px;
}
.pages {
  bottom: 0px;
  right: 0px;
  display: flex;
  height: 40px;
  margin-top: 20px;
  float: right;
}
</style>