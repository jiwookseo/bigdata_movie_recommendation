<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
      <v-flex v-for="movie in movieList" :key="movie.id" pa-2>
        <movie-info-bar
          :id="movie.id"
          :img="movie.img"
          :title="movie.title"
          :genres="movie.genres"
          :rating="movie.rating"
          :view-cnt="movie.viewCnt"
        >
        </movie-info-bar>
      </v-flex>
      <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import MovieInfoBar from './MovieInfoBar'

export default {
  components: {
    MovieInfoBar
  },
  props: {
    movieListCards: {
      type: Array,
      default: () => new Array(),
    },
  },
  data: () => ({
    cardsPerPage: 10,
    page: 1,
  }),
  computed: {
    ...mapState('movie', ['movieList']),
    // pagination related variables
    movieListEmpty: function() {
      return this.movieListCards.length === 0;
    },
    maxPages: function() {
      return Math.floor((this.movieListCards.length + this.cardsPerPage - 1) / this.cardsPerPage)
    },
    movieListCardsSliced: function() {
      return this.movieListCards.slice(this.cardsPerPage * (this.page - 1), this.cardsPerPage * this.page)
    },
  }
};
</script>