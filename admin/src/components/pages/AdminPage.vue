<template>
  <v-flex xs6>
    <v-flex xs6>
      <MovieSearchForm :submit="searchMovies" />
    </v-flex>
    <div>
      <v-btn @click="clustering">clustering</v-btn>
    </div>
    <div>
      <span @click="selectTable">Movie</span> |
      <span @click="selectTable">User</span>
    </div>
    <router-view />
  </v-flex>
</template>

<script>
import { mapActions } from 'vuex';
import MovieSearchForm from '../common/MovieSearchForm'

export default {
  components: {
    MovieSearchForm,
  },
  methods: {
    ...mapActions('movie', ['searchMovies', 'clusteringMovies']),
    ...mapActions('user', ['clusteringUsers']),
    selectTable(e) {
      const keyword = e.target.innerHTML.toLowerCase()
      // if (keyword === 'movie') {
      //   this.searchMovies()
      // }
      this.$router.push({
        name: `${keyword}-list`
      })
    },
    clustering() {
      const params = {
        method: 'em',
        k: 5
      }
      if (this.$route.path === '/admin/movies') {
        this.clusteringMovies(params)
      } else {
        this.clusteringUsers(params)
      }
    }
  }
}
</script>

<style scoped>

</style>