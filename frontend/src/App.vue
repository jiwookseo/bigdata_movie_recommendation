<template>
  <div class="app">
    <Header />
    <router-view />
    
  </div>
</template>

<script>
import router from "./router";
import "./reset.css";
import Header from "./components/header/index";

export default {
  components: {
    Header,
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
      },
    ]
  }),
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