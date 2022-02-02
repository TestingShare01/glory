<template>
  <div class="divs">
    <!-- 报告汇总 -->
    <div class="reportNum">
      <div class="report">测试报告</div>
      <el-row :gutter="20">
        <!-- 报告顶部信息汇总 -->
        <el-col :span="15">
          <el-row>
            <el-col>
              <h1>{{info.task_num}}</h1>
              <h4>执行者: {{info.zx_user}}</h4>
              <h6>开始时间: {{info.start_time}}</h6>
              <h5>结束时间: {{info.end_time}}</h5>
            </el-col>
          </el-row>
          <el-row type="flex" class="row-bg" justify="space-between">
            <el-col :span="5" class="divNum">
              <h3>总用例数</h3>
              <i class="el-icon-s-order iconclass" style="color:#AFEEEE	"></i><span class="numclass">{{info.api_num}}</span>
            </el-col>

            <el-col :span="5" class="divNum">
              <h3>通过数</h3>
              <i class="el-icon-circle-check iconclass" style="color:green"></i><span class="numclass">{{info.true_num}}</span>

            </el-col>

            <el-col :span="5" class="divNum">
              <h3>失败数</h3>
              <i class="el-icon-circle-close iconclass" style="color:red"></i><span class="numclass">{{info.false_num}}</span>

            </el-col>

            <el-col :span="5" class="divNum">
              <h3>执行耗时</h3>
              <i class="el-icon-odometer iconclass" style="color:#1E90FF;font-size:20px"></i><span class="numclass">{{info.expend_time}}</span>
            </el-col>

          </el-row>



        </el-col>


        <!-- 报告顶部图表 -->
        <el-col :span="9"><div class="grid-content bg-purple"></div></el-col>
      </el-row>
    </div>

    <!-- 报告用例页面 -->
    <div class="table_list">
      <div class="case"><p>用例列表</p></div>
      <el-table :data="tableData" style="width: 100%">
        <el-table-column type="expand">
          <template slot-scope="props">
            <p>{{ retJson(props.row.res) }}</p>
          </template>
        </el-table-column>
        <el-table-column label="名称" prop="name"> </el-table-column>
        <el-table-column label="状态" prop="status">
          <template slot-scope="scope">
            <el-tag
              effect="dark"
              size="small"
              :type="scope.row.status === '失败' ? 'danger' : 'success'"
              >{{ scope.row.status }}</el-tag
            >
          </template>
        </el-table-column>
        <el-table-column label="耗时(ms)" prop="expent_time"> </el-table-column>

        <el-table-column label="结果" prop="result"> </el-table-column>

        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              size="mini"
              @click="handleEdit(scope.row.caseid)"
              type="primary"
              >Case</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </div>

    
  </div>
</template>

<style scoped>
.case{
  background-color: #FFFFFF;
  width: 100%;
  height: 60px;
  text-align: left;
  font-size: 18px;
  font-weight: bold;
  border-bottom: 2px solid #ECEFF3;
  line-height: 60px;
  
}
.case p{
  margin-left: 10px;
}
.numclass{
  font-size: 25px;
  margin-left: 3px;
  font-weight: 600;
}
.iconclass{
  font-size: 30px;
}
.report{
  border-bottom: 2px solid #ECEFF3;
  text-align: left;
  height: 40px;
  line-height: 40px;
  font-size: 18px;
  font-weight:bold
}
.table_list{
  margin-top: 15px;
  margin-left: 20px;
  margin-right: 20px;
  border-radius: 5px;
}
.divs{
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  background-color: #ECEFF3;
}
.divNum{
  height: 100px;
}
.el-row{
  text-align: left;
}
.grid-content{
 
}
.reportNum {
  background-color: #FFFFFF;
  height: 330px;
  margin-left: 20px;
  margin-right: 20px;
  padding: 10px;
  margin-top: 20px;
  border-radius: 5px;
}
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
</style>

<script>
import { reportdetai } from "@/api/common.js";
import jsonView from "vue-json-views";

export default {
  created() {
    this.getreportdetail();
  },
  data() {
    return {
      tableData: [],
      info:{
        task_num:"",
        zx_user:"",
        start_time:"",
        end_time:"",
        api_num:0,
        true_num:0,
        false_num:0,
        expend_time:""

      }
    };
  },
  components: {
    jsonView,
  },
  methods: {
    // 获取列表数据
    getreportdetail() {
      let id = this.$route.query.id;
      console.log(id);
      reportdetai(id).then((res) => {
        this.tableData = res.data.reportList;
        this.info = res.data.info[0]
      });
    },

    //返回的数据显示json格式
    retJson(res) {
      return res;
    },

    //跳转case页面
    handleEdit(id) {
      this.$router.push("case?id=" + id);
    },
  },
};
</script>