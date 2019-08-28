<template>
  <v-card v-if="check">
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="headline user-title">
          {{ username }}
        </v-list-item-title>
        <v-list-item-subtitle class="user-title">성별 : {{ gender }} 나이 : {{ age }}</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-card-text>
      <v-layout justify-center>
        <div class="grey--text point">직업 : {{ occupation }}</div>
      </v-layout>
    </v-card-text>
    <hr>
    <v-card-text>
      <span class="user-movie">{{ username }} 님이 본 영화</span>
      <div class="user-list">
        <div class="movie-dialog" v-for="(movie, i) of ratings">
          <v-dialog v-model="dialog[i]" width="40%" :key="i">
            <template v-slot:activator="{ on }">
              <v-btn text v-on="on" class="user-button"><v-icon color="red" class="movie-icon">movie</v-icon>{{ movie }}</v-btn>
            </template>
            <MovieDetailCard :title="movie"></MovieDetailCard>
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
import {mapActions, mapState} from "vuex"

export default {
  name: "UserDetailCard",
  props: {
    username: {
      type: String,
      default: "",
    },
  },
  components: {
    MovieDetailCard: () => import("./MovieDetailCard.vue")
  },
  created() {
    this.getUsers();
  },
  computed: {
    ...mapState({
      setUser: state => state.data.userSelected[0]
    })
  },
  data: () => ({
    id: 0,
    is_staff: false,
    gender: "",
    age: "",
    occupation: "",
    ratings: {},
    dialog: [],
    check: false
  }),
  methods: {
    ...mapActions("data", ["get_userKey"]),
    async getUsers() {
      await this.get_userKey({username: this.username});
      const user = this.setUser;
      for (let i = 0; i < this.ratings.length; ++i) {
        this.dialog[i] = false;
      }
      this.username = user.username;
      this.is_staff = user.is_staff;
      this.gender = user.gender;
      this.age = user.age;
      this.occupation = user.occupation;
      this.ratings = user.ratings;
      this.check = true;
    }
  }
}
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
    display: flex
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