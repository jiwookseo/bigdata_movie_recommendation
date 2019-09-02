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
            1: "18세 미만",
            18: "18-24세",
            25: "25-34세",
            35: "35-44세",
            45: "45-49세",
            50: "50-55세",
            56: "56세 이상"
          }
        },
        {
          type: "직업",
          selectObject: {
            "academic/educator": "교육인",
            artist: "예술가",
            "clerical/admin": "사무직",
            "college/grad student": "대학생",
            "K-12 student": "학생",
            "customer service": "고객서비스",
            "doctor/health care": "의료인",
            "executive/managerial": "관리직",
            farmer: "농장주",
            homemaker: "가정부",
            lawyer: "법조인",
            programmer: "프로그래머",
            "sales/marketing": "판매원",
            scientist: "과학자",
            "self-employed": "자영업",
            "technician/engineer": "기술자",
            "tradesman/craftsman": "수공업자",
            writer: "작가"
          }
        },
        {
          type: "성별",
          selectObject: {
            M: "남성",
            F: "여성"
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
  padding: 40px 0;
  background-color: #111;
  div + div {
    margin-top: 60px;
  }
}
</style>