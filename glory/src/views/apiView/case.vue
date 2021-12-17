<template>
  <div class="bodys">
    <!-- 基础信息 -->
    <div class="info">
      <div class="p">
        <p class="pp">基础信息</p>
      </div>

      <div class="inputed" style="margin-top: 10px">
        <div style="display: inline; margin-left: 10px">
          名称：&nbsp&nbsp&nbsp<el-input style="width: 400px" :v-model="name"></el-input>
        </div>

        <div style="display: inline; margin-left: 100px" :v-model="remark">
          备注：<el-input style="width: 400px"></el-input>
        </div>
      </div>

      <div class="inputed" style="margin-top: 20px">
        <div style="display: inline; margin-left: 10px">
          优先级：<el-select class="selects" v-model="priority" placeholder="请选择">
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
          模块：<el-input style="width: 400px"></el-input>
        </div>
      </div>

      <div class="inputed" style="margin-top: 20px">
        <div style="display: inline; margin-left: 10px">
          标签：&nbsp&nbsp&nbsp<el-input style="width: 400px"></el-input>
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
              v-model="input3"
              class="input-with-select inputs"
            >
              <el-select v-model="select" slot="prepend" placeholder="请选择">
                <el-option label="POST" value="POST"></el-option>
                <el-option label="GET" value="GET"></el-option>
                <el-option label="PUT" value="PUT"></el-option>
              </el-select>
            </el-input>
            <el-button type="primary" class="urtbtn"> 运行</el-button>
            <el-button type="primary" class="urtbtn"> 保存</el-button>

            <el-button
              type="success"
              class="urtbtn"
              style="margin-left: 50px"
              @click="dialogVisible = true"
            >
              Curl导入</el-button
            >
          </div>
        </div>

        <div class="canshu">
          <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="Body" name="first">
              <div
                class="paramdatadiv"
                v-for="(item, i) in datas"
                :key="item.id"
              >
                <el-input class="divinput" v-model="item.keys"></el-input>
                <el-input class="divinputs" v-model="item.val"></el-input>
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
                <el-input class="divinput" v-model="item.keys"></el-input>
                <el-input class="divinputs" v-model="item.val"></el-input>
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


            <el-tab-pane label="Cookies" name="third">角色管理</el-tab-pane>
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
        <json-view :data="jsonData" />
      </div>
    </div>

    <!-- Curl弹框  -->
    <el-dialog
      title="Curl导入"
      :append-to-body="true"
      :visible.sync="dialogVisible"
      width="50%"
      :before-close="handleClose"
    >
      <el-input type="textarea" :rows="8" v-model="curldata"></el-input>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="curl"
          >确 定</el-button
        >
      </span>
    </el-dialog>
  </div>
</template>

<script>
import jsonView from "vue-json-views";

export default {
  data() {
    return {
      priority:"",
      options:[
        {value:"P0",label:"P0"},
        {value:"P1",label:"P1"},
        {value:"P2",label:"P2"},
        {value:"P3",label:"P3"},
      ],
      jsonDatas: {},
      jsonData: {
        status: 1,
        errorCode: 0,
        errorMessage: "",
        body: {
          groupIns: 0,
          faceToFaceAnswerer: 0,
          institutionId: 2867,
          insName: "爱学习北京名师课堂",
          roles: ["teacher", "teacher_print"],
          localDoubleTeacherListen: 0,
          telephone: "15001000009",
          institutionType: 1,
          xiaoheBindStatus: 0,
          menu: {
            tr_qbkc: 1,
            axg_jcsz_get_list: 1,
            rxcp: 1,
            bm_jwzx_zhgl: 1,
            bm: 1,
            tr_wdkc: 1,
            qzqmcp: 1,
            bm_zhxx_get_idleAccount: 1,
            bm_zhxx_put_submitRenew: 1,
            px_order_list: 1,
            jy: 1,
            tr_sy: 1,
            axg_gkk_bj_get_teaching: 1,
            bm_yxzx_zlzx_zszl: 1,
            market_daily: 1,
            bm_zhxx_get_shoppingRecord: 1,
            xqcp: 1,
            px_role_list: 1,
            bm_zhxx_get_rsplist: 1,
            bm_yxzx_zlzx: 1,
            cp: 1,
            bm_zhxx_get_accountDetail: 1,
            px_subject_list: 1,
            bm_zhxx: 1,
            px_order_submit: 1,
            bm_zhxx_accountSpendList: 1,
            px_order_confirm: 1,
            cpplfx: 1,
            bsk: 1,
            bm_zhxx_get_idlegroupList: 1,
            bm_zhxx_get_renewAccountList: 1,
            px_user_list: 1,
            bm_zlxz: 1,
            tr: 1,
          },
          userId: 2741019,
          groupInsOrgType: 0,
          portraitPath: "https://image.aixuexi.com/default.jpg",
          insId: 2867,
          logoPic: "http://img-test.aixuexi.com/FnY2FQgKMeg9L1iLluxaTMkaHu1G",
          localDoubleTeacherSpeaker: 0,
          doubleTeacherStatus: 2,
          id: 2741019,
          loveSchoolManage: 0,
          username: "zyh09",
        },
      },
      curldata: "",
      dialogVisible: false,
      input3: "",
      activeName: "first",
      select: "POST",
      datas: [{ keys: "", val: "" }],
      headers:[{ keys: "", val: "" }],
      formInline: {
        user: "",
        region: "",
      },
    };
  },
  components: {
    jsonView,
  },
  methods: {
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

    curl(){
      var str = this.curldata.split(" ")

      var curl_head = []
      for(var i in str){
        var head_curl = {};
        console.log(str[i])
        if(str[i]==="-H"){
          head_curl["keys"] = str[parseInt(i)+1].replace(":","").replace("\"","")
          head_curl["val"] = str[parseInt(i)+2].replace("\"","")
          curl_head.push(head_curl)
        }
        if(str[i]==="--compressed"){
          this.input3 = str[parseInt(i)+1].replace("\"","").replace("\"","")
        }
      }
      this.headers = curl_head
      this.dialogVisible = false
    }
  },
};
</script>

<style >
.selects{
  width: 400px;
}
.response {
  text-align: left;
  width: 100%;
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
.el-select .el-input {
  width: 130px;
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
</style>