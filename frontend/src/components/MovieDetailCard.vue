<template>
  <v-card v-if="check">
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="headline card-title">{{ movie.title }}</v-list-item-title>
        <v-list-item-subtitle class="card-title">{{ genresStr }}</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-card-text>
      <v-layout justify-center>
        <v-rating
          :value="movie.rating"
          color="indigo"
          background-color="indigo"
          half-increments
          dense
          readonly
        />
        <div class="grey--text ml-3 point">{{ fixedRating }}</div>
        <v-icon color="black" class="ml-4">mdi-eye</v-icon>
        <div class="grey--text ml-3 point">{{ movie.viewCnt }}</div>
      </v-layout>
    </v-card-text>
    <hr />
    <v-card-text>
      <span class="modal-title">줄거리</span>
      {{ movie.story }}
    </v-card-text>
    <hr />
    <v-card-text>
      <span class="modal-title">이 영화를 본 사람</span>
      <div class="user-list">
        <div class="dialog" v-for="(username, i) in audience" :key="username">
          <v-dialog v-model="dialog[i]" width="40%" :key="i">
            <template v-slot:activator="{ on }">
              <v-btn text v-on="on" class="movie-button">
                <v-icon color="green" class="user-icon">people</v-icon>
                {{ username }}
              </v-btn>
            </template>
            <UserDetailCard :username="username"></UserDetailCard>
          </v-dialog>
        </div>
      </div>
    </v-card-text>
  </v-card>
  <v-card v-else>
    <v-card-title class="obj-center">Now Loading...</v-card-title>
  </v-card>
</template>

<script>
import { mapGetters } from "vuex";
import UserDetailCard from "./UserDetailCard";

export default {
  name: "MovieDetailCard",
  props: {
    id: {
      type: Number,
      id: 1
    }
  },
  components: {
    UserDetailCard
  },
  created() {
    this.setMovie();
  },
  watch: {
    id() {
      this.setMovie();
    }
  },
  computed: {
    ...mapGetters("data", ["movie", "audience"]),
    genresStr: function() {
      return this.movie.genres ? this.movie.genres.join(" / ") : "";
    },
    fixedRating: function() {
      return this.movie.rating ? this.movie.rating.toFixed(1) : 0;
    },
    check() {
      return this.movie !== {};
    }
  },
  data: () => ({
    dialog: []
  }),
  methods: {
    setMovie() {
      this.$store.dispatch("data/getMovieById", this.id);
      for (let i = 0; i < this.audience.length; ++i) {
        this.dialog[i] = false;
      }
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
  display: flex;
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