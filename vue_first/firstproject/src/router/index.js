import VueRouter from "vue-router"
import AppleAbout from '../components/AppleAbout.vue'
import iOS from '../components/iOS.vue'
import Echarts from '../components/Echarts.vue'
import Actor from '../components/Actor.vue'
import Film from '../components/Film.vue'
import FilmDesc from '../components/FilmDesc.vue'


const router = new VueRouter({
    routes:[
        {
            path: '/',
            component: () => import('@/components/Home.vue')
        },
        {
            path: '/actor',
            component: Actor,
            meta: {
                title: '演员简介'
            }
        },
        {
            path: '/film',
            component: Film,
            meta: {
                title: '影片'
            }
        },
        {
            path: '/film/f',
            component: FilmDesc,
            props($route) {
                return {
                    country: $route.query.country,
                    name: $route.query.name
                }
            },
            meta: {
                title: '影片简介'
            }
        },
        {
            path: '/appleabout',
            component: AppleAbout,
            meta: {
                title: 'Apple简介'
            }
        },
        {
            name: 'iOS',
            path: '/iOS',
            component: iOS,
            meta: {
                title: 'Apple设备'
            }
        },
        {
            name: 'Echarts',
            path: '/Echarts',
            component: Echarts,
            meta: {
                title: 'Echarts练习'
            }
        }
    ]
})

router.afterEach((to) => {
    document.title = to.meta.title || 'Y'
});

export default router