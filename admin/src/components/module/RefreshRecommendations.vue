<template>
  <div class="search-form-container">
    <v-btn class="search_form" @click="refresh">{{ text }}</v-btn>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    text: "Recommendations refresh",
    recData: [
      {
        type: "age",
        value: [1, 18, 25, 35, 45, 50, 56]
      },
      {
        type: "occupation",
        value: [
          "academic/educator",
          "artist",
          "clerical/admin",
          "college/grad student",
          "K-12 student",
          "customer service",
          "doctor/health care",
          "executive/managerial",
          "farmer",
          "homemaker",
          "lawyer",
          "programmer",
          "sales/marketing",
          "scientist",
          "self-employed",
          "technician/engineer",
          "tradesman/craftsman",
          "writer"
        ]
      },
      {
        type: "gender",
        value: ["M", "F"]
      }
    ]
  }),
  methods: {
    refresh: function() {
      this.text = "Proceeding...";
      axios
        .post("../api/movies/recommendations/")
        .then(() => (this.text = "Recommendations refresh"));
    }
  }
};
</script>

<style lang="scss">
.search-form-container {
  width: 50%;
  display: flex;
  padding: 0 5%;
  justify-content: space-around;
  align-items: center;
}

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
  }
}

.search_form {
  display: flex;
  flex-direction: row;
  height: 40px !important;
}
</style>