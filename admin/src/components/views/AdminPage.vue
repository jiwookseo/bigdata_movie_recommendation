<template>
  <div class="content-container">
    <div v-if="form === 'sign'" class="sign">
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
    <div v-else>
      <div class="data-controller-container">
        <search-form :submit="searchMovies" />
        <v-btn @click="clustering">clustering</v-btn>
      </div>

      <div class="data-list-container">
        <div class="data-list-header">
          <div class="list-header-table" :class="[ directory === 'movie'? 'selected' : '' ]" @click="selectTable">Movie</div>
          <div class="list-header-table" :class="[ directory === 'user'? 'selected' : '' ]" @click="selectTable">User</div>
        </div>
        <div class="data-list-content">
          <router-view />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import SearchForm from '../module/SearchForm'

export default {
  components: {
    SearchForm,
  },
  computed: {
    ...mapState({getStaff: state => state.user.checkStaff}),
    ...mapState({getLogError: state => state.user.logErrors}),
  },
  data() {
    return {
      directory: 'movie',
      loginInput: {
        username: "",
        password: ""
      },
      err_login: "",
      form: "sign"
    }
  },
  methods: {
    ...mapActions('movie', ['searchMovies', 'clusteringMovies']),
    ...mapActions('user', ['clusteringUsers', 'getRelatedUsers']),
    selectTable(e) {
      const keyword = e.target.innerHTML.toLowerCase();
      this.directory = keyword
      this.$router.push({
        name: `${keyword}-list`
      })
    },
    clustering() {
      const params = {
        method: 'em',
        k: 5
      }
      if (this.$route.path === '/admin/movies') {
        this.clusteringMovies(params)
      } else {
        this.clusteringUsers(params)
      }
    },
    test() {
      const params = {
        userId: 1
      }
      this.getRelatedUsers(params);
    },
    // login
    ...mapActions("user", ["setLogin"]),
    async login() {
      const params = {
        "login": this.loginInput
      };
      await this.setLogin(params);
      if (this.getStaff === true) {
        this.form = "admin";
        this.loginInput.username = "";
        this.loginInput.password = "";
        this.err_login = "";
      } else {
        this.err_login += "관리자만 로그인이 가능합니다. 계정을 확인하세요.";
      }
    },
  }
}
</script>

<style scoped lang="scss">

.data-controller-container {
  display: flex;
  height: 15vh;
  padding-bottom: 2vh;
}


.data-list-header {
  display: flex;
  height: 10vh;
  justify-content: left;
  align-items: flex-end;
}

.list-header-table {
  width: 15vw;
  margin: 0 0 0 2vw;
  padding: 0 1vw;
  color: white;
  font-size: 3vh;
  text-align: center;
  border-radius: 10px 10px 0 0;
  background-color: #1867C0;
  transition: all 1s;

  &:hover {
    color: #1867C0;
    background-color: white;
  }
}

.selected {
  color: #1867C0;
  background-color: white;
  box-shadow: 1px -1px 3px gray;
  &:hover {
    background-color: #1867C0;
    color: white;
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