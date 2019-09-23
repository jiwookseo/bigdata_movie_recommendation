<template>
  <section class="image-slider">
    <!-- 
      ImageSilder 사용시 import를 하고 사용 하실 때 
      expand에 boolean value와 data에 movieList data를 넣어주면 됩니다.
      movieList의 형식은 Array 이며, 각 Array는 2개의 object를 요소로 가집니다.
      Array = [ selectedObj, type] 이며
      selectedObj: select box를 사용할 경우 각 값에 대해 key - value(String) 으로 사용하시면 됩니다.
      type : String 으로, imageSlider의 타이틀로 사용됩니다.
      
      <ImageSlider :sliderList="sliderList" :expnad="true"/>
    -->
    <ImageSliderList
      v-for="slider in sliderList"
      :key="slider.type"
      :data="slider"
      :sliderType="sliderType"
      :expand="expand"
      :related="related" />
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
  props: {
    sliderList: {type: Array, default: () => []},
    expand: {type: Boolean, default: true},
    related: {type: Boolean, default: false},
  },
  computed: {
    ...mapGetters("mvUi", ["sliderType"])
  },
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