<template>
  <div>
    <div class="dh">
      <el-input
        placeholder="任务名称"
        style="width: 200px"
        size="mini"
      ></el-input>
      <el-button type="primary" size="mini" style="margin-left:10px">筛选</el-button>

      <!-- <span style="float: right; margin-right: 20px"
        >总任务数:102 总执行次数：100
      </span> -->
    </div>

    
    <div>
      <el-table :data="tableData" style="width: 100%" size="small">
        <el-table-column label="名称" prop="name" width="180">
        </el-table-column>

        <el-table-column label="接口数" prop="api_num" width="100">
        </el-table-column>

        <el-table-column label="用例数" prop="case_num" width="100">
        </el-table-column>

        <el-table-column label="执行次数" prop="zx_num" width="100">
        </el-table-column>

        <el-table-column label="正确率" prop="accuracy" width="100">
        </el-table-column>

        <el-table-column label="创建者" prop="makeUser" width="100">
        </el-table-column>

        <el-table-column label="执行者" prop="user" width="100">
        </el-table-column>

        <el-table-column label="执行时间" prop="zx_time" width="180">
        </el-table-column>

        <el-table-column label="状态" prop="status" width="180">
          <template slot-scope="scope">
            <el-tag
              effect="dark"
              size="small"
              :type="scope.row.status === '未执行' ? 'info' : 'success'"
              >{{ scope.row.status }}</el-tag
            >
          </template>
        </el-table-column>

        <el-table-column label="操作" fixed="right" width="400">
          <template slot-scope="scope">
            <el-button size="mini" @click="taskzx(scope.row.id)" type="success"
              >执行</el-button
            >
            <el-button size="mini" @click="report(scope.row.id)" type="warning"
              >报告</el-button
            >
            <el-button size="mini" @click="dingshi(scope.row)" type="primary"
              >定时任务</el-button
            >

            <el-button size="mini" @click="config(scope.row.id)" type="primary"
              >前置条件</el-button
            >
            <el-button size="mini" type="danger" @click="deltask(scope.row.id)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </div>

    <el-dialog
      title="cron表达式定时任务"
      :visible.sync="dialogVisible"
      width="30%"
    >
      <el-input placeholder="cron规范 * * * * *" v-model="cron"></el-input>
      <span slot="footer" class="dialog-footer">
        <el-button @click="deltimi" type="info">删除</el-button>

        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="editCorn">确 定</el-button>
      </span>
    </el-dialog>

    <el-dialog
      :visible.sync="configuration"
      width="50%"
      class="config"
      style="border-radius: 10px"
    >
      <el-tabs v-model="activeName" type="card">
        <el-tab-pane label="Curl导入" name="first">
          <el-input type="textarea" :rows="10" v-model="culcookie"></el-input>
          <el-button
            type="success"
            size="mini"
            style="float: right; margin-right: 1px; margin-top: 5px"
            @click="addCurl"
            >导入</el-button
          >
        </el-tab-pane>
        <el-tab-pane label="全局Cookie" name="second">
          <el-row v-for="(item, i) in cookies" :key="item.keys">
            <el-col :span="9">
              <el-input placeholder="Key" v-model="item.keys"></el-input
            ></el-col>
            <el-col :span="9" style="margin-left: 10px">
              <el-input placeholder="Value" v-model="item.val"></el-input
            ></el-col>
            <el-col :span="2">
              <el-button icon="el-icon-plus" @click="add_cookies"></el-button
            ></el-col>
            <el-col :span="2">
              <el-button
                icon="el-icon-minus"
                @click="del_cookies(i)"
              ></el-button
            ></el-col>
          </el-row>
        </el-tab-pane>

        <el-tab-pane label="全局Headers" name="third">
          <el-row v-for="(item, i) in headers" :key="item.keys">
            <el-col :span="9">
              <el-input placeholder="Key" v-model="item.keys"></el-input
            ></el-col>
            <el-col :span="9" style="margin-left: 10px">
              <el-input placeholder="Value" v-model="item.val"></el-input
            ></el-col>
            <el-col :span="2">
              <el-button icon="el-icon-plus" @click="add_head"></el-button
            ></el-col>
            <el-col :span="2">
              <el-button icon="el-icon-minus" @click="del_head(i)"></el-button
            ></el-col>
          </el-row>
        </el-tab-pane>
        <el-tab-pane label="前置Case" name="fourth"
          ><el-input
            v-model="case_list"
            placeholder="请输入caseid逗号隔开"
          ></el-input
        ></el-tab-pane>

        <el-tab-pane label="环境配置" name="five" style="text-align: left">
          <el-row>
            <el-col :span="3"><p>环境配置：</p></el-col>
            <el-col :span="21">
              <el-select v-model="envalues" placeholder="请选择">
                <el-option
                  v-for="item in envList"
                  :key="item.value"
                  :label="item.name"
                  :value="item.id"
                >
                </el-option>
              </el-select>
            </el-col>
          </el-row>
        </el-tab-pane>
      </el-tabs>

      <div slot="footer" class="dialog-footer">
        <el-button @click="configuration = false">取 消</el-button>
        <el-button type="primary" @click="addconfig">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import {
  getTask,
  zxTask,
  Cron,
  delTask,
  delTimin,
  createGload,
  getGload,
  getEnv,
} from "@/api/common.js";
export default {
  created() {
    this.gettask();
    this.getdataEnv()
  },
  data() {
    return {
      envalues:"",
      case_list: "",
      culcookie: "",
      activeName: "first",
      taskId: "",
      cron: "",
      dialogVisible: false,
      dialogVisibleqz: false,
      configuration: false,
      tableData: [],
      headers: [{ keys: "", val: "" }],
      cookies: [{ keys: "", val: "" }],
      envList: [],
    };
  },
  methods: {
    handleEdit(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
      console.log(index, row);
    },

    //获取任务
    gettask() {
      getTask().then((res) => {
        console.log(res.data);
        this.tableData = res.data;
      });
    },

    //执行任务
    taskzx(id) {
      let username = localStorage.getItem("user");
      zxTask(id, username).then((res) => {
        console.log(id);
        console.log(res.data);
        this.gettask();
      });
    },

    //查看报告
    report(id) {
      this.$router.push("/report?id=" + id);
    },

    //定时弹框
    dingshi(id) {
      this.dialogVisible = true;
      this.taskId = id.id;
      this.cron = id.cron;
    },

    // 设置定时任务
    editCorn() {
      Cron(this.taskId, this.cron).then((res) => {
        console.log(res.data);
        this.dialogVisible = false;
      });
    },

    // 删除定时任务
    deltimi() {
      delTimin(this.taskId).then((res) => {
        console.log(res.data);
      });
    },

    //删除任务
    deltask(id) {
      delTask(id).then((res) => {
        console.log(res.data);
        this.gettask();
      });
    },

    //前置条件弹框
    config(id) {
      this.configuration = true;
      this.taskId = id;
      this.getGloads();
    },

    //curl导入
    curl() {
      var url = this.culcookie.split(" ");
      var cooke = [];
      var head = [];
      for (var i in url) {
        var header = {};
        if (url[i] === "-H") {
          if (
            url[parseInt(i) + 1].replace('"', "").replace(":", "") === "Cookie"
          ) {
            for (var j = 0; j < 1000; j++) {
              var cookie = {};
              if (
                url[parseInt(i) + 2 + j] != "-H" &&
                url[parseInt(i) + 2 + j] != "--compressed"
              ) {
                console.log(url[parseInt(i) + 2 + j]);
                cookie["keys"] = url[parseInt(i) + 2 + j].split("=")[0];
                cookie["val"] = url[parseInt(i) + 2 + j]
                  .split("=")[1]
                  .replace(";", "")
                  .replace('"', "");
                cooke.push(cookie);
              } else {
                break;
              }
            }
          } else {
            header["keys"] = url[parseInt(i) + 1]
              .replace('"', "")
              .replace(":", "");
            var va = "";
            for (var j = 0; j < 1000; j++) {
              if (
                url[parseInt(i) + 2 + j] != "-H" &&
                url[parseInt(i) + 2 + j] != "--compressed" &&
                url[parseInt(i) + 2 + j] != "--data"
              ) {
                va = va + url[parseInt(i) + 2 + j].replace('"', "");
              } else {
                header["val"] = va;
                break;
              }
            }
            head.push(header);
          }
        }
      }
      // var new_head = []
      // header = header.filter(item=>{
      //   if(item.keys !="Cookie"){
      //     new_head.push(item)
      //   }
      // })

      this.cookies = cooke;
      this.headers = head;
    },

    // 配置确定键
    addconfig(id) {
      var cooke = [];
      var head = [];
      for (var i = 0; i < this.cookies.length; i++) {
        if (this.cookies[i].keys === "") {
          cooke = "null";
        } else {
          cooke = this.cookies;
          createGload(this.taskId, "cookies", this.cookies).then((res) => {
            console.log(res.data);
          });
          break;
        }
      }

      for (var i = 0; i < this.headers.length; i++) {
        if (this.headers[i].keys === "") {
          head = "null";
        } else {
          head = this.headers;
          createGload(this.taskId, "headers", this.headers).then((res) => {
            console.log(res.data);
          });
          break;
        }
      }
      if (this.case_list != "") {
        createGload(this.taskId, "caseId", this.case_list).then((res) => {
          console.log(res.data);
        });
      }
      if(this.envalues !=""){
        console.log(this.envalues)
        createGload(this.taskId,"env",this.envalues).then(res=>{
          console.log(res.data)
        })
      }
    },

    //curl导入
    addCurl() {
      if (this.culcookie != "") {
        this.curl();
      } else {
        this.$message.error("请输入内容");
      }
    },

    add_head() {
      this.headers.push({ keys: "", val: "" });
    },
    del_head(id) {
      this.headers.splice(id, 1);
    },

    add_cookies() {
      this.cookies.push({ keys: "", val: "" });
    },
    del_cookies(id) {
      this.cookies.splice(id, 1);
    },

    //获取任务全局内容
    getGloads() {
      getGload(this.taskId).then((res) => {
        res.data.gloab.forEach((element) => {
          console.log(element);
          if (element.parameter === "cookies") {
            this.cookies = eval(element.value);
          }
          if (element.parameter === "headers") {
            console.log(element.va);
            this.headers = eval(element.value);
          }
          if (element.parameter === "caseId") {
            this.case_list = eval(element.value);
          }
          this.envalues= res.data.envid
        });
      });
    },

    // 获取环境配置数据
    getdataEnv(){
      getEnv().then(res=>{
        console.log(res.data)
        this.envList = res.data
      })
    }
  },
};
</script>

<style scoped>
.el-dialog {
  border-radius: 100px;
}
.config {
  border-radius: 100px;
}
.dh {
  width: 100%;
  height: 50px;
  text-align: left;
  line-height: 50px;
}
</style>