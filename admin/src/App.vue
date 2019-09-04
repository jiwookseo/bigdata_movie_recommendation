<template>
  <div id="app">
    <!-- NavBar -->
    <div class="navbar">
      <div class="navbar-title"><i class="fas fa-user-shield"></i> ADMIN PAGE</div>
    </div>

    <!-- Content Container -->
    <router-view />
  </div>
</template>

<script>
import router from "./router";
import { mapActions } from 'vuex'

export default {
  methods: {
    ...mapActions('movie', ['getMovieList']),
    ...mapActions('user', ['getUserList']),
  },
  created() {
    this.getMovieList()
    this.getUserList()
  }
};
</script>

<style lang="scss">

ul {
  list-style-type: none;
}

.navbar {
  background-color: #1867C0;
  height: 5vh;
  color: white;
  display: flex;
  align-items: center;
  .navbar-title {
    margin-left: 3vw;
    font-size: 2.5vh;
  }
}

</style>