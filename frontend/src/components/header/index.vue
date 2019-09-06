<template>
  <header class="header">
    <NavBar />
    <Sign />
  </header>
</template>

<script>
  import NavBar from "./NavBar"
  import Sign from "./Sign"

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
          this.$store.state.data.isLogin = sessionStorage.getItem("isLogin");
        }
        if (sessionStorage.getItem("jwt") !== null) {
          this.$store.state.data.token = sessionStorage.getItem("jwt");
        }
        if (sessionStorage.getItem("username") !== null) {
          this.$store.state.data.username = sessionStorage.getItem("username");
        }
        if (sessionStorage.getItem("isStaff") !== null) {
          this.$store.state.data.checkStaff = sessionStorage.getItem("isStaff");
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
.header {
  position: absolute;
  width: 100vw;
}


</style>