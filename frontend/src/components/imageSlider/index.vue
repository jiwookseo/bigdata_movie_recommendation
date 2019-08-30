<template>
  <section class="image-slider">
    <ImageSliderList :list-title="'10대가 좋아하는 영화쓰'" :movie-list="recommendation.age" />
    <ImageSliderList :list-title="'남성이 사랑하는 영화들'" :movie-list="recommendation.gender" />
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
  computed: {
    ...mapGetters("data", ["recommendation"])
  },
  watch: {},
  mounted() {
    this.$store.dispatch("data/getRecByAge", 18);
    this.$store.dispatch("data/getRecByOccupation", "artist");
    this.$store.dispatch("data/getRecByGender", "M");
  }
};
</script>

<style lang="scss" scoped>
.image-slider {
  padding: 40px 0;
  background-color: #111;
  div + div {
    margin-top: 60px;
  }
}
</style>