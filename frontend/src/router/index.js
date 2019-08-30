import Vue from 'vue'
import VueRouter from 'vue-router'
<<<<<<< HEAD

// Pages
import EmptyPage from '../components/pages/EmptyPage'
=======
import BoardingPage from '../components/pages/BoardingPage.vue'
>>>>>>> dee5dbd7e4e215749d2085c01445885ed350e79b
import MovieSearchPage from '../components/pages/MovieSearchPage'
import UserSearchPage from '../components/pages/UserSearchPage'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: BoardingPage, name: 'home' },
    { path: '/movies/search', component: MovieSearchPage, name: 'movie-search' },
    { path: '/users/search', component: UserSearchPage, name: 'user-search' },
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router