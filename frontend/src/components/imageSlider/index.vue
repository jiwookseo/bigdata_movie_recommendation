<template>
  <section class="image-slider">
    <ImageSliderList v-for="slider in sliderList" :key="slider.type" :data="slider" />
  </section>
</template>

<script>
import ImageSliderList from "./imageSliderList";
import { mapGetters } from "vuex";

export default {
  name: "ImageSlider",
  components: {
    ImageSliderList
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters("mvUi", ["sliderType"]),
    sliderList() {
      if (this.$store.state.mvUi.sliderType === "board") {
        return this.$store.getters["mvUi/sliderBoardData"];
      } else if (this.$store.state.mvUi.sliderType === "profile") {
        return [
          {
            type: "평가한 영화",
            selectedObject: ""
          }
        ];
      }
    }
  },
  watch: {},
  mounted() {}
};
</script>

<style lang="scss" scoped>
.image-slider {
  position: relative;
  padding: 40px 0;
  background-color: #111;
  div + div {
    margin-top: 60px;
  }
}
</style>