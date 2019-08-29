<template>
  <section class="image-slider">
    <h1>HEllo slider</h1>
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
  height: 100vh;
  background-color: blue;
}
</style>