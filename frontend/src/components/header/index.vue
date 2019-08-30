<template>
  <header class="header">
    <NavBar />
    <div class="test" />
  </header>
</template>

<script>
  import NavBar from "./NavBar"

  export default {
    name: "Header",
    components: {
      NavBar
    }
  }
</script>

<style lang="scss" scoped>
.header {
  position: absolute;
  width: 100vw;
}


</style>