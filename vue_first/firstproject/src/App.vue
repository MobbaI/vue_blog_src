<template>
  <div id="app">
    <el-container direction="vertical">
      <Header />
      <el-container class="th_container">
        <Aside />
        <keep-alive><router-view></router-view></keep-alive>
        <!-- <Android :tableData="tableData" /> -->
      </el-container>
    </el-container>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Aside from "./components/Aside.vue";
// import Android from "./components/Android.vue";

export default {
  name: "App",
  components: { Header, Aside },
  mounted() {
      this.$store.dispatch('getFilmInfo')
  }
};
</script>

<style>
.el-header {
  background-color: #93d4d6;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}

html,
body,
#app,
.el-container {
  padding: 0;
  margin: 0;
  height: 100%;
}

.th_container {
  height: calc(100% - 60px);
}
</style>
