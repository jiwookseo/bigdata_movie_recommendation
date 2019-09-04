<template>
  <v-form ref="form">
    <v-text-field v-model="title" label="키워드를 입력하세요" />
    <v-btn large color="indigo white--text" @click="onSubmit">Search</v-btn>
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