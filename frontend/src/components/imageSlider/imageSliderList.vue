<template>
  <div class="image-slider__list">
    <div class="image-slider__title">
      <h2>{{ listTitle }}</h2>
    </div>
    <div class="image-slider__wrapper">
      <div class="image-slider__box" :style="{ transform: 'translateX(' + slideNum*16 +'vw)' }">
        <ImageItem
          class="image-slider__item"
          v-for="movie in movieList"
          :key="movie.id"
          :id="movie.id"
          :title="movie.title"
          :img="movie.stillCut || movie.poster || 'https://files.slack.com/files-pri/TMJ2GPC23-FMF2L2DQA/599637c326f7d273826d.jpg'"
          :description="movie.story.slice(0, 500)"
          :genre="movie.genres"
          @activateMovieDetail="handleMovieData"
        />
      </div>
      <div v-if="slideNum !=0" class="image-slider__arrow-left" @click="handleClick(1)">
        <span>&#60;</span>
      </div>
      <div v-if="slideNum>-5" class="image-slider__arrow-right" @click="handleClick(-1)">
        <span>&#62;</span>
      </div>
    </div>

    <ImageItemDetail v-if="toggleDetail" toggle="detailToggle" @closeDetail="handleDetailToggler" />
  </div>
</template>

<script>
import ImageItem from "./imageItem";
import ImageItemDetail from "./imageItemDetail";

export default {
  name: "ImageSliderList",
  components: {
    ImageItem,
    ImageItemDetail
  },
  props: ["movieList", "listTitle"],
  data() {
    return {
      slideNum: 0,
      detailToggle: false
    };
  },
  computed: {
    toggleDetail() {
      return this.$store.state.mvUi.detailToggler && this.detailToggle;
    }
  },
  mounted() {},
  methods: {
    handleClick: function(n) {
      const s = this.slideNum + n;
      this.slideNum = s;
    },
    handleDetailToggler: function() {
      this.detailToggle = !this.detailToggle;
    },
    handleMovieData: function(movie) {
      this.handleDetailToggler();
      this.$store.commit("mvUi/setActivateMovie", movie);
    }
  }
};
</script>

<style lang="scss" scoped>
.image-slider__list {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.image-slider__wrapper {
  display: flex;
  align-items: center;
}

.image-slider__title {
  padding: 20px 0 20px 30px;
  h2 {
    color: #fff;
    font-size: 28px;
    font-weight: 700;
  }
}
.image-slider__box {
  width: 80%;
  margin-left: 30px;
  display: flex;
  align-items: center;
  transition: all 0.4s ease-in-out;
  div + div {
    margin-left: 10px;
  }
}

.image-slider__arrow-left {
  position: absolute;
  left: 0px;
  width: 30px;
  height: 80px;
  display: flex;
  align-items: center;
  background-color: rgba(33, 33, 33, 0.6);
  span {
    font-size: 40px;
    font-weight: 700;
    color: #aaa;
    cursor: pointer;
  }
}

.image-slider__arrow-right {
  position: absolute;
  right: 0;
  width: 30px;
  height: 80px;
  display: flex;
  align-items: center;
  background-color: rgba(33, 33, 33, 0.6);
  span {
    font-size: 40px;
    font-weight: 700;
    color: #aaa;
    cursor: pointer;
  }
}
</style>