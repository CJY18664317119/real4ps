import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/pages/HomePage.vue'
import ProblemOrientationForm from '@/pages/ProblemOrientationForm.vue'
import ProblemOrientationList from '@/pages/ProblemOrientationList.vue'
import NotFound from '@/pages/NotFound.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/problem-orientation',
    name: 'ProblemOrientation',
    component: ProblemOrientationForm
  },
  {
    path: '/problem-list',
    name: 'ProblemList',
    component: ProblemOrientationList
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: NotFound
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router