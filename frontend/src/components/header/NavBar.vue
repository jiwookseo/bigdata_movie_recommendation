<template>
  <nav class="nav">
    <div class="nav__title">
      <router-link to="/">
        <span class="txt-orange">
          HONEY BEE
        </span>
      </router-link>
    </div>
    <div class="nav__icon-bar">
      <span>
        <font-awesome-icon icon="search" size="2x" />
      </span>
      <span v-if="!getIsLogin">
        <v-icon class="login_icon" @click="sign">vpn_key</v-icon>
      </span>
      <span v-else class="user_span">
        <router-link :to="profile">
          <font-awesome-icon icon="user" class="login_icon" />
        </router-link>
        <button @click="signout">
          <i class="material-icons login_icon">meeting_room</i>
        </button>
      </span>
    </div>
  </nav>
</template>
​
<script>
  /* Requirements for use fontawesome & How to Use
     1. library 를 @fontawesome/fontawesome-svg-core 에서 import 하세요
     2. @fontawesome/free-solid-svg-icons에서 필요한 아이콘을 import 하세요
        (font-awesome 사이트에서 fas-fa-user인 경우 faUser로 import 하면 됩니다.)
     3. import 해온 것을 library에 add 합니다.
     4. FontAwesomeIcon의 경우 <template>내부에 <font-awesome-icon /> 으로 정의하고, icon값에 위에 import 한 icon에서 fa를 빼고 소문자로 입력하시면 됩니다.
     ex) faSearch => <font-awesome-icon icon="search" />
     참고) https://github.com/FortAwesome/vue-fontawesome
  */
  import { library } from '@fortawesome/fontawesome-svg-core'
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
  import { faSearch, faUser } from '@fortawesome/free-solid-svg-icons'
  import { mapState, mapActions } from "vuex"

library.add(faSearch, faUser)

export default {
  name: "Header",
  components: {
    FontAwesomeIcon,
  },
  data: () => ({
    sign() {
      const modal = document.getElementsByClassName("sign_modal")[0];
      modal.style.display = "flex";
    },
    userState: false,
    profile: "profile",
    admin: "http://localhost:8081/admin",
  }),
  computed: {
    ...mapState({getIsLogin: state => state.data.isLogin}),
    ...mapState({getUsername: state => state.data.username}),
  },
  methods: {
    ...mapActions("data", ["logout"]),
    async signout() {
      const params = {
        "username": this.getUsername
      };
      await this.logout(params);
    }
  }
}
</script>

<style lang="scss" scoped>
  .nav {
    z-index: 10;
    height: 64px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: rgb(33, 33, 33);
    opacity: 0.8;
    width: 100%;
    padding: {
      left: 30px;
      right: 30px;
    }
  }

  .nav__title {

    font-size: 24px;
    font-weight: 700;
    cursor: pointer;

    a {
      text-decoration: none;
    }
  }

  .nav__icon-bar {
    margin-right: 20px;
    display: flex;
    align-items: center;
    justify-content: space-around;

    span {
      cursor: pointer;
      color: rgba(255, 177, 1, 0.7);

      &:hover {
        color: rgb(255, 177, 1);
      }
    }
  }

  .login_icon {
    color: rgba(255, 177, 1, 0.7) !important;
    transform: scale(1.5);
    margin: {
      left: 30px;
    };
  }
  .login_icon:hover {
    color: rgb(255, 177, 1) !important;
  }
  .user_span {
    display: flex;
    align-items: center;

    button {
      outline: none;
    }
  }
</style>
