<template>
  <div class="divbody">

    <div class="nums">
      <el-row :gutter="20">
        <el-col :span="6" >
          <div class="div_num">
            <p class="z_num" style="color:#2894FF	">{{zx_num}}</p>
            <p class="z_xiao_num">报告数</p>
          </div>
        </el-col>

        <el-col :span="6" >
          <div class="div_num">
            <p class="z_num" style="color:#9F35FF">{{api_num}}</p>
            <p class="z_xiao_num">接口执行数</p>
          </div>
        </el-col>

        <el-col :span="6" >
          <div class="div_num">
            <p class="z_num" style="color:#00BB00">{{true_num}}</p>
            <p class="z_xiao_num">正确数</p>
          </div>
        </el-col>

        <el-col :span="6" >
          <div class="div_num">
            <p class="z_num" style="color:#FF0000	">{{false_num}}</p>
            <p class="z_xiao_num">错误数</p>
          </div>
        </el-col>
       
      </el-row>
    </div>

    <div class="bottom_table">
      <el-table :data="tableData" style="width: 100%" size="small">
        <el-table-column label="ID" prop="id" width="100"> </el-table-column>

        <el-table-column label="任务名称" prop="task_num" width="150">
        </el-table-column>

        <el-table-column label="正确率" prop="accuracy" width="150">
        </el-table-column>

        <el-table-column label="执行总数" prop="num" width="150">
        </el-table-column>

        <el-table-column label="正确数" prop="true_num" width="150">
        </el-table-column>

        <el-table-column label="错误数" prop="false_num" width="150">
        </el-table-column>
        <el-table-column label="执行者" prop="zx_user" width="150">
        </el-table-column>

        <el-table-column label="耗时" prop="expend_time" width="150">
        </el-table-column>

        <el-table-column label="执行时间" prop="createtime" width="180">
        </el-table-column>

        <el-table-column label="执行者" prop="zx_user" width="180">
        </el-table-column>

        <el-table-column label="操作" fixed="right">
          <template slot-scope="scope">
            <el-button size="mini" @click="detail(scope.row.id)"
              >详情</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </div>

    <div class="pages">
      <el-pagination
        background
        layout="prev, pager, next"
        :total="count"
        page-size="20"
        class="fenye"
        @current-change="handleCurrentChange"
      >
      </el-pagination>
    </div>
  </div>
</template>
<script>
import { getReport } from "@/api/common.js";
export default {
  created() {
    this.get_list();
  },
  data() {
    return {
      tableData: [],
      count: 0,
      zx_num:0,
      api_num:0,
      true_num:0,
      false_num:0,
    };
  },
  methods: {
    get_list() {
      let id = this.$route.query.id;
      let page = this.$route.query.page;
      getReport(id, page).then((res) => {
        console.log(res.data);
        if (res.data.code === 0) {
          this.tableData = res.data.data_list;
          this.count = res.data.countNum;
          res.data.num_list.forEach(element => {
            if(element.type ==="report"){
              this.zx_num = element.num
            }else if(element.type === "apiNum"){
              this.api_num = element.num
            }else if(element.type === "trueApi"){
              this.true_num = element.num
            }else if(element.type === "falseApi"){
              this.false_num = element.num
            }
          });
        }
      });
    },

    detail(id) {
      this.$router.push("/detail?id=" + id);
    },

    handleCurrentChange(val) {
      let id = this.$route.query.id;
      getReport(id, val).then((res) => {
        if (res.data.code === 0) {
          this.tableData = res.data.data_list;
          this.count = res.data.countNum;
        }
      });
    },
  },
};
</script>

<style scoped>
.z_xiao_num{
  margin-top: 0px;
  color:#8E8E8E	
}
.z_num{
  font-size: 50px;
  font-weight: 700;
  margin-top: 0;
  margin-bottom: 0;
}
.div_num{
  margin-top: 10px;
  height: 120px;
  background-color: white;
  padding: 20px;
}
.fenye {
  float: right;
  margin-top: 10px;
}
.pages {
  height: 50px;
  margin-left: 10px;
  margin-right: 10px;
  background-color: white;
}
.divbody {
  background-color: #e7ebf0;
}
.nums {
  height: 150px;
  /* background-color: beige; */
  margin-left: 10px;
  margin-right: 10px;
  /* margin-bottom: 10px; */

}
.bottom_table {
  overflow: visible;
  /* position:absolute; */
  bottom: 50px;
  margin-left: 10px;
  margin-right: 10px;
}
/* .pages{
    bottom: 0px;
    right: 0px;
    display: flex;
    height: 40px;
    margin-top: 20px;
    float: right;
    
} */


</style>