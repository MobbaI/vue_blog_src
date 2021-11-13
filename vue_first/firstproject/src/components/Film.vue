<template>
    <el-main id="filmScroll">
        <el-backtop target="#filmScroll" style="color: black"></el-backtop>
        <!-- <button class="btn" @click="test">test</button> -->
        <div class="countries" v-for="filmC in filmInfo" :key="filmC.country">
            <h1>{{filmC.country}}</h1>
            <div class="country">
                <div class="film" v-for="film in filmC.film" :key="film.name" @click="showDesc(filmC.country, film.name)">
                    <div class="filmImage">
                        <img :src="film.imageUrl">
                    </div>
                    <span class="filmName"><p>{{film.name}}</p></span>
                </div>
            </div>
            <div class="clearFloat"></div>
        </div>
    </el-main>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: 'Film',
    data() {
        return {
            scroll: 0,
        };
    },
    computed: {
        ...mapState(['filmInfo'])
    },
    methods: {
        showDesc(country, name) {
            console.log(name)
            this.$router.push({
                path: '/film/f',
                query: {
                    country,
                    name
                }
            })
        },

        // test() {
        //     console.log(document.querySelector('#filmScroll').scrollTop)
        // }
    },
    beforeRouteLeave(to, from, next) {
        console.log('haha')
        this.scroll = document.querySelector('#filmScroll').scrollTop
        next()
    },
    activated() {
        document.querySelector('#filmScroll').scrollTop = this.scroll
    }
}
</script>

<style scoped>
/* div {
    border: 1px solid black;
} */
.btn {
    position: fixed;
    bottom: 100px;
    right: 50px;
}

.countries {
    margin-bottom: 110px;
}

.countries h1 {
    margin-left: 20px;
}

.country {
    min-width: 850px;
    /* max-width: 1900px; */
}

.film {
    float: left;
    width: 220px;
    height: 380px;
    margin: 30px 100px 30px 90px;
    /* background-color: blueviolet; */
}

.filmImage {
    height: 330px;
    /* background-color: blue; */
}

.filmImage img {
    width: 100%;
}

.filmName {
    height: 50px;
}

.filmName p {
    text-align: center;
    margin: 5px 0 0 0;
    /* font-weight: bold; */
}

.film:hover {
    cursor: pointer;
}

.clearFloat {
    clear: both;
}
</style>