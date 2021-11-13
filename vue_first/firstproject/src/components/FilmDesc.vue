<template>
    <el-main>
        <div v-if="imageUrl" class="main_box">
            <div class="film_image">
                <img :src="imageUrl">               
            </div>
            <div class="film_desc">
                <h1>{{name}}</h1>
                <p>...</p>
            </div>
        </div>
        <div v-else class="noFilm"><h1>无影片信息</h1></div>
    </el-main>
</template>

<script>

export default {
    name: 'FilmDesc',
    props: ['country', 'name'],
    computed: {
        imageUrl(){
            return this.getImageUrl()
        }
    },
    methods: {
        getImageUrl() {
            for(const f of this.$store.state.filmInfo) {
                if(f.country === this.country) {
                    for(const i of f.film) {
                        if(i.name === this.name) return i.imageUrl
                    }
                }
            }
        }
    },
    mounted() {
        // const x = Object.entries(this.$store.state.filmInfo[0])
        // console.log(x)
    }
}
</script>

<style scoped>
/* div {
    border: 1px solid black;
} */

.main_box {
    /* border: 1px solid black; */
    display: flex;
    width: 1200px;
    height: 800px;
    position: relative;
    top: 30px;
    /* justify-content: space-around; */
    margin: 0 auto;
}

.noFilm {
    position: relative;
    text-align: center;
    top: 300px;
}

.film_image {
    flex: 1;
    /* text-align: right; */
    position: relative;
    /* right: 100px; */
}

.film_image img {
    height: 100%;
}

.film_desc {
    flex: 1;
    text-align: center;
}
</style>