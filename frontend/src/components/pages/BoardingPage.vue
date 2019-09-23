<template>
  <div>
    <Jumbotron />
    <ImageSlider :sliderList="sliderList" :expnad="true" :related="true" />
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
  computed: {
    sliderList(){
      return this.$store.getters["mvUi/sliderBoardData"];
    }
  },
  created(){
    this.$store.commit('mvUi/setSliderType', "board")
  }
}
</script>

<style lang="scss" scoped>

</style>