import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/HomeView.vue')
    },
    {
      path: '/sets',
      name: 'sets',
      component: () => import('@/views/StudySetsView.vue')
    },
    {
      path: '/sets/:user',
      name: 'sets-user',
      component: () => import('@/views/StudySetsView.vue')
    },
    {
      path: '/set/:id',
      name: 'set',
      component: () => import('@/views/SetView.vue')
    }
  ]
})

export default router
