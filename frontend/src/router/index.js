import Vue from 'vue'
import VueRouter from 'vue-router'
import BoardingPage from '../components/pages/BoardingPage.vue'
import MovieSearchPage from '../components/pages/MovieSearchPage'
import UserSearchPage from '../components/pages/UserSearchPage'
import ProfilePage from '../components/pages/ProfilePage'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: BoardingPage, name: 'home' },
    { path: '/movies/search', component: MovieSearchPage, name: 'movie-search' },
    { path: '/users/search', component: UserSearchPage, name: 'user-search' },
    { path: '/profile/:username', component: ProfilePage, name: 'profile', },
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router