<template>
  <div>
    <Jumbotron />
    <ImageSlider />
  </div>
</template>

<script>
import Jumbotron from '../header/Jumbotron'
import ImageSlider from '../imageSlider/index'

export default {
  name: "BoardingPage",
  component: {
    Jumbotron,
    ImageSlider
  }
}
</script>

<style lang="scss" scoped>

</style>