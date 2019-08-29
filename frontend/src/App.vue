<template>
  <div class="app">
    <Header />
    <ImageSlider />
  </div>
</template>

<script>
import router from "./router";
import './reset.css';
import Header from "./components/header/index"
import ImageSlider from "./components/imageSlider/index"

export default {
  components: {
    Header,
    ImageSlider
  }
};
</script>

<style lang="scss" scoped>
  .app {
    width: 100vw;
    overflow-x: hidden;
  }

  
</style>