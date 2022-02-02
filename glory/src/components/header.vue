<template>
  <div class="head">
    <h3>
      <a href="/" style="text-decoration: none; color: white">测试平台</a>
    </h3>

    <el-dropdown>
      <span class="el-dropdown-link">
        {{ username }}<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item>黄金糕</el-dropdown-item>
        <el-dropdown-item>狮子头</el-dropdown-item>
        <el-dropdown-item>螺蛳粉</el-dropdown-item>
        <el-dropdown-item disabled>双皮奶</el-dropdown-item>
        <el-dropdown-item divided>蚵仔煎</el-dropdown-item>
      </el-dropdown-menu>

    
    </el-dropdown>
  </div>
</template>

<script>
export default {
  props: ["username"],
};
</script>

<style scoped>
.item {
  margin-top: 10px;
  margin-right: 40px;
}
h3 {
  line-height: 5px;
  float: left;
  margin-left: 10px;
  color: white;
}
.el-dropdown-link {
  line-height: 40px;
  float: right;
}
.el-dropdown {
  float: right;
  margin-right: 20px;
}
</style>