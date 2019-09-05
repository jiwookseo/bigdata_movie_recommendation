<template>
  <v-form ref="form" class="search_form">
    <v-text-field v-model="title" class="search_input" label="키워드를 입력하세요" />
    <v-btn large class="search_button" @click="onSubmit">Search</v-btn>
  </v-form>
</template>

<script>
export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    }
  },
  data: () => ({
    title: ""
  }),
  methods: {
    onSubmit: function() {
      const params = {
        title: this.title,
      };
      
      this.submit(params);
    }
  }
};
</script>

<style lang="scss">
.search_input {
  padding: 0 !important;
  width: 250px;
  height: 60px !important;
}

.search_button {
  color: white !important;
  background: {
    color: indigo !important;
  }
  height: 40px !important;
  margin: {
    left: 10px;
    right: 10px;
  };
}

.search_form {
  display: flex;
  flex-direction: row;
  height: 60px !important;
}
</style>