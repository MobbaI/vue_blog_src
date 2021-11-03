<template>
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu :default-openeds="['2']">
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-lollipop"></i>导航一</template>
        <el-menu-item index="1-1">关于</el-menu-item>
        <el-menu-item index="1-2">设备</el-menu-item>
        <el-menu-item index="1-3">？？？</el-menu-item>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-apple"></i>iOS</template>
        <el-menu-item index="2-1" @click="toAppleAbout">关于</el-menu-item>
        <el-menu-item index="2-2" @click="toApple">设备</el-menu-item>
        <el-menu-item index="2-3">？？？</el-menu-item>
      </el-submenu>
    </el-menu>
  </el-aside>
</template>

<script>
export default {
  name: "Aside",
  methods: {
    toAppleAbout() {
        this.$router.push({
            path: '/appleabout'
        })
    },
    toApple() {
        this.$router.push({
            name: 'iOS'
        })
    }
  }
};
</script>

<style>
/* .el-aside {
    height: 100vh;
} */
</style>