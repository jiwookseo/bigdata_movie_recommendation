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
    return {
      sliderList: [
        {
          type: "연령대",
          selectObject: {
            1: "18세 미만이",
            18: "18-24세가",
            25: "25-34세가",
            35: "35-44세가",
            45: "45-49세가",
            50: "50-55세가",
            56: "56세 이상이"
          }
        },
        {
          type: "직업",
          selectObject: {
            "academic/educator": "교육인이",
            artist: "예술가가",
            "clerical/admin": "사무직이",
            "college/grad student": "대학생이",
            "K-12 student": "학생이",
            "customer service": "서비스직이",
            "doctor/health care": "의료인이",
            "executive/managerial": "관리직이",
            farmer: "농업인이",
            homemaker: "가정주부가",
            lawyer: "법조인이",
            programmer: "프로그래머가",
            "sales/marketing": "마케터가",
            scientist: "과학자가",
            "self-employed": "자영업자가",
            "technician/engineer": "기술자가",
            "tradesman/craftsman": "수공업자가",
            writer: "작가가"
          }
        },
        {
          type: "성별",
          selectObject: {
            M: "남성이",
            F: "여성이"
          }
        }
      ]
    };
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
  position: relative;
  padding: 40px 0;
  background-color: #111;
  div + div {
    margin-top: 60px;
  }
}
</style>