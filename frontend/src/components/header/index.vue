<template>
  <header class="header">
    <NavBar />
    <JumboTron />
    
    <div class="test" />
  </header>
</template>

<script>
  import NavBar from "./NavBar"
  import JumboTron from "./Jumbotron"

  export default {
    name: "Header",
    components: {
      NavBar, JumboTron
    }
  }
</script>

<style lang="scss" scoped>
.header {
  position: absolute;
  width: 100vw;
}


</style>