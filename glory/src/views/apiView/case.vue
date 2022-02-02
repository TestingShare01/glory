<template>
  <div class="bodys">
    <!-- 基础信息 -->
    <div class="info">
      <div class="p">
        <p class="pp">基础信息</p>
      </div>

      <div class="inputed" style="margin-top: 10px">
        <div style="display: inline; margin-left: 10px">
          名称：&nbsp&nbsp&nbsp<el-input
            style="width: 400px"
            v-model="name"
          ></el-input>
        </div>

        <div style="display: inline; margin-left: 100px">
          备注：<el-input style="width: 400px" v-model="remark"></el-input>
        </div>
      </div>

      <div class="inputed" style="margin-top: 20px">
        <div style="display: inline; margin-left: 10px">
          优先级：<el-select
            class="selects"
            v-model="priority"
            placeholder="请选择"
          >
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </div>

        <div style="display: inline; margin-left: 100px">
          模块：<el-select
            v-model="mokuai"
            filterable
            placeholder="请选择"
            class="selects"
          >
            <el-option
              v-for="item in mokuais"
              :key="item"
              :label="item"
              :value="item"
            >
            </el-option>
          </el-select>
        </div>
      </div>

      <div class="inputed" style="margin-top: 20px">
        <div style="display: inline; margin-left: 10px">
          标签：&nbsp&nbsp&nbsp
          <el-select
            class="selects"
            v-model="tag"
            multiple
            filterable
            allow-create
            default-first-option
            placeholder="请输入标签"
          >
            <el-option
              v-for="item in tags"
              :key="item"
              :label="item"
              :value="item"
            >
            </el-option>
          </el-select>
        </div>
      </div>
    </div>

    <!-- 请求参数 -->
    <div class="info">
      <div class="p">
        <p class="pp">请求参数</p>
      </div>

      <div>
        <div class="url">
          <div style="margin-top: 15px">
            <el-input
              placeholder="请输入URL"
              v-model="url"
              class="input-with-select inputs"
            >
              <el-select
                v-model="selectmethod"
                slot="prepend"
                placeholder="请选择"
                style="width: 100px"
              >
                <el-option label="POST" value="POST"></el-option>
                <el-option label="GET" value="GET"></el-option>
                <el-option label="PUT" value="PUT"></el-option>
              </el-select>
            </el-input>
            <el-button type="primary" class="urtbtn" @click="zx">
              运行</el-button
            >

            <el-button type="primary" class="urtbtn" @click="apisave">
              保存</el-button
            >

            <!-- <t-button theme="success" lass="urtbtn">保存</t-button> -->

            <el-button
              type="success"
              class="urtbtn"
              style="margin-left: 50px"
              @click="dialogVisible = true"
            >
              Curl导入</el-button
            >
            <el-button type="warning" class="urtbtn" @click="logs">
              日志</el-button
            >
          </div>
        </div>

        <div class="canshu">
          <el-tabs v-model="activeName" >
            <el-tab-pane label="Body" name="first">
              <div
                class="paramdatadiv"
                v-for="(item, i) in datas"
                :key="item.id"
              >
                <el-input
                  class="divinput"
                  v-model="item.keys"
                  placeholder="Key"
                ></el-input>
                <el-input
                  class="divinputs"
                  v-model="item.val"
                  placeholder="Value"
                ></el-input>
                <el-button
                  class="btn2"
                  type="danger"
                  @click="del_div(i)"
                  v-show="!(datas.length == i + 1)"
                  icon="el-icon-minus"
                ></el-button>
                <el-button
                  class="btn2"
                  type="primary"
                  @click="add_div"
                  v-show="datas.length == i + 1"
                  icon="el-icon-plus"
                ></el-button>
              </div>
            </el-tab-pane>

            <el-tab-pane label="Hearders" name="second">
              <div
                class="paramdatadiv"
                v-for="(item, i) in headers"
                :key="item.id"
              >
                <el-input
                  class="divinput"
                  v-model="item.keys"
                  placeholder="Key"
                ></el-input>
                <el-input
                  class="divinputs"
                  v-model="item.val"
                  placeholder="Value"
                ></el-input>
                <el-button
                  class="btn2"
                  type="danger"
                  @click="del_head(i)"
                  v-show="!(headers.length == i + 1)"
                  icon="el-icon-minus"
                ></el-button>
                <el-button
                  class="btn2"
                  type="primary"
                  @click="add_head"
                  v-show="headers.length == i + 1"
                  icon="el-icon-plus"
                ></el-button>
              </div>
            </el-tab-pane>

            <el-tab-pane label="Cookies" name="third">
              <div
                class="paramdatadiv"
                v-for="(item, i) in cookies"
                :key="item.id"
              >
                <el-input
                  class="divinput"
                  v-model="item.keys"
                  placeholder="Key"
                ></el-input>
                <el-input
                  class="divinputs"
                  v-model="item.val"
                  placeholder="Value"
                ></el-input>
                <el-button
                  class="btn2"
                  type="danger"
                  @click="del_cookies(i)"
                  v-show="!(cookies.length == i + 1)"
                  icon="el-icon-minus"
                ></el-button>
                <el-button
                  class="btn2"
                  type="primary"
                  @click="add_cookies"
                  v-show="cookies.length == i + 1"
                  icon="el-icon-plus"
                ></el-button>
              </div>
            </el-tab-pane>

            <el-tab-pane label="提取器" name="four">
              <el-row v-for="(item,i) in tiqu" :key="item.keyRule">
                <el-col :span="6"> <el-input v-model="item.keyRule" placeholder="提取规则"></el-input></el-col>
                <el-col :span="6" style="margin-left:20px"><el-input v-model="item.keyName" placeholder="赋值名称"></el-input></el-col>
                <el-col :span="3"> 
                  <el-button icon="el-icon-plus" @click="addtiqu"></el-button>
                  <el-button icon="el-icon-minus" ></el-button>
                </el-col>
              </el-row>
            </el-tab-pane>

          </el-tabs>
        </div>
      </div>
    </div>

    <!-- 返回信息 -->
    <div class="info">
      <div class="p">
        <p class="pp">返回值</p>
      </div>

      <div class="response">
        <el-row type="flex" class="row-bg">
          <!-- 返回json显示 -->
          <el-col :span="15">
            <json-view v-show="ifjson==1" :data="jsonData" />
            <codemirror
              v-show="ifjson==0"
              style="width: 100%; height: 100%"
              v-model="jsonData"
              :options="cmOptions"
            >
            </codemirror>
          </el-col>

          <!-- 字段验证 -->
          <el-col :span="9" class="yanzheng">
            <div class="p">
              <p class="pp" style="display: inline-block">验证字段</p>

              <el-tooltip
                class="item"
                effect="dark"
                :content="con"
                placement="top-start"
              >
                <i
                  class="el-icon-warning-outline"
                  style="margin-left: 10px"
                ></i>
              </el-tooltip>

              <i
                class="el-icon-plus"
                style="line-height: 75px; margin-right: 20px; float: right"
                @click="addresult"
              ></i>

              <el-row
                type="flex"
                class="row-bg"
                v-for="(item, i) in resultPk"
                :key="item.id"
              >
                <el-col :span="12">
                  <el-input
                    v-model="item.keys"
                    placeholder="请输入断言路径"
                  ></el-input>
                </el-col>

                <el-col :span="6" style="margin-left: 10px"
                  ><el-input
                    v-model="item.expect"
                    placeholder="预期结果"
                  ></el-input
                ></el-col>

                <el-col :span="6" style="line-height: 40px; margin-left: 20px"
                  ><i class="el-icon-success" v-if="item.status == 1"></i>
                  <i class="el-icon-error" v-if="item.status == 2"></i>
                </el-col>
              </el-row>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>

    <!-- Curl弹框  -->
    <el-dialog
      title="Curl导入"
      :append-to-body="true"
      :visible.sync="dialogVisible"
      width="50%"
    >
      <el-input type="textarea" :rows="8" v-model="curldata"></el-input>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="curl">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 日志右侧弹框 -->
    <el-drawer
      title="日志"
      :visible.sync="table"
      direction="rtl"
      size="40%"
      style="width: 100%"
    >
      <el-table :data="gridData">
        <el-table-column
          property="createtime"
          label="日期"
          width="150"
        ></el-table-column>
        <el-table-column
          property="msg"
          label="信息"
          width="500px"
        ></el-table-column>
      </el-table>
    </el-drawer>
  </div>
