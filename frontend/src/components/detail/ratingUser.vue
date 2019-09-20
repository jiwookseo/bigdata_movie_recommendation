<template>
  <div>
    <span>{{ movieId }}</span>
    <span>{{ username }}</span>
    <span>{{ rating }}</span>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  props: {
    movieId: {
      type: Number,
    },
    username: {
      type: String,
      default: "",
    },
  },
  name: "ratingUser",
  created() {
    this.check();
  },
  computed: {
    ...mapState({
      getLogin: state => state.user.isLogin,
      getRating: state => state.user.rating
    })
  },
  data: () => ({
    rating: 0,
  }),
  methods: {
    ...mapActions("user", ["setUserRating"]),
    async check() {
      if (this.getLogin) {
        const data = {
          "username": this.username,
          "movieId": this.movieId
        };
        await this.setUserRating(data);
        this.rating = this.getRating
      }
    }
  }
}
</script>

<style lang="scss">
.rating-user-div {
  display: inline-flex;
}
.rating-user-div span {
  color: white;
}
</style>
