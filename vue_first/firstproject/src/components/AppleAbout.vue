<template>
  <el-main>
    <div class="text">
      <h2>iOS</h2>
      <p>{{appleText}}</p>
    </div>
    <img id="apple" src="../assets/images/ios.jpg">
    <div class="image">
      <img  ref="hahaha" src="../assets/images/ios.jpg">
      <img src="../assets/images/ios.jpg">
      <img src="../assets/images/ios.jpg">
      <img src="../assets/images/ios.jpg">
      <img src="../assets/images/ios.jpg">
      <img src="../assets/images/ios.jpg">
    </div>
  </el-main>
</template>

<script>
// import elementResizeDetetorMaker from 'element-resize-detector'

export default {
  name: 'AppleAbout',
  data() {
    return {
      appleText: 'iOS是由苹果公司开发的移动操作系统。苹果公司最早于2007年1月9日的Macworld大会上公布这个系统，最初是设计给iPhone使用的，后来陆续套用到iPod touch、iPad上。iOS与苹果的macOS操作系统一样，属于类Unix的商业操作系统。原本这个系统名为iPhone OS，因为iPad，iPhone，iPod touch都使用iPhone OS，所以2010年WWDC上宣布改名为iOS（iOS为美国Cisco公司网络设备操作系统注册商标，苹果改名已获得Cisco公司授权）。',
    };
  },
  // computed: {
  //   hahahaHeight() {
  //     return this.$refs.hahaha.height
  //   }
  // },
  // watch: {
  //   hahahaHeight(val) {
  //     console.log(val)
  //   }
  // },
  // mounted() {

  // }
};
</script>

<style scoped>
.text {
  font-size: 17px;
  text-indent: 34px;
  line-height: 2;
}

.image {
  float: left;
}

.image img,
.text,
#apple {
  float: left;
  width: 50%;
}
</style>