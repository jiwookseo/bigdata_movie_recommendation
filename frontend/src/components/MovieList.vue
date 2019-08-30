<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout row class="layout">
      <v-flex v-for="card in movieListCardsSliced" :key="card.id" pa-2 xs8 sm8 md8 lg8 xl8>
        <MovieListCard
          :id="card.id"
          :img="card.img"
          :title="card.title"
          :genres="card.genres"
          :rating="card.rating"
          :view-cnt="card.viewCnt"
        />
      </v-flex>
      <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
    </v-layout>
  </v-container>
</template>

<script>
import MovieListCard from "./MovieListCard";

export default {
  components: {
    MovieListCard
  },
  props: {
    movieListCards: {
      type: Array,
      default: () => new Array()
    }
  },
  data: () => ({
    cardsPerPage: 10,
    page: 1
  }),
  computed: {
    // pagination related variables
    movieListEmpty: function() {
      return this.movieListCards.length === 0;
    },
    maxPages: function() {
      return Math.floor(
        (this.movieListCards.length + this.cardsPerPage - 1) / this.cardsPerPage
      );
    },
    movieListCardsSliced: function() {
      return this.movieListCards.slice(
        this.cardsPerPage * (this.page - 1),
        this.cardsPerPage * this.page
      );
    }
  }
};
</script>

<style>
.layout {
  justify-content: center;
}
</style>