<template>
  <div class="item-list-container">

    <!-- Data List -->
    <div v-for="(movie, idx) in dataList" v-if="idx+1 <= currentPage*10 && idx+1 > (currentPage-1)*10" :key="`movie${movie.id}`">
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

    <!-- Page Buttons -->
    <div class="page-buttons-container">
      <div v-show="index > 1" @click="showFirstPageList" class="page-button">
        <i class="fas fa-backward"></i>
      </div>

      <div v-show="index > 1" @click="showPrevPageList" class="page-button">
        <i class="fas fa-caret-left"></i>
      </div>

      <div class="page-button" 
        v-for="pageNumber in pageArray" 
        :key="`page${pageNumber}`"
        v-show="pageNumber <= lastPage"
        @click="changeCurrentPage(pageNumber)"
        :class="{ 'current-page' : pageNumber === currentPage}"
      >
        {{ pageNumber }}
      </div>

      <div v-show="index + 10 <= lastIndex" @click="showNextPageList" class="page-button">
        <i class="fas fa-caret-right"></i>
      </div>

      <div v-show="index + 10 <= lastIndex" @click="showLastPageList" class="page-button">
        <i class="fas fa-forward"></i>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import MovieInfoBar from './MovieInfoBar'
import DataList from '../../mixin/components/DataList'

export default {
  components: {
    MovieInfoBar,
  },
  data() {
    return {
      currentView: 'movie'
    }
  },
  computed: {
    ...mapState('movie', { dataList: 'movieList' }),
  },
  mixins: [ DataList ]
};
</script>

<style scoped lang="scss">
@import "@/mixin/style/_datalist";
</style>