<template>
  <div class="recommended-movies-container">
    <div class="recommended-movies--header">
      맞춤 추천 영화
    </div>
    <div class="recommended-movies--movie-container" v-for="movie in recommendedMovies">
      <div class="recommended-movies--movie-poster">
        <img :src="movie.poster" height="195" width="150" />
      </div>
      <div class="recommended-movies--movie-information">
        <div>
          {{ movie.title }}
        </div>
        <div>
          장르 | {{ movie.genres_array[0] }}
        </div>
        <div>
          평점 | {{ movie.avg_rating }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  props: ['username'],
  computed: {
    ...mapGetters('user', ["recommendedMovies"])
  },
  mounted() {
    this.$store.dispatch("user/getRecommendedMovies", this.username);
  }
}
</script>

<style lang="scss" scoped>
.recommended-movies-container {
  color: #fff;
  width: 100%;

  .recommended-movies--header {
    margin: 10px 0 10px 0;
    padding: 0 0 0 30px;
    font-size: 28px;
    font-weight: 700;
  }
}

.recommended-movies--movie-container {
  margin: 0 0 0 10px;
  padding: 2%;
  width: 100%;
  display: flex;
  
  .recommended-movies--movie-information {
    padding: 2%;

    div {
      margin: 0 0 10px 0;
    }
  }
}
</style>