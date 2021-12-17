<template>
  <div class="navigation">
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      :router="true"
       background-color="#545c64"
             text-color="#fff"
    style="width:100%;text-align:left"
    >
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>API自动化</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="/project">项目管理</el-menu-item>
          <el-menu-item index="1-2">选项2</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>导航二</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="1-1">选项1</el-menu-item>
          <el-menu-item index="1-2">选项2</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
  
    </el-menu>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>