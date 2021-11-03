<template>
  <div id="app">
    <el-container direction="vertical" style="height: 500px; border: 1px solid #eee">
      <Header />
      <el-container class="th_container">
        <Aside />
        <el-main>
          <router-view></router-view>
          <!-- <Android :tableData="tableData" /> -->
        </el-main>
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

#app {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
