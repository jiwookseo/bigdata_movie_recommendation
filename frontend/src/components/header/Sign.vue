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

<!--      회원가입-->
      <div v-if="form === 'register'" class="register">
        <Snackbar v-if="snackbar"/>
        <div class="sign_div">
          <div class="sign_title_div">
            <button class="back_button">
              <i aria-hidden="true" class="v-icon mdi mdi-arrow-left hb-color" />
            </button>
            <p class="sign_title">Register</p>
          </div>
          <div class="register_form">
            <input id="username" v-model="reg_username" type="text" required>
            <label for="username">Username</label>
            <span>{{ err_username }}</span>
            <input id="password1" v-model="reg_password1" type="password" class="mt-30" required>
            <label for="password1">Password</label>
            <span>{{ err_password1 }}</span>
            <input id="password2" v-model="reg_password2" type="password" class="mt-30" required>
            <label for="password2">Confirm Password</label>
            <span>{{ err_password2 }}</span>
            <div class="gender mt-30">
              <p class="gender_title">gender</p>
              <label for="gender_F">Female</label>
              <input id="gender_F" v-model="reg_gender" value="F" type="radio" required>
              <label for="gender_M">Male</label>
              <input id="gender_M" v-model="reg_gender" value="M" type="radio" required>
            </div>
            <span>{{ err_gender }}</span>
            <div class="age mt-30">
              <label for="age">age</label>
              <select id="age" v-model="reg_age" required>
                <option v-for="(age, i) of ageList" :key="age + i" :value="i">{{ age }}</option>
              </select>
            </div>
            <span>{{ err_age }}</span>
            <div class="occupation mt-30">
              <label for="occupation">occupation</label>
              <select id="occupation" v-model="reg_occupation" required>
                <option v-for="(occupation, i) of occupationList" :key="occupation + i" :value="i">{{ occupation }}</option>
              </select>
            </div>
            <span>{{ err_occupation }}</span>
          </div>
          <div class="buttons">
            <button v-if="checkRegister" class="sign_button" @click="register" @keydown.enter="register">Register</button>
            <button v-else class="disabled_button" disabled>Register</button>
          </div>
        </div>
      </div>
      <div class="sign_image" />
    </div>
    <div class="text-center">
      <v-snackbar v-model="snackbar" :multi-line="multiLine">
        {{ text }}
        <v-btn color="red" text @click="snackbar = false">
          Close
        </v-btn>
      </v-snackbar>
    </div>
  </div>
</template>


