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
    }
  }
</script>

<style lang="scss" scoped>
.header {
  position: absolute;
  width: 100vw;
}


</style>