<template>
  <v-card v-if="check">
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="headline card-title">
          {{ title }}
        </v-list-item-title>
        <v-list-item-subtitle class="card-title">{{ genresStr }}</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-card-text>
      <v-layout justify-center>
        <v-rating :value="rating" color="indigo" background-color="indigo" half-increments dense readonly/>
        <div class="grey--text ml-3 point">{{ rating.toFixed(1) }}</div>
        <v-icon color="black" class="ml-4">mdi-eye</v-icon>
        <div class="grey--text ml-3 point">{{ viewCnt }}</div>
      </v-layout>
    </v-card-text>
    <hr>
    <v-card-text>
      <span class="modal-title">줄거리</span>
      {{ story }}
    </v-card-text>
    <hr>
    <v-card-text>
      <span class="modal-title">이 영화를 본 사람</span>
      <div class="user-list">
        <div class="dialog" v-for="(user, i) of ratings">
          <v-dialog v-model="dialog[i]" width="40%" :key="i">
            <template v-slot:activator="{ on }">
              <v-btn text v-on="on" class="movie-button"><v-icon color="green" class="user-icon">people</v-icon>{{ user }}</v-btn>
            </template>
            <UserDetailCard :username="user"></UserDetailCard>
          </v-dialog>
        </div>
      </div>
    </v-card-text>
  </v-card>
  <v-card v-else>
    <v-card-title class="obj-center">
      Now Loading...
    </v-card-title>
  </v-card>
</template>

<script>
import {mapState, mapActions} from "vuex";
import UserDetailCard from "./UserDetailCard";

export default {
  name: "MovieDetailCard",
  props: {
    title: {
      type: String,
      default: "",
    }
  },
  components: {
    UserDetailCard
  },
  created() {
    this.getMovie();
  },
  computed: {
    genresStr: function() {
      return this.genres.join(" / ");
    },
    ...mapState({
      setMovie: state => state.data.movieSelected[0]
    })
  },
  data: () => ({
    id: 0,
    dialog: [],
    genres: [],
    img: "",
    rating: 0.0,
    viewCnt: 0,
    story: "",
    ratings: {},
    check: false,
  }),
  methods: {
    ...mapActions("data", ["get_movieKey"]),
    async getMovie() {
      await this.get_movieKey({title: this.title});
      const movie = this.setMovie;
      for (let i = 0; i < this.ratings.length; ++i) {
        this.dialog[i] = false;
      }
      this.id = movie.id;
      this.title = movie.title;
      this.genres = movie.genres;
      this.viewCnt = movie.viewCnt;
      this.rating = movie.rating;
      this.ratings = movie.ratings;
      this.story = movie.story;
      this.check = true;
    }
  }
};
</script>

<style>
.movie-button {
  display: flex;
  z-index: 1;
}
hr {
  margin: 0% 4% 10px 4%;
}
.card-title {
  display: flex;
  justify-content: center;
}
.point {
  margin-top: 4px;
}
.modal-title {
  margin: 20px 0 10px 0;
  font-size: 16px;
  font-weight: bold;
  color: black;
  display: flex
}
.dialog > button > span {
  color: rgba(0, 0, 0, 0.7);
}
.dialog {
  width: 20%;
  margin: 0 2% 0 2%;
  display: inline-flex;
  justify-content: center;
}
.user-icon {
  margin-right: 5px;
}
</style>