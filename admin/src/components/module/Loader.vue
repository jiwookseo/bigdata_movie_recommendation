<template>
  <div class="loader">
    <div class="loader-box box1"></div>
    <div class="loader-box box2"></div>
    <div class="loader-box box3"></div>
  </div>
</template>

<script>

</script>

<style scoped lang="scss">
.loader {
  height: 100px;
  width: 50%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.loader-box {
  height: 100%;
  width: 20%;
  background-color: #1867C0;
  animation-name: load;
  animation-duration: 1.5s;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
  animation-fill-mode: backwards;
}

.box1 {
  animation-delay: 0;
}

.box2 {
  animation-delay: 0.5s;
}

.box3 {
  animation-delay: 1s;
}

@keyframes load {
  from {
    transform: scale(0, 0);
    opacity: 1;
  }

  to {
    transform: scale(1, 1);
    opacity: 0.2;
  }
}
</style>