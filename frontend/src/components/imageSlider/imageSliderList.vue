<template>
  <div class="image-slider__list">
    <div class="image-slider__title">
      <ImageSliderTitle
        :data="data"
        :sliderType="sliderType"
        :type="type"
      />
    </div>
    <div class="image-slider__wrapper">
      <div class="image-slider__box" :style="{ transform: 'translateX(' + slideNum * 16 +'vw)' }">
        <ImageItem
          v-for="movie in movieList"
          :key="type + movie.id"
          :movie="movie"
          :type="type"
          :expand="expand"
          :related="related"
          class="image-slider__item"
        />
      </div>
      <div v-if="slideNum != 0" class="image-slider__arrow-left" @click="handleClick(1)">
        <span>&#60;</span>
      </div>
      <div v-show="loadAble" class="image-slider__arrow-right" @click="handleClick(-1)">
        <span>&#62;</span>
      </div>
      <div v-show="!loadAble">spinner?</div>
    </div>
    <div v-if="!expand">
      <subscribe />
    </div>
    <transition name="bounce">
      <ImageItemDetail v-if="expand && toggleDetail" :related="related" />
    </transition>
  </div>
</template>

<script>
import ImageItem from "./imageItem";
import ImageItemDetail from "./imageItemDetail";
import ImageSliderTitle from "./imageSliderTitle"
import subscribe from "../detail/subscribe";
import { mapGetters } from "vuex";

export default {
  name: "ImageSliderList",
  components: { ImageItem, ImageItemDetail, ImageSliderTitle, subscribe },
  props: { 
    data: { type: Object, default: () => ({ type: "연령대" }) },
    sliderType: { type: String, default: () => ""},
    expand: { type: Boolean, default: () => true},
    related: {type: Boolean, default: false}
  },
  data() {
    return {
      slideNum: 0,
      detailToggle: false,
      selected: 18,
      loadAble: true
    };
  },
  computed: {
    ...mapGetters("mvUi", ["detailToggler", "detailType"]),
    type() {
      if (this.data.type === "연령대") {
        return "Age";
      } else if (this.data.type === "직업") {
        return "Occupation";
      } else {
        return "Gender";
      }
    },
    movieList() {
      if (this.$store.state.mvUi.sliderType === "board") {
        return this.$store.getters[`movie/rec${this.type}`].map(movie => ({
          ...movie,
          description: movie.story.slice(0, 500),
          avg_rating: movie.avg_rating,
          img:
            movie.stillCut ||
            movie.poster ||
            "https://files.slack.com/files-pri/TMJ2GPC23-FMF2L2DQA/599637c326f7d273826d.jpg"
        }));
      } else if (this.$store.state.mvUi.sliderType === "profile") {
        return this.$store.getters["user/ratings"].map(movie => ({
          ...movie,
          description: movie.story.slice(0, 500),
          avg_rating: movie.avg_rating,
          img:
            movie.stillCut ||
            movie.poster ||
            "https://files.slack.com/files-pri/TMJ2GPC23-FMF2L2DQA/599637c326f7d273826d.jpg"
        }));
      }
    },
    toggleDetail() {
      return this.detailToggler && this.detailType === this.type;
    },
  },
  watch: {
    movieList() {
      this.loadAble = true;
    }
  },
  methods: {
    handleClick: function(n) {
      this.slideNum += n;
      if (this.slideNum < -this.movieList.length + 5) {
        this.load();
        this.loadAble = false;
      }
    },
    handleDetailToggler: function() {
      this.$store.dispatch("mvUi/setDetailToggler");
    },
    load: function() {
      this.$store.dispatch(`movie/getRecBy${this.type}`, this.selected);
    },
  }
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css?family=Jua|Ubuntu&display=swap");
.image-slider__list {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.image-slider__wrapper {
  display: flex;
  align-items: center;
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
  right: 20px;
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

.bounce-enter-active {
  animation: bounce-in 1s;
}
.bounce-leave-active {
  animation: bounce-out 0.4s;
}
@keyframes bounce-in {
  0% { transform: scale(0); }
  50% { transform: scale(1.3); }
  100% { transform: scale(1); }
}
@keyframes bounce-out {
  0% { transform: scaleY(0.8); }
  25% { transform: scaleY(0.6); }
  50% { transform: scaleY(0.4); }
  75% { transform: scaleY(0.2); }
  100% { transform: scaleY(0); }
}
</style>
