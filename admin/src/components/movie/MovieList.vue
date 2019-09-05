<template>
  <div class="item-list-container">
    <div class="genre_buttons" v-if="check">
      <button v-for="genre of Object.keys(genres)" v-if="genres[genre] === 1" class="genre_button" @click="insertGenre(genre)">{{ genre }}</button>
    </div>
    <!-- Data List -->
    <div v-for="(movie, idx) in dataList" v-if="idx+1 <= currentPage*10 && idx+1 > (currentPage-1)*10" :key="`movie${movie.id}`">
      <movie-info-bar
        :id="movie.id"
        :img="movie.img"
        :title="movie.title"
        :genres="movie.genres"
        :rating="movie.rating"
        :view-cnt="movie.viewCnt"
        :idx="idx"
        :target="checkTarget"
        :onTarget="targetIdx"
        :input-genres="inputGenres"
        :reset-genre="resetGenre"
        :check-genre="checkGenre"
        :insert-genre="insertGenre"
        :edited="edited"
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
      currentView: 'movie',
      inputGenres: [],
      genres: {},
      check: false,
      targetIdx: -1
    }
  },
  computed: {
    ...mapState('movie', { dataList: 'movieList' }),
  },
  mounted() {
    this.resetGenre();
  },
  methods: {
    resetGenre() {
      this.inputGenres = [];
      this.genres = {"Action": 1, "Adventure": 1, "Animation": 1, "Children's": 1, "Comedy": 1, "Crime": 1, "Documentary": 1, "Drama": 1,
        "Fantasy": 1, "Film-Noir": 1, "Horror": 1, "Musical": 1, "Mystery": 1, "Romance": 1, "Sci-Fi": 1, "Thriller": 1, "War": 1, "Western": 1};
    },
    checkGenre() {
      this.check = !this.check;
    },
    checkTarget(idx, genres) {
      if (this.targetIdx === -1) {
        this.resetGenre();
        this.checkGenre();
        this.targetIdx = idx
      } else if (this.targetIdx === idx) {
        this.resetGenre();
        this.checkGenre();
        this.targetIdx = -1;
      } else {
        this.resetGenre();
        this.targetIdx = idx;
      }
      for (const genre of genres) {
        this.insertGenre(genre)
      }
    },
    insertGenre(genre) {
      if (this.genres[genre] === 1) {
        this.genres[genre] = 0;
        this.inputGenres.push(genre)
      } else {
        this.genres[genre] = 1;
      }
    },
    edited(idx, info) {
      this.dataList[idx]["title"] = info["title"];
      this.dataList[idx]["genres"] = info["genres"];
    },
  },
  mixins: [ DataList ]
};
</script>

<style scoped lang="scss">
@import "@/mixin/style/_datalist";

.genre_buttons {
  margin: {
    top: 10px;
    bottom: 10px;
  }
  width: 100%;
  display: flex;
  justify-content: space-around;
}
.genre_button {
  background: {
    color: rgba(0, 255, 30, 0.37);
  };
  padding: 5px;
  border: rgba(0, 167, 255, 1) solid 2px;
  border-radius: 10px;
}
.genre_button:hover {
  background: {
    color: rgba(5, 255, 24, 0.5);
  };
}
</style>