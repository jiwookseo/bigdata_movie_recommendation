<template>
  <div class="rating-user">
    <span 
      class="star"
      v-for="i in 5"
      :id="'star' + (i - 1)"
      :key="'star' + i"
      @mouseover="paint(i - 1)" 
      @click="editRating"
    >
      {{ stars[i - 1] }}
    </span>
  </div>
</template>

<script>
  import { mapState, mapActions } from "vuex";
  export default {
    name: "ratingUser",
    props: {
      movieId: {
        type: Number,
        default: 0
      }
    },
    data: () => ({
      stars: ["☆", "☆", "☆", "☆", "☆"],
      buttonMessage: "수정",
      rating: 0,
    }),
    watch: {
      getRating: function() {
        this.buttonMessage = "수정";
        const stars = ["☆", "☆", "☆", "☆", "☆"];
        for (let i = 0; i < this.getRating[0]; ++i) {
          stars[i] = "★";
          let star = document.getElementById("star" + i);
          star.style.color = "rgb(255, 177, 1)";
          this.rating = i + 1;
        }
        for (let i = this.getRating[0]; i < 5; ++i) {
          stars[i] = "☆";
          let star = document.getElementById("star" + i);
          star.style.color = "white";
        }
        this.stars = stars;
      }
    },
    mounted() {
      this.draw();
    },
    computed: {
      ...mapState({
        getRating: state => state.user.rating,
        username: state => state.user.username,
        token: state => state.user.token,
      }),
    },
    methods: {
      ...mapActions("user", ["setRating"]),
      draw() {
        const stars = ["☆", "☆", "☆", "☆", "☆"];
        for (let i = 0; i < this.getRating[0]; ++i) {
          stars[i] = "★";
          let star = document.getElementById("star" + i);
          star.style.color = "rgb(255, 177, 1)";
          this.rating = i + 1;
        }
        this.stars = stars;
      },
      paint(idx) {
        const stars = ["☆", "☆", "☆", "☆", "☆"];
        for (let i = 0; i <= idx; ++i) {
          stars[i] = "★";
          let star = document.getElementById("star" + i);
          star.style.color = "rgb(255, 177, 1)";
          this.rating = i + 1;
        }
        for (let i = idx + 1; i < 5; ++i) {
          stars[i] = "☆";
          let star = document.getElementById("star" + i);
          star.style.color = "white";
        }
        this.stars = stars
      },
      async editRating() {
        if (this.buttonMessage === "수정") {
          this.stars = ["☆", "☆", "☆", "☆", "☆"];
          for (let i = 0; i < 5; ++i) {
            let star = document.getElementById("star" + i);
            star.style.color = "white";
            this.rating = i + 1;
          }
          this.buttonMessage = "완료";
        } else {
          if (this.getRating !== this.rating) {
            const data = {
              "username": this.username,
              "token": this.token,
              "movieId": this.movieId,
              "rating": this.rating
            }
            await this.setRating(data);
          }
          this.buttonMessage = "수정";
        }
      }
    }
  }
</script>

<style lang="scss">
  .rating-user {
    margin-top: 20px;
  }
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
    cursor: pointer;
  }
  .rating_button {
    margin-left: 30px;
    color: white;
    border-radius: 10px;
    background-color: rgb(255, 177, 1);
    padding: 10px;
    outline: none;
  }
</style>
