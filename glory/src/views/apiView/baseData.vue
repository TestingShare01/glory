<template>
  <div>
    <el-row type="flex" class="row-bg" justify="space-between">
      <el-col :span="8"
        ><div class="card">
          <div class="title">
            <span>API数量</span>
          </div>
          <div class="num">
            <div class="shuzi">
              <p class="p">接口数</p>
              <p class="pp">{{info.apiNum}}</p>
            </div>
            <div class="shuzi">
              <p class="p">执行数</p>
              <p class="pp">123</p>
            </div>
            <div class="shuzi">
              <p class="p">用例数</p>
              <p class="pp">{{info.caseNum}}</p>
            </div>
          </div>
        </div></el-col>

      <el-col :span="8"
        ><div class="card">
          <div class="title">
            <span>任务</span>
          </div>
          <div class="num">
            <div class="shuzi">
              <p class="p">任务数量</p>
              <p class="pp">{{info.taskNum}}</p>
            </div>
            <div class="shuzi">
              <p class="p">执行次数</p>
              <p class="pp">{{info.taskexecute}}</p>
            </div>
            <div class="shuzi">
              <p class="p">定时数量</p>
              <p class="pp">{{info.taskdingshi}}</p>
            </div>
          </div>
        </div></el-col
      >

      <el-col :span="8"
        ><div class="card">
          <div class="title">
            <span>项目</span>
          </div>
          <div class="num">
            <div class="shuzi">
              <p class="p">项目数</p>
              <p class="pp">{{info.xiangmu}}</p>
            </div>
            <div class="shuzi">
              <p class="p">模块数</p>
              <p class="pp">{{info.mokuai}}</p>
            </div>
      
          </div>
        </div></el-col
      >
    </el-row>

  </div>
</template>

<script>
import {getNums} from "@/api/common.js"
export default {
    created(){
        this.getdata()
    },
    data(){
        return{
            info:{
                apiNum:0,
                caseNum:0,
                mokuai:0,
                taskNum:0,
                taskdingshi:0,
                taskexecute:0,
                xiangmu:0
            }
        }
    },
    methods:{
        getdata(){
            getNums().then(res=>{
                console.log(res.data[0])
                this.info = res.data[0]
            })
        }
    }
};
</script>

<style>
.data {
  width: 100%;
  height: 100%;
}

.shuzi p {
  color: white;
  font-weight: 600;
}
.pp {
  font-weight: 700;
  font-size: 20px;
}

.title span {
  margin-left: 10px;
}
.card {
  height: 156px;
  width: 430px;
  background-image: linear-gradient(to left, #6a6aff, #ca8eff);
}
.title {
  width: 100%;
  height: 50px;
  /* background-color: aqua; */
  border-bottom: 2px solid white;
  text-align: left;
  line-height: 50px;
  font-weight: 600;
  font-size: 15px;
  color: white;
}
.num {
  width: 100%;
  height: 100%;
  /* background-color: blueviolet; */
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}
.shuzi {
  height: 100px;
  width: 60px;
  margin-top: 10px;
}



.el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
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
</style>