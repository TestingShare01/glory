<template>
  <div>
    <div>
      <el-table :data="tableData" style="width: 100%" size="small">

        <el-table-column label="ID" prop="id" width="100">
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

        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" @click="detail(scope.row.id)"
              >详情</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>
<script>
import {getReport} from "@/api/common.js"
export default {
    created(){
        this.get_list()
    },
    data(){
        return{
            tableData: []
        }
    },
    methods:{
        get_list(){
            let id = this.$route.query.id;
            console.log(id)
            getReport(id).then(res=>{
                console.log(res.data.data_list)
                this.tableData = res.data.data_list
            })
        },
        
        detail(id){
            this.$router.push("/detail?id="+id)
        }
 
    }
}
</script>

<style>

</style>