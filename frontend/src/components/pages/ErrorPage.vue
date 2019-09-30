<template>
  <div class="error-page-div">
    <img src="../../../public/sad_bumblebee.png" />
    <p>페이지를 찾을 수 없어요 😥😥</p>
  </div>
</template>

<script>
  export default {
    name: "ErrorPage"
  }
</script>

<style lang="scss" scoped>
  .error-page-div {
    width: 100vw;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #111;
    color: #fff;
    img {
      border-radius: 30%;
    }
    p {
      margin-top: 40px;
      font-family: 'Jua';
      font-size: 36px;
      font-weight: 500;
    }
  }
</style>