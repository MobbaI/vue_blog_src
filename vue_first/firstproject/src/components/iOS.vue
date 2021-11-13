<template>
  <el-main>
    <!-- <el-col :span="3"> -->
    <el-select v-model="value" clearable placeholder="请选择">
      <el-option
        v-for="item in options"
        :key="item.id"
        :label="item.label"
        :value="item.id"
      >
      </el-option>
    </el-select>
    <el-input ref="input_search" v-model="inputSearch" placeholder="请输入内容" style="margin-left: 10px" :disabled="!value"></el-input>
    <el-tag style="float: right">数量：{{tableData.length}}</el-tag>
    <!-- <el-button
      icon="el-icon-search"
      circle
      style="margin-left: 10px"
    ></el-button> -->
    <!-- </el-col> -->
    <el-table :data="tableData">
      <el-table-column prop="p_name" label="设备名称" width="170">
      </el-table-column>
      <el-table-column prop="size" label="屏幕尺寸(英寸)" width="120">
      </el-table-column>
      <el-table-column prop="resolution" label="分辨率" width="120">
      </el-table-column>
      <el-table-column prop="RAM" label="RAM" width="120"> </el-table-column>
      <el-table-column prop="CPU" label="CPU型号" width="120">
      </el-table-column>
      <el-table-column prop="Model" label="设备型号" width="120">
      </el-table-column>
      <el-table-column prop="OpenGL_ES" label="OpenGL ES" width="100" header-align="left" align="center">
      </el-table-column>
      <el-table-column prop="screen" label="屏幕属性"> </el-table-column>
    </el-table>
  </el-main>
</template>

<script>
export default {
  name: "iOS",
  data() {
    return {
      inputSearch: "",
      options: [{
          id: '001',
          label: '设备名称'
        }, {
          id: '002',
          label: '屏幕尺寸'
        }, {
          id: '003',
          label: '分辨率'
        }, {
          id: '004',
          label: 'RAM'
        }, {
          id: '005',
          label: 'CPU型号'
        }, {
          id: '006',
          label: '设备型号'
        }, {
          id: '007',
          label: 'OpenGL ES'
        }, {
          id: '008',
          label: '屏幕属性'
        }],
      value: '',
      tableData: []
    };
  },
  watch: {
    inputSearch(val) {
      if(this.value) {
        this.data_select(val)
      }
    },
    value() {
      this.inputSearch = ''
      this.data_select('')       
    }
  },
  methods: {
    data_select(val) {
      this.$axios({
        method: 'get',
        url: 'http://127.0.0.1:5000/dataSelect',
        params: {
          label: this.value,
          value: val
        }
        }).then((res) => {
        this.tableData = res.data.iOS
      })
    }
  },
  mounted() {
    this.$axios.get('http://127.0.0.1:5000/dataJson').then((res) => {
      this.tableData = res.data.iOS
    }, err => {
      console.log(err.message)
    })
  }
};
</script>

<style scoped>
.el-input {
  width: 200px;
}

.container {
  height: 100vm;
}
</style>