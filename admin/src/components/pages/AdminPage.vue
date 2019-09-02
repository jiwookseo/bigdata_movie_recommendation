<template>
  <v-flex xs6>
    <v-flex xs6>
      <MovieSearchForm :submit="searchMovies" />
    </v-flex>
    <div>
      <v-btn @click="clustering">clustering</v-btn>
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
        method: 'km',
        k: 7
      }
      this.clusteringMovies(params)
    }
  }
}
</script>

<style scoped lang="scss">

</style>