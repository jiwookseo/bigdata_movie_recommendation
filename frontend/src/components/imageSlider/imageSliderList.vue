<template>
  <div class="image-slider__list">
    <div class="image-slider__title">
      <h2 v-if="sliderType==='board'">
        <select v-model="selected" name="target">
          <option class="movie-option" value>{{ data.type }} 선택</option>
          <option class="movie-option" v-for="(key, value) in data.selectObject" :key="key" :value="value">{{ key }}</option>
        </select> 좋아하는 영화
      </h2>
      <h2 v-if="sliderType==='profile'">
        {{ data.type }}
      </h2>
    </div>
    <div class="image-slider__wrapper">
      <div class="image-slider__box" :style="{ transform: 'translateX(' + slideNum*16 +'vw)' }">
        <ImageItem
          v-for="movie in movieList"
          :key="movie.id"
          :movie="movie"
          :type="type"
          class="image-slider__item"
        />
      </div>
      <div v-if="slideNum !=0" class="image-slider__arrow-left" @click="handleClick(1)">
        <span>&#60;</span>
      </div>
      <div v-if="slideNum>-5" class="image-slider__arrow-right" @click="handleClick(-1)">
        <span>&#62;</span>
      </div>
    </div>
    <transition name="bounce">
      <ImageItemDetail v-if="toggleDetail" />
    </transition>
  </div>
</template>

<script>
import ImageItem from "./imageItem";
import ImageItemDetail from "./imageItemDetail";
import { mapGetters } from "vuex";

export default {
  name: "ImageSliderList",
  components: {
    ImageItem,
    ImageItemDetail
  },
  props: { data: { type: Object, default: () => ({ type: "연령대" }) } },
  data() {
    return {
      slideNum: 0,
      detailToggle: false,
      selected: 18
    };
  },
  computed: {
    ...mapGetters("mvUi", ["detailToggler", "detailType", "sliderType"]),
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
      if (this.$store.state.mvUi.sliderType === "board"){
        return this.$store.getters[`data/rec${this.type}`].map(movie => ({
          ...movie,
          description: movie.story.slice(0, 500),
          img:
            movie.stillCut ||
            movie.poster ||
            "https://files.slack.com/files-pri/TMJ2GPC23-FMF2L2DQA/599637c326f7d273826d.jpg"
        }))
      } else if (this.$store.state.mvUi.sliderType === "profile"){
        return this.$store.getters[`data/rec${this.type}`].map(movie => ({
          ...movie,
          description: movie.story.slice(0, 500),
          img:
            movie.stillCut ||
            movie.poster ||
            "https://files.slack.com/files-pri/TMJ2GPC23-FMF2L2DQA/599637c326f7d273826d.jpg"
        }))
      };
    },
    toggleDetail() {
      return this.detailToggler && this.detailType === this.type;
    }
  },
  watch: {
    selected() {
      if (this.selected !== "")
        this.$store.dispatch(`data/getRecBy${this.type}`, this.selected);
    }
  },
  mounted() {
    if (this.type === "Age") {
      this.selected = "1";
    } else {
      this.selected = this.type === "Occupation" ? "programmer" : "M";
    }
  },
  methods: {
    handleClick: function(n) {
      const s = this.slideNum + n;
      this.slideNum = s;
    },
    handleDetailToggler: function() {
      this.$store.dispatch("mvUi/setDetailToggler");
    }
  }
};
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css?family=Jua|Ubuntu&display=swap');
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
  display: flex;
  h2 {
    display: inline-block;
    margin-right: 14px;
    color: #fff;
    font-size: 28px;
    font-weight: 700;
  }
  select {
    outline: none;
    border: none;
    color: rgb(255, 177, 1);
    padding: 10px;
    cursor: pointer;
    font-weight: 700;
    &:hover {
      background-color: rgba(255, 177, 1);
      color: #111;
      border: none;
      outline: none;
    }
  }

  .movie-option {
    outline: none;
    border: none;
    font-family: 'Ubuntu', sans-serif;
    font-size: 16px;
    font-weight: 700;
    text-align: center;
    cursor: pointer;

    &:first-child {
      color: #111;
      font-size: 18px;

    }
    &:active, &:focus {
      border: none;
      outline: none;
      background-color: #111;
      font-weight: 700;
      color: rgba(255, 177, 1);
    }
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
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.3);
  }
  100% {
    transform: scale(1);
  }
}
@keyframes bounce-out {
  0% {
    transform: scaleY(0.8);
  }
  25% {
    transform: scaleY(0.6);
  }
  50% {
    transform: scaleY(0.4);
  }
  75% {
    transform: scaleY(0.2);
  }
  100% {
    transform: scaleY(0);
  }
}
</style>
