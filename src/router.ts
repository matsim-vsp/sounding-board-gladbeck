import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeIndex from '@/views/HomeIndex.vue'
import Imprint from '@/views/Imprint.vue'

Vue.use(VueRouter)

const latestRCalculator = '/r-calcs-v2/2021-01-24b'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeIndex,
  },
  {
    path: '/imprint',
    name: 'Imprint',
    component: Imprint,
  },
  {
    path: '/calculators',
    component: () => import(/* webpackChunkName: "calculators" */ '@/views/Calculators.vue'),
  },
  {
    path: '/scenarios/:runId',
    component: () => import(/* webpackChunkName: "scenarios" */ '@/views/ScenarioCalculator.vue'),
  },
  {
    path: '/calculator',
    redirect: latestRCalculator,
  },
  {
    path: '/r-calc',
    redirect: latestRCalculator,
  },
  {
    path: '/r-calcs-v1/:rcalc',
    component: () => import(/* webpackChunkName: "r-calcs" */ '@/views/RCalculator.vue'),
  },
  {
    path: '/r-calcs-v2/:rcalc',
    component: () => import(/* webpackChunkName: "r-calcs" */ '@/views/RCalculatorNew.vue'),
  },
  {
    path: '/risk-calcs/:rcalc',
    component: () => import(/* webpackChunkName: "risk-calcs" */ '@/views/RiskCalculator.vue'),
  },
  {
    path: '/mobility',
    component: () => import(/* webpackChunkName: "mobility" */ '@/views/MobilityPage.vue'),
  },
  {
    path: '/mobility/duration',
    component: () => import(/* webpackChunkName: "mobility" */ '@/views/MobilityPage.vue'),
  },
  {
    path: '/mobility/distance',
    component: () => import(/* webpackChunkName: "mobility" */ '@/views/MobilityPage.vue'),
  },
  {
    path: '/mobility/proportion-mobile-persons',
    component: () => import(/* webpackChunkName: "mobility" */ '@/views/MobilityPage.vue'),
  },
  {
    path: '/mobility-counties',
    component: () =>
      import(/* webpackChunkName: "mobility" */ '@/views/MobilityPageLandkreise.vue'),
  },
  {
    path: '/mobility-counties/duration/week',
    component: () =>
      import(/* webpackChunkName: "mobility" */ '@/views/MobilityPageLandkreise.vue'),
  },
  {
    path: '/mobility-counties/distance/week',
    component: () =>
      import(/* webpackChunkName: "mobility" */ '@/views/MobilityPageLandkreise.vue'),
  },
  {
    path: '/mobility-counties/proportion-mobile-persons/week',
    component: () =>
      import(/* webpackChunkName: "mobility" */ '@/views/MobilityPageLandkreise.vue'),
  },
  {
    path: '/mobility-counties/duration/weekday',
    component: () =>
      import(/* webpackChunkName: "mobility" */ '@/views/MobilityPageLandkreise.vue'),
  },
  {
    path: '/mobility-counties/distance/weekday',
    component: () =>
      import(/* webpackChunkName: "mobility" */ '@/views/MobilityPageLandkreise.vue'),
  },
  {
    path: '/mobility-counties/proportion-mobile-persons/weekday',
    component: () =>
      import(/* webpackChunkName: "mobility" */ '@/views/MobilityPageLandkreise.vue'),
  },
  {
    path: '/mobility-counties/duration/weekend',
    component: () =>
      import(/* webpackChunkName: "mobility" */ '@/views/MobilityPageLandkreise.vue'),
  },
  {
    path: '/mobility-counties/distance/weekend',
    component: () =>
      import(/* webpackChunkName: "mobility" */ '@/views/MobilityPageLandkreise.vue'),
  },
  {
    path: '/mobility-counties/proportion-mobile-persons/weekend',
    component: () =>
      import(/* webpackChunkName: "mobility" */ '@/views/MobilityPageLandkreise.vue'),
  },
  {
    path: '/mobility-counties/nightly-activity/week',
    component: () =>
      import(/* webpackChunkName: "mobility" */ '@/views/MobilityPageLandkreise.vue'),
  },
  {
    path: '/mobility-counties/nightly-activity/weekday',
    component: () =>
      import(/* webpackChunkName: "mobility" */ '@/views/MobilityPageLandkreise.vue'),
  },
  {
    path: '/mobility-counties/nightly-activity/weekend',
    component: () =>
      import(/* webpackChunkName: "mobility" */ '@/views/MobilityPageLandkreise.vue'),
  },
  {
    path: '/*',
    component: () => import(/* webpackChunkName: "runviewer" */ '@/views/RunPage.vue'),
  },
  {
    // catch-all back to home page
    path: '*',
    redirect: '/',
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
