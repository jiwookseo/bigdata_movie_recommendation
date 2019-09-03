<template>
  <div>
    {{ id }} | {{ title }}
  </div>
</template>

<script>
export default {
  props: {
    id: {
      type: Number,
      default: 0
    },
    title: {
      type: String,
      default: ""
    },
    genres: {
      type: Array,
      default: () => new Array()
    },
    img: {
      type: String,
      default: ""
    },
    rating: {
      type: Number,
      default: 0.0
    },
    viewCnt: {
      type: Number,
      default: 0
    }
  },
  computed: {
    genresStr: function() {
      return this.genres.join(" / ");
    },
  }
}
</script>

<style scoped>

</style>