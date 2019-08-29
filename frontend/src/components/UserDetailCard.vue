<template>
  <v-card v-if="check">
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="headline user-title">{{ username }}</v-list-item-title>
        <v-list-item-subtitle class="user-title">성별 : {{ user.gender }} 나이 : {{ user.age }}</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-card-text>
      <v-layout justify-center>
        <div class="grey--text point">직업 : {{ user.occupation }}</div>
      </v-layout>
    </v-card-text>
    <hr />
    <v-card-text>
      <span class="user-movie">{{ username }} 님이 본 영화</span>
      <div class="user-list">
        <div class="movie-dialog" v-for="(rating, i) in ratings" :key="rating.id">
          <v-dialog v-model="dialog[i]" width="40%" :key="i">
            <template v-slot:activator="{ on }">
              <v-btn text v-on="on" class="user-button">
                <v-icon color="red" class="movie-icon">movie</v-icon>
                {{ rating.movie_title }}
              </v-btn>
            </template>
            <MovieDetailCard :id="rating.movie_id"></MovieDetailCard>
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

export default {
  name: "UserDetailCard",
  props: {
    username: {
      type: String,
      default: ""
    }
  },
  components: {
    MovieDetailCard: () => import("./MovieDetailCard.vue")
  },
  created() {
    this.setUser();
  },
  watch: {
    username() {
      this.setUser();
    }
  },
  computed: {
    ...mapGetters("data", ["user", "ratings"]),
    check() {
      return this.ratings[0]
        ? this.ratings[0].username === this.username
        : false;
    }
  },
  data: () => ({
    dialog: []
  }),
  methods: {
    setUser() {
      this.$store.dispatch("data/getUserByUsername", this.username);
      for (let i = 0; i < this.ratings.length; ++i) {
        this.dialog[i] = false;
      }
    }
  }
};
</script>

<style>
.user-button {
  display: flex;
  flex-direction: column;
}
.movie-dialog {
  width: 100%;
  margin: 0;
  display: inline-flex;
  justify-content: center;
}
hr {
  margin: 0% 4% 10px 4%;
}
.user-movie {
  margin: 20px 0 10px 0;
  font-size: 16px;
  font-weight: bold;
  color: black;
  display: flex;
}
.movie-dialog > button > span {
  color: rgba(0, 0, 0, 0.7);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.movie-icon {
  margin-right: 5px;
}
</style>