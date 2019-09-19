<template>
  <div class="related_modal">
    <div class="movie_info_div">
      <div :style="{'backgroundImage':`url('${movie.img}')`}" class="movie_image"></div>
      <div class="movie_info">
        <p class="movie_title">{{ movie.title }}</p>
        <p class="movie_genre">{{ movie.genre }}</p>
        <div class="rating">
          <div class="avg_rating_div">
            <div class="avg_title">평균 별점</div>
            <div class="avg_rating">{{ movie.avg_rating }}</div>
          </div>
          <div class="user_rating">

          </div>
        </div>
        <div class="discription">

        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  props: {
    movie: {
      type: Object,
      default: () => ({ id: 0, title: "", img: "", description: "", genre: "" })
    },
  },
  name: "userRelatedMovie",

}

</script>

<style lang="scss">
.related_modal {
  width: 100vw;
  height: 100vh;
  top: 0;
  left: 0;
  display: none;
  position: fixed;
  flex-direction: row;
  z-index: 1;
  background-color: rgba(0, 0, 0, 0.2);
  color: white;
}
.movie_info_div {
  display: flex;
  flex-direction: column;
  width: fit-content;
}
.movie_image {
  width: 90%;
  height: 60%;
  margin: 0 auto;
  background: {
    size: contain;
    repeat: no-repeat;
  }
}
.movie_title {
  width: fit-content;
  font-size: 22px;
}
.avg_rating_div {
  margin-top: 16px;
  display: flex;
  width: fit-content;
  border: 2px white solid;
  border-radius: 5px;
  font-size: 22px;
}
.avg_title {
  background-color: black;
  padding: 5px;
}
.avg_rating {
  background-color: white;
  color: black;
  padding: 5px;
}
</style>