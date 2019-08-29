<template>
  <v-container>
    <v-col class="search_buttons">
      <div class="search_button">
        <v-btn text color="red" @click="selectTitle">제목 검색</v-btn>
        <v-btn text color="green" @click="selectGenre">장르 검색</v-btn>
      </div>
      <div class="sort_button">
        <v-btn text small color="pink" @click="sortViews">조회수 순</v-btn>
        <v-btn text small color="blue" @click="sortRatings">평점 순</v-btn>
      </div>
    </v-col>
    <v-text-field
      class="search_input"
      v-model="title"
      @keydown.enter="onSubmit"
      label="영화 제목"
      v-if="btn === 'title'"
    ></v-text-field>
    <v-container v-else>
      <v-btn
        v-for="(genre, i) of genreItems"
        v-if="genre.state === false"
        :key="i"
        text
        class="genre_button"
        @click="changeState(i)"
      >{{ genre.genre }}</v-btn>
      <v-btn
        v-else
        :key="i"
        text
        color="blue"
        class="genre_button"
        @click="changeState(i)"
      >{{ genre.genre }}</v-btn>
    </v-container>
    <v-layout justify-center pa-10>
      <v-btn large color="indigo white--text" @click="onSubmit">Search</v-btn>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    }
  },
  data: () => ({
    title: "",
    params: {
      title: "",
      genres: "",
      sort_ratings: "",
      sort_views: ""
    },
    btn: "title",
    genre: [],
    genreItems: [
      { genre: "Action", state: false },
      { genre: "Adventure", state: false },
      { genre: "Animation", state: false },
      { genre: "Children's", state: false },
      { genre: "Comedy", state: false },
      { genre: "Crime", state: false },
      { genre: "Documentary", state: false },
      { genre: "Drama", state: false },
      { genre: "Fantasy", state: false },
      { genre: "Film-Noir", state: false },
      { genre: "Horror", state: false },
      { genre: "Musical", state: false },
      { genre: "Mystery", state: false },
      { genre: "Romance", state: false },
      { genre: "Sci-Fi", state: false },
      { genre: "Thriller", state: false },
      { genre: "War", state: false },
      { genre: "Western", state: false }
    ]
  }),
  watch: {
    title: function() {
      this.params.title = this.title;
      this.submit(this.params);
    }
  },
  mounted() {
    this.onSubmit();
  },
  methods: {
    onSubmit() {
      this.params.genres = this.genre.join();
      this.submit(this.params);
    },
    selectTitle() {
      if (this.btn === "genre") {
        this.params.genres = "";
        this.genre = [];
        this.btn = "title";
        this.onSubmit();
      }
    },
    selectGenre() {
      if (this.btn === "title") {
        for (let i = 0; i < this.genreItems.length; ++i) {
          this.genreItems[i].state = false;
        }
        this.btn = "genre";
        this.title = "";
        this.onSubmit();
      }
    },
    changeState(i) {
      if (this.genreItems[i].state === false) {
        this.genreItems[i].state = true;
        this.genre.push(this.genreItems[i].genre);
      } else {
        this.genreItems[i].state = false;
        const idx = this.genre.indexOf(this.genreItems[i].genre);
        this.genre.splice(idx, 1);
      }
      this.onSubmit();
    },
    sortViews() {
      if (this.params.sort_views === "") {
        this.params.sort_views = "1";
        this.params.sort_ratings = "";
      } else {
        this.params.sort_views = "";
      }
      this.onSubmit();
    },
    sortRatings() {
      if (this.params.sort_ratings === "") {
        this.params.sort_ratings = "1";
        this.params.sort_views = "";
      } else {
        this.params.sort_ratings = "";
      }
      this.onSubmit();
    }
  }
};
</script>

<style>
.search_buttons {
  display: flex;
  justify-content: space-between;
}

.search_button > button {
  padding: 0px 10px 0px 10px !important;
}

.search_button > button > span {
  font-size: 18px;
  font-weight: bold;
}

.genre_button {
  width: 18%;
  margin: 0px 1% 0px 1%;
  overflow: hidden;
}

.search_input {
  padding: 12px;
}
</style>