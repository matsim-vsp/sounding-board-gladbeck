import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

// könntet Ihr das bitte so bauen, dass die URL https://vsp.berlin/sounding-board/ nach https://vsp.berlin/sounding-board/current/config

const routes = [
  {
    path: '/:runId/:config',
    component: () => import(/* webpackChunkName: "scenarios" */ '@/views/SoundingBoard.vue'),
  },
  {
    path: '/:runId/:config/',
    component: () => import(/* webpackChunkName: "scenarios" */ '@/views/SoundingBoard.vue'),
  },
  {
    path: '/:runId/',
    redirect: '/:runId/config',
    component: () => import(/* webpackChunkName: "scenarios" */ '@/views/SoundingBoard.vue'),
  },
  {
    path: '/:runId/',
    redirect: '/:runId/config',
    component: () => import(/* webpackChunkName: "scenarios" */ '@/views/SoundingBoard.vue'),
  },
  {
    // catch-all back to home page
    path: '*',
    redirect: '/current/config',
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
