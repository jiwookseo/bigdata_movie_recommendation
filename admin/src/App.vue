<template>
  <div id="app">
    <!-- NavBar -->
    <div class="navbar">
      <div class="navbar-title"><i class="fas fa-user-shield"></i> ADMIN PAGE</div>
      <div v-if="getStaff"><i class="fas fa-sign-out-alt" @click="signout"></i></div>
    </div>
    <div v-if="!getStaff" class="sign">
      <div class="sign_div">
        <p class="sign_title">Admin Login</p>
        <div class="signin">
          <input id="insert_id" v-model="loginInput.username" type="text" required @keydown.enter="login">
          <label for="insert_id">Username</label>
          <input id="insert_pw" v-model="loginInput.password" type="password" class="mt-30" required @keydown.enter="login">
          <label for="insert_pw">Password</label>
          <span>{{ err_login }}</span>
        </div>
        <button class="sign_button" @click="login">Login</button>
      </div>
    </div>
    <!-- Content Container -->
    <router-view v-else />
  </div>
</template>

<script>
import router from "./router";
import { mapState, mapActions } from 'vuex'

export default {
  computed: {
    ...mapState({getStaff: state => state.user.checkStaff}),
    ...mapState({getError: state => state.user.logErrors}),
    ...mapState({getUsername: state => state.user.username}),
  },
  watch: {
    getStaff: function() {
      if (this.getStaff) {
        this.getMovieList();
        this.getUserList();
      }
    }
  },
  mounted() {
    this.checkLogin();
  },
  data: () => ({
    loginInput: {
      username: "",
      password: ""
    },
    err_login: "",
    form: "sign"
  }),
  methods: {
    ...mapActions('movie', ['getMovieList']),
    ...mapActions('user', ['getUserList']),
    // login
    ...mapActions("user", ["setLogin"]),
    ...mapActions("user", ["logout"]),
    async login() {
      const params = {
        "login": this.loginInput,
        "admin": true,
      };
      await this.setLogin(params);
      if (!this.getError) {
        this.form = "admin";
        this.loginInput.username = "";
        this.loginInput.password = "";
      }
      this.err_login = this.getError;
    },
    checkLogin() {
      if (sessionStorage.getItem("adminLogin") !== null) {
        this.$store.state.user.isLogin = sessionStorage.getItem("adminLogin");
      }
      if (sessionStorage.getItem("adminName") !== null) {
        this.$store.state.user.username = sessionStorage.getItem("adminName");
      }
      if (sessionStorage.getItem("adminCheck") !== null) {
        this.$store.state.user.checkStaff = sessionStorage.getItem("adminCheck");
      }
      if (sessionStorage.getItem("adminToken") !== null) {
        this.$store.state.user.token = sessionStorage.getItem("adminToken");
      }
    },
    async signout() {
      const params = {
        username: this.getUsername
      };
      await this.logout(params);
    },
    ...mapActions("user", ["logout"]),
  },
};
</script>

<style lang="scss">

ul {
  list-style-type: none;
}

.navbar {
  background-color: #1867C0;
  height: 5vh;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  .fa-sign-out-alt {
    margin-right: 30px;
    transform: scale(1.5);
  }

  .navbar-title {
    margin-left: 3vw;
    font-size: 2.5vh;
  }
}
.sign, .register {
  margin: {
    top: auto;
    bottom: auto;
  }
  display: flex;
  justify-content: center;
}
.sign_div {
  width: 50%;
  min-width: 380px;
  display: flex;
  flex: {
    direction: column;
  };
  align: {
    items: center;
  };
  padding: 20px;
}
#insert_id, #insert_pw, #username, #password1, #password2 {
  position: relative;
  z-index: 2;
  top: 20px;
  border: {
    bottom: rgba(117, 117, 117, 0.68) 1.5px solid;
  };
  min-height: 16px;
  max-height: 16px;
}
#insert_id + label, #insert_pw + label, #username + label, #password1 + label, #password2 + label {
  transition: all .5s ease;
  position: relative;
  top: 0px;
  z-index: 1;
  white-space: nowrap;
  color: rgba(117, 117, 117, 0.68);
  font-size: 16px;
  min-height: 16px;
  max-height: 16px;
  user: {
    select: none;
  }
}
#insert_id:focus + label, #insert_pw:focus + label {
  top: -20px;
  font: {
    size: 12px;
  };
  text: {
    align: left;
  };
  min-height: 16px;
  max-height: 16px;
  user: {
    select: none;
  }
}
#insert_id:valid + label, #insert_pw:valid + label {
  top: -20px;
  font: {
    size: 12px;
  };
  text: {
    align: left;
  };
}
#insert_id:focus, #insert_pw:focus {
  border: {
    bottom: rgba(255, 183, 0, 1.0) 2px solid;
  };
  transition: all .5s ease;
  outline: none;
  min-height: 16px;
  max-height: 16px;
}
label + span {
  margin: {
    top: 10px;
  }
  color: red;
  font: {
    size: 12px;
  }
  user-select: none;
}
.mt-30 {
  margin: {
    top: 30px;
  };
}
.sign_title_div {
  width: 70%;
}
.sign_title {
  text-align: center;
  margin: 0;
  font: {
    family: Consolas;
    size: 24px;
    weight: bold;
  }
  color: rgba(255, 183, 0, 1.0);
}
.signin {
  width: 70%;
  margin: {
    top: 30px;
    bottom: 30px;
  };
  display: flex;
  flex: {
    direction: column;
  };
}
.sign_button {
  background: {
    color: rgba(255, 183, 0, 1.0);
  }
  font: {
    family: Consolas;
    size: 24px;
    weight: bold;
  }
  color: rgb(255, 255, 255);
  padding: 5px 10px 10px 10px;
  line: {
    height: 1.2em;
  };
  border: {
    radius: 15px;
  };
  margin: {
    bottom: 30px;
  };
  outline: none;
}
</style>
