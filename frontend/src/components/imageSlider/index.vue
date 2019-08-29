<template>
  <section class="image-slider">
    <ImageSliderList />
    <ImageSliderList />
  </section>
</template>

<script>
import ImageSliderList from "./imageSliderList"
export default {
  name: "ImageSlider",
  components: {
    ImageSliderList
  }
}
</script>

<style lang="scss" scoped>
.image-slider {
  margin-top: calc(100vh - 64px);
  padding-top: 40px;
  height: 100vh;
  background-color: #333;
  div + div {
    margin-top: 60px;
  }
}
</style>