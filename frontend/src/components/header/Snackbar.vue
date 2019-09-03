<template>
  <div>
    <v-snackbar v-model="snackbar" :timeout="usage === 'message' ? 3000 : 0" top>
      {{ text }}
      <v-btn v-if="usage === 'ask'" dark text @click="confirmSnackbar">Confirm</v-btn>
      <v-btn dark text @click="setSnackbar()">Close</v-btn>
    </v-snackbar>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "SnackBar",
  computed: {
    ...mapGetters("snackbar", ["snackbar", "confirm", "usage", "text"])
  },
  watch: {
    confirm() {
      // snackbar 를 사용하는 컴포넌트에서
      // confirm 을 watch 하고 true 가 되면, target 이 해당 컴포넌트 인지 확인하고
      // 맞다면 callback 함수를 실행해주면 된다.
      // if (this.confirm && this.target === "rating") {
      //   this.deleteRating();
      //   this.setSnackbar({
      //     usage: "message",
      //     text: "해당 평점이 삭제 되었습니다."
      //   });
      // }
    }
  },
  mounted() {
    // confirm alert example
    this.setSnackbar({
      usage: "ask",
      target: "rating",
      text: "이 평점을 삭제하시겠습니까?"
    });
    // // message alert example
    // this.setSnackbar({
    //   usage: "message",
    //   text: "로그인 되었습니다."
    // });
  },
  methods: {
    ...mapActions("snackbar", ["setSnackbar", "confirmSnackbar"])
  }
};
</script>