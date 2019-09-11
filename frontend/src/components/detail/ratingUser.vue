<template>
  <div>
    <span>{{ id }}</span>
    <span>{{ username }}</span>
    <span>{{ rating }}</span>
  </div>
</template>

<script>
export default {
  props: {
    id: {
      type: Number,
      default: 0
    },
    username: {
      type: String,
      default: "",
    },
    rating: {
      type: Number,
      default: 0,
    }
  },
  name: "ratingUser",
  date: () => ({
    rating: 0,
  }),
  methods: {
    check() {

    }
  }
}
</script>

<style>
span {
  color: white;
}
</style>
