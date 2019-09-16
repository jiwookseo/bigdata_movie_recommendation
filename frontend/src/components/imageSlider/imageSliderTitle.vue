<template>
  <div class="image-slider__title">
    <h2 v-if="sliderType==='board'">
      <select v-model="selected" name="target">
        <option class="movie-option" value>{{ data.type }} 선택</option>
        <option
          class="movie-option"
          v-for="(key, value) in data.selectObject"
          :key="key"
          :value="value"
        >{{ key }}</option>
      </select> 좋아하는 영화
    </h2>
      <h2 v-if="sliderType==='profile'">{{ data.type }}</h2>
  </div>
</template>

<script>
export default {
  name: "ImageSliderTitle",
  props: ["data", "sliderType", "type"],
  data() { return { selected: 18, }; },
  watch: {
    selected() {
      if (this.selected !== "") this.load();
    },
  },
  mounted() {
    if (this.type === "Age") {
      this.selected = "1";
    } else {
      this.selected = this.type === "Occupation" ? "programmer" : "M";
    }
  },
  methods: {
    load: function() {
      this.$store.dispatch(`movie/getRecBy${this.type}`, this.selected);
    }
  }

}
</script>

<style lang="scss" scoped>
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
    font-family: "Ubuntu", sans-serif;
    font-size: 16px;
    font-weight: 700;
    text-align: center;
    cursor: pointer;

    &:first-child {
      color: #111;
      font-size: 18px;
    }
    &:active,
    &:focus {
      border: none;
      outline: none;
      background-color: #111;
      font-weight: 700;
      color: rgba(255, 177, 1);
    }
  }
}

</style>