<template>
  <div class="input-form-container">
    <span class="input-form">
      <v-btn class="refresh-button" @click="refresh">
        <span v-if="!isProceeding">
          <i class="fas fa-redo"></i>
        </span>
        <span v-else>
          <i class="fas fa-ellipsis-h"></i>
        </span>
      </v-btn>
    </span>
  </div>
</template>

<script>
import axios from "axios";
import { mapMutations, mapActions } from "vuex";
import api from "../../api"

export default {
  data: () => ({
    isProceeding: false,
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
    ...mapMutations("loader", ["toggleLoader"]),
    
    async refresh() {
      this.toggleLoader();
      try {
        this.isProceeding = !this.isProceeding;
        await api.recommendation();
        this.isProceeding = !this.isProceeding;
      } catch (error) {
        console.log(error);
      }
      this.toggleLoader();
    }
  }
};
</script>

<style lang="scss" scoped>
@import "@/mixin/style/_dataControllerForm";
</style>