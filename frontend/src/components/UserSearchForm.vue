<template>
  <v-container>
    <v-text-field class="search_input" v-model="params.username" @keydown.enter="onSubmit" label="유저 이름"></v-text-field>
    <v-layout justify-center pa-10>
      <v-btn large color="indigo white--text" @click="onSubmit">Search</v-btn>
    </v-layout>
    </v-container>
</template>

<script>
export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    },
  },
  data: () => ({
    params: {
      username: "",
    },
    btn: "title",
  }),
  created() {
    this.onSubmit();
  },
  methods: {
    onSubmit() {
      this.submit(this.params);
    },
  }
};
</script>

<style>
.search_buttons {
  display: flex;
  justify-content: space-between;
}

.search_button > button {
  padding: 0px 10px 0px 10px !important;
}

.search_button > button > span {
  font-size: 18px;
  font-weight: bold;
}

.genre_button {
  width: 18%;
  margin: 0px 1% 0px 1%;
  overflow: hidden;
}

.search_input {
  padding: 12px;
}
</style>