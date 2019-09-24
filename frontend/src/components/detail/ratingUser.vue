<template>
  <div>
    <span v-for="star, i in stars" v-on:mouseenter="paint(i)" :id="'star' + i" class="star">{{ star }}</span>
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
    stars: []
  }),
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
        await this.setUserRating(data);
        this.rating = this.getRating
        for (let i = 0; i < this.rating; ++i) {
          this.stars.push("★");
        }
        for (let i = this.rating; i < 5; ++i) {
          this.stars.push("☆")
        }
      }
    },
    paint(idx) {
      for (let i = 0; i <= idx; ++i ) {
        let star = document.getElementById("star" + i);
        star.style.color = "rgb(255, 177, 1)";
      }
      for (let i = idx + 1; i < 5; ++i) {
        let star = document.getElementById("star" + i);
        star.style.color = "white";
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
.star {
  font-size: 30px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  color: rgb(255, 177, 1);
}
</style>
