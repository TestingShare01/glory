<template>
  <el-table
    :data="tableData"
    style="width: 100%"
    >
    <el-table-column
      fixed
      prop="id"
      label="ID"
      width="100">
    </el-table-column>
    <el-table-column
      prop="keyName"
      label="字段"
      width="100">
    </el-table-column>
    <el-table-column
      prop="values"
      label="值"
      width="500"
      :show-overflow-tooltip="true">
    </el-table-column>
    <el-table-column
      prop="keyRule"
      label="规则"
      width="120">
    </el-table-column>
    <el-table-column
      prop="env"
      label="环境"
      width="300">
      <template slot-scope="scope">
        <el-tag effect="dark" :type="scope.row.env === '测试环境' ? 'success' : 'warning'" size="small"
>{{scope.row.env}}</el-tag>
      </template>
    </el-table-column>
    <el-table-column
      prop="updatetime"
      label="更新时间"
      width="300">
    </el-table-column>
    <el-table-column
      prop="caseid"
      label="CaseId"
      width="120">
    </el-table-column>
    <el-table-column
      fixed="right"
      label="操作"
      width="120">
      <template slot-scope="scope">
        <el-button
          @click.native.prevent="deleteRow(scope.$index, tableData)"
          type="text"
          size="small">
          移除
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import {getTiqu} from "@/api/common.js"
  export default {
    created(){
      this.getGoladList()
    },
    methods: {
      deleteRow(index, rows) {
        rows.splice(index, 1);
      }
    },
    data() {
      return {
        tableData:[]
      }
    },
    methods:{
      getGoladList(){
        getTiqu().then(res=>{
          console.log(res.data)
          this.tableData = res.data
        })
      }
    }
  }
</script>