<template>
  <v-flex xs6>
    <v-flex xs6>
      <MovieSearchForm :submit="searchMovies" />
    </v-flex>
    <div>
      <v-btn @click="clustering">clustering</v-btn>
      <v-btn @click="check">check</v-btn>
    </div>
    <div>
      <span @click="showItemList">Movie</span> |
      <span @click="showItemList">User</span>
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
    showItemList(e) {
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
    },
    check() {
      console.log(this.$route.path)
    }
  }
}
</script>

<style scoped>

</style>