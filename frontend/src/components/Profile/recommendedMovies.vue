<template>
  <div class="recommended-movies-container">
    <div class="recommended-movies--header">
      맞춤 추천 영화
    </div>
    <div class="recommended-movies--movie-container" v-for="movie in recommendedMovies">
      <div class="recommended-movies--movie-poster">
        <img 
          :src="movie.poster || 
          'https://files.slack.com/files-pri/TMJ2GPC23-FMF2L2DQA/599637c326f7d273826d.jpg'" height="195" width="150" />
      </div>
      <div class="recommended-movies--movie-information">
        <div class="recommended-movies--movie-title">
          <p class="txt-orange">{{ movie.title }}</p>
        </div>
        <div class="recommended-movies--movie-genres">
          <span v-for="genre in movie.genres_array">
            {{ genre }}
          </span>
        </div>
        <div class="recommended-movies--movie-rating">
          <span>평점</span>
          <span>{{ movie.avg_rating }}</span>
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
  display: flex;
  width: 100%;
  
  .recommended-movies--movie-information {
    box-sizing: border-box;
    width: calc(100% - 150px);
    padding: 2%;

    .recommended-movies--movie-title {
      font-size: 20px;
      font-weight: 700;
      margin: 0 0 20px 0;
    }
  }
}

.recommended-movies--movie-genres {
  margin: 0 0 15px 0;
  span {
    font-size: 12px;
    font-family: 'Jua';
    font-weight: 500;
    text-transform: uppercase;
    border: 2px solid #fff;
    border-radius: 5px;
    padding: 5px 10px;
  }
  span + span {
    margin-left: 10px;
  }
}

.recommended-movies--movie-rating {
  margin: 0 0 15px 0;
  padding: 0 0 0 5px;
  span {
    font-family: 'Jua';
    &:first-child {
      font-weight: 500;
    }
  }
  span + span {
    margin-left: 15px;
  }
}
</style>