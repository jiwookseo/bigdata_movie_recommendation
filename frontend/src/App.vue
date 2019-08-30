<template>
  <div class="app">
    <Header />
    <Jumbotron />
    <ImageSlider />
  </div>
</template>

<script>
import router from "./router";
import './reset.css';
import Header from "./components/header/index"
import Jumbotron from "./components/header/Jumbotron"
import ImageSlider from "./components/imageSlider/index"
import { mapGetters } from "vuex";

export default {
  components: {
    Jumbotron,
    Header,
    ImageSlider
  },
  data: () => ({
    drawer: null,
    choices: [
      {
        icon: "mdi-movie",
        text: "영화 검색",
        path: "movie-search"
      },
      {
        icon: "people",
        text: "유저 검색",
        path: "user-search"
      }
    ]
  }),
  computed: {
    ...mapGetters("data", ["recommendation"])
  },
  mounted() {
    this.$store.dispatch("data/getRecByAge", 18);
    this.$store.dispatch("data/getRecByOccupation", "artist");
    this.$store.dispatch("data/getRecByGender", "M");
  },
  methods: {
    goTo: function(path) {
      router.push({ name: path });
    }
  }
};
</script>

<style lang="scss" scoped>
  .app {
    width: 100vw;
    overflow-x: hidden;
  }

  
</style>