<script>
  import { mapState, mapActions } from "vuex";

  export default {
    name: "Sign",
    data: () => ({
      multiLine: true,
      snackbar: false,
      text: '회원이 되신 것을 환영합니다 :)',
      loginInput: {
        username: "",
        password: "",
      },
      reg_username: "",
      reg_password1: "",
      reg_password2: "",
      reg_age: "",
      reg_gender: "",
      reg_occupation: "",
      err_username: "",
      err_password1: "",
      err_password2: "",
      err_age: "",
      err_gender: "",
      err_occupation: "",
      username: "",
      form: "sign",
      checkRegister: false,
      ageList: ["Under 18", "18-24", "25-34", "35-44", "45-49", "50-55", "56+"],
      ages: ["1", "18", "25", "35", "45", "50", "56"],
      occupationList: [
        "other", "academic/educator", "artist", "clerical/admin", "college/grad student", "customer service", "doctor/health care",
        "executive/managerial", "farmer", "homemaker", "K-12 student", "lawyer", "programmer", "retired", "sales/marketing",
        "scientist", "self-employed", "technician/engineer", "tradesman/craftsman", "unemployed", "writer"
      ],
    }),
    computed: {
      ...mapState({getUsername: state => state.data.username}),
      ...mapState({getRegister: state => state.data.register})
    },
    watch: {
      reg_username: function() {
        this.chkUsername();
      },
      reg_password1: function() {
        this.chkPass1();
      },
      reg_password2: function() {
        this.chkPass2();
      },
      reg_age: function() {
        this.chkAge();
      },
      reg_gender: function() {
        this.chkGender();
      },
      reg_occupation: function() {
        this.chkOccupation();
      }
    },
    mounted() {
      this.closeModal(this.resetForm);
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
          this.snackbar = false;
          this.form = "register";
        }
      },
      resetForm() {
        this.form = "sign"
      },
      async register() {
        this.chkRegister();
        if (this.checkRegister) {
          const params = {
            "profiles": [
              {
                "username": this.reg_username,
                "password1": this.reg_password1,
                "password2": this.reg_password2,
                "age": this.reg_age,
                "gender": this.reg_gender,
                "occupation": this.reg_occupation,
              }
            ]
          };
          await this.setRegister(params);
          const s = this.getRegister;
          if (s === "sign") {
            this.snackbar = true;
            this.form = s
          } else {
            this.snackbar = false;
          }
        }
      },
      chkUsername() {
        if (this.reg_username.length < 6) {
          this.err_username = "username의 길이는 6자 이상이어야 합니다.";
        } else {
          this.err_username = "";
        }
        this.chkRegister();
      },
      chkPass1() {
        if (this.reg_password1.length < 8) {
          this.err_password1 = "password의 길이는 8자 이상이어야 합니다.";
          this.checkRegister = false;
        } else {
          this.err_password1 = "";
        }
        this.chkRegister();
      },
      chkPass2() {
        if (this.reg_password1 !== this.reg_password2) {
          this.err_password2 = "password가 일치하지 않습니다.";
        } else {
          this.err_password2 = "";
        }
        this.chkRegister();
      },
      chkAge() {
        if (typeof(this.reg_age) === "number" && this.ages[this.reg_age] !== undefined) {
          this.err_age = "";
        } else {
          this.err_age = "age를 선택해주세요.";
        }
        this.chkRegister();
      },
      chkGender() {
        if (this.reg_gender === "M" || this.reg_gender === "F") {
          this.err_gender = "";
        } else {
          this.err_gender = "gender를 선택해주세요.";
        }
        this.chkRegister();
      },
      chkOccupation() {
        if (typeof(this.reg_occupation) === "number" && this.occupationList[this.reg_occupation] !== undefined) {
          this.err_occupation = "";
        } else {
          this.err_occupation = "occupation을 선택해주세요.";
        }
        this.chkRegister();
      },
      chkRegister() {
        if (this.reg_username && this.reg_password1 && this.reg_password2 && this.ages[this.reg_age] !== undefined && this.reg_gender && this.occupationList[this.reg_occupation] !== undefined && !this.err_username && !this.err_password1 && !this.err_password2 && !this.err_age && !this.err_gender && !this.err_occupation) {
          this.checkRegister = true;
        } else {
          this.checkRegister = false;
        }
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
    };
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
  #insert_id:focus + label, #insert_pw:focus + label, #username:focus + label, #password1:focus + label, #password2:focus + label {
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
  #insert_id:valid + label, #insert_pw:valid + label, #username:valid + label, #password1:valid + label, #password2:valid + label {
    top: -20px;
    font: {
      size: 12px;
    };
    text: {
      align: left;
    };
  }
  #insert_id:focus, #insert_pw:focus, #username:focus, #password1:focus, #password2:focus {
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
  @media screen and (max-width: 600px) {
    .sign_image {
      display: none;
    }
    .sign_contents {
      width: 380px;
    }
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
  .disabled_button {
    background: {
      color: rgba(117, 117, 117, 0.4)
    };
    font: {
      family: Consolas;
      size: 24px;
      weight: bold;
    };
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
    width: 100%;
    margin: {
      left: 10px;
    }
    border: {
      bottom: rgba(117, 117, 117, 0.68) 1.5px solid;
    }
    outline: none;
  }
  .occupation {
    display: flex;
    justify: {
      content: space-between;
    };
    color: rgba(117, 117, 117, 0.68);
  }
  #occupation {
    width: 100%;
    margin: {
      left: 10px;
    };
    border: {
      bottom: rgba(117, 117, 117, 0.68) 1.5px solid;
    };
    outline: none;
  }
  .back_button {
    position: absolute;
    margin: {
      right: 100%;
    };
    background: {
      color: rgba(117, 117, 117, 0.18);
    };
    border: {
      radius: 15px;
    };
    width: 30px;
    height: 30px;
  }
  .hb-color {
    color: rgba(255, 183, 0, 1.0);
  }
</style>
