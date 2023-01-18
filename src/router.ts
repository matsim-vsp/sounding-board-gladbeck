import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeIndex from '@/views/HomeIndex.vue'
import Imprint from '@/views/Imprint.vue'

Vue.use(VueRouter)

const latestRCalculator = '/r-calcs-v2/2021-01-24b'

const routes = [
  {
    path: '/:runId',
    component: () => import(/* webpackChunkName: "scenarios" */ '@/views/SoundingBoard.vue'),
  },
  {
    path: '/:runId/',
    component: () => import(/* webpackChunkName: "scenarios" */ '@/views/SoundingBoard.vue'),
  },
  {
    // catch-all back to home page
    path: '*',
    redirect: '/ccc',
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes, // native-like back/forward and top-of-page routing
  scrollBehavior(to, from, savedPosition) {
    if (to.path === from.path) return
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  },
})

export default router
