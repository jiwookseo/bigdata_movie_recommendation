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
  components: {
    Jumbotron,
    ImageSlider
  },
  created(){
    this.$store.commit('mvUi/setSliderType', "board")
  }
}
</script>

<style lang="scss" scoped>

</style>