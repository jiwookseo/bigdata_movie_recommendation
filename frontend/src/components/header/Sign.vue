<template>
  <div class="sign_modal">
    <div class="sign_contents">
      <div v-if="form === 'sign'" class="sign">
        <div class="sign_div">
          <p class="sign_title">Member Login</p>
          <div class="signin">
            <input id="insert_id" v-model="loginInput.username" type="text" required>
            <label for="insert_id">Username</label>
            <input id="insert_pw" v-model="loginInput.password" type="password" class="mt-30" required>
            <label for="insert_pw">Password</label>
          </div>
          <button class="sign_button" @click="login" @keydown.enter="login">Login</button>
          <div class="pw_reg">
            <button class="password_button">Forget password?</button>
            <button class="register_button" @click="changeForm">Register</button>
          </div>
        </div>
      </div>
      <div v-if="form === 'register'" class="register">
        <div class="sign_div">
          <p class="sign_title">Register</p>
          <div class="register_form">
            <input id="username" v-model="regInput.username" type="text" required>
            <label for="username">Username</label>
            <input id="password1" v-model="regInput.password1" type="password" class="mt-30" required>
            <label for="password1">Password</label>
            <input id="password2" v-model="regInput.password2" type="password" class="mt-30" required>
            <label for="password2">Password</label>
            <div class="age mt-30">
              <label for="age">age</label>
              <input id="age" v-model="regInput.age" type="number" required>
            </div>
            <div class="gender mt-30">
              <p class="gender_title">gender</p>
              <label for="gender_F">Female</label>
              <input id="gender_F" v-model="regInput.gender" value="F" type="radio" required>
              <label for="gender_M">Male</label>
              <input id="gender_M" v-model="regInput.gender" value="M" type="radio" required>
            </div>
            <input id="occupation" v-model="regInput.occupation" type="text" class="mt-30" required>
            <label for="occupation">occupation</label>
          </div>
          <button class="sign_button" @click="register" @keydown.enter="register">Register</button>
        </div>
      </div>
      <div class="sign_image"></div>
    </div>
  </div>
</template>
<script>
  import { mapState, mapActions } from "vuex";
  export default {
    name: "Sign",
    data: () => ({
      loginInput: {
        username: "",
        password: "",
      },
      username: "",
      form: "sign",
      regInput: {
        username: "",
        password1: "",
        password2: "",
        age: 0,
        gender: "",
        occupation: ""
      }
    }),
    mounted() {
      this.closeModal(this.resetForm);
    },
    computed: {
      ...mapState({getUsername: state => state.data.username}),
      ...mapState({getRegister: state => state.data.register})
    },
    methods: {
      closeModal(func) {
        const modal = document.getElementsByClassName("sign_modal")[0];
        const change = func;
        window.onclick = function(e) {
          if (e.target === modal) {
            modal.style.display = "none";
            change();
          }
        };
      },
      ...mapActions("data", ["setLogin"]),
      ...mapActions("data", ["setRegister"]),
      async login() {
        const params = {
          "login": this.loginInput
        };
        await this.setLogin(params);
        this.username = this.getUsername;
      },
      changeForm() {
        if (this.form === "register") {
          this.form = "sign";
        } else {
          this.form = "register";
        }
      },
      resetForm() {
        this.form = "sign"
      },
      async register() {
        const params = {
          "profiles": [this.regInput]
        };
        await this.setRegister(params);
        this.form = this.getRegister;
      }
    }
  }
</script>
<style lang="scss" scoped>
  .sign_modal {
    position: fixed;
    z-index: 1;
    display: none;
    left: 0;
    top: 0;
    width: 100vw;
    height: 100vh;
    background: {
      color: rgba(0, 0, 0, 0.5);
    };
    justify: {
      content: center;
    };
    align: {
      items: center;
    }
  }
  .sign_contents {
    background: {
      color: rgb(255, 255, 255);
    };
    width: 70%;
    height: 60%;
    display: flex;
    border: {
      radius: 15px;
    };
  }
  .sign, .register {
    margin: {
      top: auto;
      bottom: auto;
    }
  }
  .sign_div {
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
  .sign_image {
    overflow: hidden;
    width: 100%;
    height: 100%;
    background: {
      image: url("../../../public/modalImg.jpg");
      size: cover;
      position: center center;
      repeat: no-repeat;
    }
    border: {
      radius: 0px 15px 15px 0px;
    };
  }
  #insert_id, #insert_pw, #username, #password1, #password2, #occupation {
    position: relative;
    z-index: 2;
    top: 20px;
    border: {
      bottom: rgba(117, 117, 117, 0.68) 1.5px solid;
    };
    min-height: 16px;
    max-height: 16px;
  }
  #insert_id + label, #insert_pw + label, #username + label, #password1 + label, #password2 + label, #occupation + label {
    transition: all .5s ease;
    position: relative;
    top: 0px;
    z-index: 1;
    white-space: nowrap;
    color: rgba(117, 117, 117, 0.68);
    font-size: 16px;
    min-height: 16px;
    max-height: 16px;
  }
  #insert_id:focus + label, #insert_pw:focus + label, #username:focus + label, #password1:focus + label, #password2:focus + label, #occupation:focus + label {
    top: -20px;
    font: {
      size: 12px;
    };
    text: {
      align: left;
    };
    min-height: 16px;
    max-height: 16px;
  }
  #insert_id:valid + label, #insert_pw:valid + label, #username:valid + label, #password1:valid + label, #password2:valid + label, #occupation:valid + label {
    top: -20px;
    font: {
      size: 12px;
    };
    text: {
      align: left;
    };
  }
  #insert_id:focus, #insert_pw:focus, #username:focus, #password1:focus, #password2:focus, #occupation:focus {
    border: {
      bottom: rgba(255, 183, 0, 1.0) 2px solid;
    };
    transition: all .5s ease;
    outline: none;
    min-height: 16px;
    max-height: 16px;
  }
  .mt-30 {
    margin: {
      top: 30px;
    };
  }
  @media screen and (max-width: 600px) {
    .sign_image {
      display: none;
    }
    .sign_contents {
      width: 380px;
    }
  }
  .sign_title {
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
      size: 25px;
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
  .pw_reg {
    font: {
      family: Consolas;
    };
    display: flex;
    flex: {
      direction: column;
    };
  }
  .password_button, .register_button {
    color: rgba(255, 183, 0, 1.0);
    font: {
      size: 20px;
    };
    text: {
      align: center;
    };
    margin: {
      top: 20px;
    };
    outline: none;
  }
  .register_form {
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
  .age, .gender {
    display: flex;
    justify: {
      content: space-between;
    }
    color: rgba(117, 117, 117, 0.68);
  }
  #age {
    border: {
      bottom: rgba(117, 117, 117, 0.68) 1.5px solid;
    }
    outline: none;
  }
</style>
