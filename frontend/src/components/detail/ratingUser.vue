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
  name: "ratingUser",
  props: {
    movieId: {
      type: Number,
      default: 0,
    },
    username: {
      type: String,
      default: "",
    },
  },
  data: () => ({
    rating: 0,
  }),
  mounted() {
    // console.log(this.movieId)
  },
  computed: {
    ...mapState({
      getLogin: state => state.user.isLogin,
      getRating: state => state.user.rating
    })
  },
  created() {
    this.check();
  },
  methods: {
    ...mapActions("user", ["setUserRating"]),
    async check() {
      if (this.getLogin) {
        const data = {
          "username": this.username,
          "movieId": this.movieId
        };
        // console.log(this.movieId)
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
