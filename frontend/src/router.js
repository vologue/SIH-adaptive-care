import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
      {
      path: '/login',
      name: 'login',
      component: () => import('./views/login.vue')
    },
    {
    path: '/SignUp',
    name: 'signup',
    component: () => import('./views/SignUp.vue')
  },


  ]
})
