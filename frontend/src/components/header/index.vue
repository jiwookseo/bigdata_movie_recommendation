<template>
  <header class="header">
    <NavBar />
    <Sign />
  </header>
</template>

<script>
import NavBar from "./NavBar";
import Sign from "./Sign";

export default {
  name: "Header",
  components: {
    NavBar,
    Sign
  },
  mounted() {
    this.checkLogin();
  },
  methods: {
    checkLogin() {
      if (sessionStorage.getItem("isLogin") !== null) {
        this.$store.state.user.isLogin = sessionStorage.getItem("isLogin");
      }
      if (sessionStorage.getItem("jwt") !== null) {
        this.$store.state.user.token = sessionStorage.getItem("jwt");
      }
      if (sessionStorage.getItem("username") !== null) {
        this.$store.state.user.username = sessionStorage.getItem("username");
      }
      if (sessionStorage.getItem("isStaff") !== null) {
        this.$store.state.user.checkStaff = sessionStorage.getItem("isStaff");
      }
      if (sessionStorage.getItem("subscribe") !== null) {
        this.$store.state.user.subscribe = sessionStorage.getItem("subscribe");
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.header {
  position: absolute;
  width: 100vw;
}
</style>