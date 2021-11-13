<template>
  <el-header style="text-align: right; font-size: 17px">
    <span class="header_title" style="margin-right: 17px">Hello Vue</span>
    <el-button icon="el-icon-house" circle style="margin-right: 15px" @click="goHome"></el-button>
  </el-header>
</template>

<script>
export default {
  name: "Header",
  methods: {
    goHome(){
      this.$router.push({
        path: '/'
      })
    }
  }
};
</script>

<style scoped>
.el-header {
  background-color: black;
  line-height: 60px;
}

.header_title {
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  color: #FFFFFF;
}
</style>