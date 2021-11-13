<template>
    <el-main>
        <!-- <button @click="test">点我测试</button> -->
        <div class="actor" v-for="info in actorInfo" :key="info.name">
            <div class="actor_image">
                <img :src="info.imageUrl" alt="none">               
            </div>
            <div class="actor_intro">
                <h1 @click="test">{{info.name}}</h1>
                <p>{{info.introduction}}</p>
            </div>
        </div>
    </el-main>
</template>

<script>

export default {
    name: 'Actor',
    data() {
        return {
            actorInfo: []
        }
    },
    methods: {
        test() {
            console.log(this.actorInfo)
        }
    },
    mounted() {
        this.$axios.get('actor.json').then(res => {
            this.actorInfo = res.data
        }, err => {
            console.log(err.message)
        })
    }
}
</script>

<style scoped>
/* div {
    border: 1px solid black;
} */

.actor {
    display: flex;
    height: 540px;
    min-width: 800px;
    margin-top: 150px;
    margin-bottom: 200px;
}

.actor_image {
    display: flex;
    width: 50%;
    justify-content: center;
    align-items: center;
}

.actor_image img {
    height: 90%;
}

.actor_intro {
    flex: 1;
    margin: auto 100px auto 10px;
}

.actor_intro h1 {
    text-align: center;    
}

.actor_intro h1:hover{
    cursor: pointer;    
}

.actor_intro p {
    text-indent: 34px;
    letter-spacing: 1.5px;
    line-height: 160%;
}
</style>