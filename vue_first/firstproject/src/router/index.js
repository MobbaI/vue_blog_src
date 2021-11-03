import VueRouter from "vue-router"
import AppleAbout from '../components/AppleAbout.vue'
import iOS from '../components/iOS.vue'


const router = new VueRouter({
    routes:[
        {
            path: '/',
            component: () => import('@/components/Home.vue')
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
            path: '/iOS/',
            component: iOS,
            meta: {
                title: 'Apple设备'
            }
        }
    ]
})

router.afterEach((to) => {
    document.title = to.meta.title || 'Y'
});

export default router