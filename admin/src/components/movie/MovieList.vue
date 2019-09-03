<template>
    <div class="item-list-container">
      <div v-for="(movie, idx) in movieList" v-if="idx < 10" :key="movie.id">
        <movie-info-bar
          :id="movie.id"
          :img="movie.img"
          :title="movie.title"
          :genres="movie.genres"
          :rating="movie.rating"
          :view-cnt="movie.viewCnt"
        >
        </movie-info-bar>
      </div>
    </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import MovieInfoBar from './MovieInfoBar'

export default {
  components: {
    MovieInfoBar
  },
  computed: {
    ...mapState('movie', ['movieList']),
  }
};
</script>

<style scoped lang="scss">
.item-list-container {
  padding: 3vh 2vw;
}
</style>