</template>

<script>
import jsonView from "vue-json-views";

import "codemirror/mode/javascript/javascript.js";
import "codemirror/theme/material.css";
import { codemirror } from "vue-codemirror";
import "codemirror/lib/codemirror.css";

import {
  oneCase,
  apiSave,
  getOneCase,
  getTagList,
  getModel,
  getlog,
  SaveTiquValue
} from "@/api/common.js";
import { pk } from "@/api/tools.js";
export default {
  created() {
    this.getid();
    this.getTag();
    this.getModelList();
  },
  data() {
    return {
      tiqu:[{"keyRule":"","keyName":""}],
      ifjson:0,
      cmOptions: {
        tabSize: 4,
        styleActiveLine: true,
        lineNumbers: true,
        line: true,
        // mode: 'text/javascript',
        mode:{
          name:"javascript",
          json:true
        },
        lineWrapping: true,
        theme: 'material'
        },
      table: false,
      gridData: [],
      cookies: [{ keys: "", val: "" }],
      url: "",
      remark: "",
      name: "",
      con: "断言支持多层级验证，可通过.的方式逐级查找：eg：info.user.name 如果存在列表可eg：info.user[2].name的方式查找",
      priority: "",
      options: [
        { value: "P0", label: "P0" },
        { value: "P1", label: "P1" },
        { value: "P2", label: "P2" },
        { value: "P3", label: "P3" },
      ],
      mokuais: [],
      mokuai: "",
      tags: [],
      tag: [],
      jsonData: {},

      curldata: "",
      dialogVisible: false,
      input3: "",
      activeName: "first",
      selectmethod: "POST",
      resultPk: [{ keys: "", expect: "", result: "", status: 0 }],
      datas: [{ keys: "", val: "" }],
      headers: [{ keys: "", val: "" }],
      formInline: {
        user: "",
        region: "",
      },
    };
  },
  components: {
    jsonView,codemirror
  },
  methods: {
    addtiqu(){
      this.tiqu.push({"keyRule":"","keyName":""})
    },
    addresult() {
      this.resultPk.push({ keys: "", expect: "", result: "", status: 0 });
    },
    handleClick() {
      console.log(1111);
    },
    add_div() {
      this.datas.push({ keys: "", val: "" });
    },
    del_div(id) {
      this.datas.splice(id, 1);
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

    // 获取curl解析
    curl() {
      var str = this.curldata.split(" ");
      var curl_head = [];
      var cook = []
      for (var i in str) {
        var head_curl = {};
        if(str[i]==="-H"){
          head_curl["keys"] = str[parseInt(i) + 1].replace('"',"").replace(":","")
          if(str[parseInt(i) + 1].replace('"',"").replace(":","")==="Cookie"){
            for(var k=0;k<100;k++){
              var cooke = {}
              if(str[parseInt(i) + 2+k] != "-H"){
                console.log(str[parseInt(i) + 2+k])
                cooke["keys"] = str[parseInt(i) + 2+k].split("=")[0]
                cooke["val"] = str[parseInt(i) + 2+k].split("=")[1].replace(";","").replace('"',"")
              }else{
                break
              }
              cook.push(cooke)
            }
          }
          
          var va = ""
          for(var j=0;j<1000;j++){
            if(str[parseInt(i) + 2 + j] !="-H" && str[parseInt(i) + 2 + j]!="--compressed" && str[parseInt(i) + 2 + j] != "--data" ){
              va = va + str[parseInt(i) + 2 + j].replace('"',"")
            }else{
              head_curl["val"] = va
              break
            }
          }
  
        curl_head.push(head_curl)
        }
        if(str[i]==="--compressed"){
          this.url = str[parseInt(i)+1].replace('"',"").replace('"',"")
        }
      }
      this.cookies = cook
      var new_head = []
      curl_head = curl_head.filter(item=>{
        if(item.keys !="Cookie"){
          new_head.push(item)
        }
      })
      this.headers = new_head
      this.dialogVisible = false;
    },
    // 运行
    zx() {
      var id = this.$route.query.id;
      console.log(id);
      oneCase(
        id,
        this.selectmethod,
        this.url,
        this.datas,
        this.headers,
        this.resultPk,
        this.cookies
      ).then((ress) => {
        console.log(ress.data);
        if (ress.data.res.code === 0) {
          var ifstr = ress.data.res.response
          if(ifstr.constructor != String){
            console.log("非字符串")
            this.ifjson = 1
          }
          console.log(ress.data.res.response)
          this.jsonData = ress.data.res.response;
    
          
        } else {
          this.$message.error(ress.data.res.msg);
        }

        if (ress.data.result != null && ress.data.result != 0) {
          this.resultPk = ress.data.result;
        }
      });
    },

    //接口保存
    apisave() {
      let id = this.$route.query.id;
      if (
        this.url != "" &&
        this.name != "" &&
        this.priority != "" &&
        this.mokuai != "" &&
        this.tag != []
      ) {
        var username = localStorage.getItem("user");
        apiSave(
          id,
          username,
          this.name,
          this.remark,
          this.priority,
          this.mokuai,
          this.tag,
          this.url,
          this.selectmethod,
          this.datas,
          this.headers,
          this.cookies,
          this.resultPk
        ).then((res) => {
          console.log(res.data);
          this.$message.success(res.data);
        });
        if(id != undefined && this.tiqu[0]["keyRule"] !=""){
          this.saveTiValue()
          console.log("提取器已提交")
        }else{
          console.log("提取器信息不全")
        }
      } else {
        this.$message.error("请填写全部内容哦！！！");
      }
    },

    //获取url参数
    getid() {
      let id = this.$route.query.id;
      if (id) {
        console.log("走这里");
        getOneCase(id).then((res) => {
          var datass = res.data.api_list[0];
          this.name = datass.name;
          this.remark = datass.remark;
          this.priority = datass.priority;
          this.mokuai = datass.mokuai;
          this.tag = eval(datass.tag);
          this.selectmethod = datass.methods;
          this.url = datass.url;
          this.datas = eval(datass.bodys);
          this.headers = eval(datass.headers);
          this.cookies = eval(datass.cookie);
          this.resultPk = eval(datass.resultPk);
  
          console.log(res.data.tiqu_list.length)
          if (datass.extractor.length != 0){
            this.tiqu = eval(datass.extractor)
          }
        });
      }
    },

    //获取tagList数据
    getTag() {
      getTagList().then((res) => {
        for (var i in res.data) {
          this.tags.push(res.data[i]["name"]);
        }
      });
    },

    //获取所有模块
    getModelList() {
      getModel().then((res) => {
        console.log(res.data);
        var model = res.data.data;
        for (var i in model) {
          this.mokuais.push(model[i]["name"]);
        }
      });
    },

    //弹框log
    logs() {
      this.table = true;
      this.logdata();
    },
    logdata() {
      let id = this.$route.query.id;
      getlog(id).then((res) => {
        console.log(res.data);
        this.gridData = res.data;
      });
    },

    //保存时，上传提取器参数
    saveTiValue(){
      let id = this.$route.query.id;
      console.log(this.tiqu)
      SaveTiquValue(id,this.tiqu).then(res=>{
        console.log(res.data)
      })
    }
  },
};
</script>

<style>
.el-icon-error {
  color: red;
}
.el-icon-success {
  color: #00db00;
  size: 10px;
}
.yanzheng {
  height: 300px;
  background-color: #ffffff;
}
.response {
  width: 100%;
  height: 400px;
  text-align: left;
}
.response_left {
  text-align: left;
  width: 70%;
  height: 400px;
  background-color: antiquewhite;
  float: left;
}
.response_right {
  width: 30%;
  height: 400px;

  float: right;
}
.selects {
  width: 400px;
}

.el-dialog__body {
  padding: 10px 20px;
}
.el-tabs__content {
  margin-top: 10px;
}
.tabs {
  height: 30px;
  width: 100%;
  background-color: #61a5e4;
}
.canshu {
  margin-left: 10px;
  width: 100%;
  padding-bottom: 30px;
}
.inputed {
  height: 40px;
  width: 100%;
  text-align: left;
}
.atest {
  text-align: left;
}
.test {
  background-color: #61a5e4;
  width: 100%;
  height: 40px;
}
.input_div {
  width: 100%;
  float: left;
  margin-left: 20px;
}
.infobase {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
  align-content: space-between;
}
.input_base {
  width: 400px;
  margin-left: 10px;
}
.pz {
  width: 100%;
  height: 70px;
  margin-left: 10px;
}
.urtbtn {
  float: left;
  margin-left: 20px;
}
.el-input {
  width: 100%;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
.sele {
  float: left;
}
.p {
  height: 50px;
}
.inputs {
  width: 1000px;
  float: left;
}
.url {
  width: 100%;
  margin-left: 10px;
  height: 50px;
}
.select_input {
  width: 150px;
}
.pp {
  text-align: left;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 10px;
  border-left-style: solid;
  border-color: #61a5e4;
}
.info {
  /* width: 100%; */
  background-color: #ffffff;
  margin-top: 10px;
  margin-left: 10px;
  box-shadow: inset 0 0 10px #ccc;
  padding-bottom: 20px;
}
.req {
  width: 100%;
  height: 400px;
  background-color: azure;
}
.rep {
  width: 100%;
  height: 400px;
  background-color: azure;
}
.bodys {
  background-color: #f0f0f0;
  width: 100%;
}

.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

.case {
  margin-top: 20px;
}
.addcurlbtn {
  margin-top: 10px;
  right: 0;
}
.paramdatadiv {
  float: left;
  margin-left: 5px;
  /* display: inline-block; */
  margin-top: 5px;
}
.divinput {
  width: 450px;
}
.divinputs {
  margin-left: 30px;
  width: 450px;
}
.btn2 {
  margin-left: 10px;
}
.el-form-item__content {
  display: inline-block;
}
.el-table__body {
  width: 100%;
}
</style>