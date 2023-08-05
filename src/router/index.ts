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
      path: '/set',
      name: 'set',
      component: () => import('@/views/SetView.vue')
    }
  ]
})

export default router
