<template>
  <div class="subscribe_div">
    <span class="subscribe_text"><span class="sub_title">HONEY BEE</span>를 구독하시면 다양한 영화를 추천해드려요!</span>
    <button class="subscribe_button" @click="sub">구독(2$/1month)</button>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "subscribe",
  props: {
    newSub: {
      type: Function,
      default: () => {}
    }
  },
  data: () => ({
  }),
  computed: {
    ...mapState({
        getLogin: state => state.user.isLogin,
        getToken: state => state.user.token,
        getUsername: state => state.user.username,
        getSubscribe: state => state.user.subscribe
    })
  },
  methods: {
    ...mapActions("user", ["subscribe"]),
    async sub() {
      if (this.getLogin) {
        const data = {
          "username": this.getUsername,
          "token": this.getToken,
        };
        await this.subscribe(data);
        if (this.getSubscribe === true) {
          this.newSub(true);
        }
      } else {
        const modal = document.getElementsByClassName("sign_modal")[0];
        modal.style.display = "flex";
      }
    }
  }
}
</script>

<style>
.subscribe_text {
  color: white;
  font-size: 30px;
}

.subscribe_button {
  color: white;
  font-size: 30px;
  display: block;
  margin: 30px auto 0px auto;
  outline: none;
}
.subscribe_button:hover {
  color: rgba(255, 183, 0, 1);
  transition: color;
  transition-duration: 1s;
}

.sub_title {
  color: rgba(255, 183, 0, 1);
  font-weight: bold;
}
</style>