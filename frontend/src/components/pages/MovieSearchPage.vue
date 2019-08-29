<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs8>
        <div class="display-2 pa-10">영화 검색</div>
        <MovieSearchForm :submit="searchMovies" />
      </v-flex>
      <!-- 검색 결과 -->
      <v-flex xs8>
        <MovieList :movie-list-cards="movieList" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import MovieSearchForm from "../MovieSearchForm";
import MovieList from "../MovieList";

export default {
  components: {
    MovieList,
    MovieSearchForm
  },
  data: () => ({}),
  computed: {
    ...mapState({
      movieList: state => state.data.movieSearchList
    })
  },
  methods: {
    ...mapActions("data", ["searchMovies"]),
  }
};
</script>
