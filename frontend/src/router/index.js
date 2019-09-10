import Vue from 'vue'
import VueRouter from 'vue-router'
import BoardingPage from '../components/pages/BoardingPage.vue'
import ProfilePage from '../components/pages/ProfilePage'
import DetailPage from '../components/pages/DetailPage'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: BoardingPage, name: 'home' },
    { path: '/profile/:username', component: ProfilePage, name: 'profile', },
    { path: '/movie/:id', component: DetailPage, name: 'detail'},
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router