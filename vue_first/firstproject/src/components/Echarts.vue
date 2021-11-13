<template>
    <el-main>
        <div ref="echarts_box" class="echarts_box"></div>
    </el-main>
</template>

<script>
import * as echarts from 'echarts'

export default {
    name: 'Echarts',
    data() {
        return {
            property: 'value',
        }
    },
    mounted() {
        const mCharts = echarts.init(this.$refs.echarts_box)
        const option = {
            xAxis: {
                type: 'category',
                data: ['张三', '李四', '王五'],
            },
            yAxis: {
                type: 'value'
            },
            tooltip: {
                trigger: 'item',
                // triggerOn: 'click'
            },
            legend: {
                data: ['语文', '数学']
            },
            series: [
                {
                name: '语文',
                type: 'bar',
                data: [85, 92, 77],
                // label: {
                //     show: true
                // }
                },
                {
                name: '数学',
                type: 'bar',
                data: [137, 97, 98],
                // label: {
                //     show: true
                // }
                },
            ]
        }
        mCharts.setOption(option)
        window.onresize = mCharts.resize
    }
}
</script>

<style>
.echarts_box {
    width: 50%;
    height: 600px;
    margin: 100px auto;
    border: 1px solid black;
    min-width: 300px;
}
</style>