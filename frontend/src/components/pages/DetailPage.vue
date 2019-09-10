<template>
  <div class="detail-page">
    <detail />
  </div>
</template>

<script>
import detail from '../detail'

export default {
  name: "DetailPage",
  components: {
    detail
  }
}
</script>

<style lang="scss" scoped>
.detail-page { margin-top: 64px; }
</style>