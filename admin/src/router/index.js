import Vue from 'vue'
import VueRouter from 'vue-router'
import AdminPage from '../components/pages/AdminPage'
import MovieList from '../components/movie/MovieList'
import UserList from '../components/user/UserList'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/',
      redirect: 'admin'
    },
    { path: '/admin', 
      component: AdminPage, 
      name: 'admin',
      children: [
        {
          path: 'movies',
          component: MovieList,
          name: 'movie-list'
        },
        {
          path: 'users',
          component: UserList,
          name: 'user-list'
        }
      ]
    },
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router