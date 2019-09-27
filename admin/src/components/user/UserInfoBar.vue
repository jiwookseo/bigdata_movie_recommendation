<template>
  <div class="data-info-bar">
    <div v-if="user !== idx" class="data-info">
      {{ username }} | {{ gender }} | {{ age }} | {{ occupation }} | {{ isStaff }}
    </div>
    <div v-else class="data-edit">
      <span>{{ username }}</span>
      <div class="gender">
        <label for="gender_F">Female</label>
        <input id="gender_F" v-model="checkGender" value="F" type="radio">
        <label for="gender_M">Male</label>
        <input id="gender_M" v-model="checkGender" value="M" type="radio">
      </div>
      <div class="age">
        <label for="age"></label>
        <select name="age" id="age" v-model="checkAge">
          <option v-for="(age, i) of ages" :value=age>{{ ageList[i] }}</option>
        </select>
      </div>
      <div class="occupation">
        <label for="occupation"></label>
        <select name="occupation" id="occupation" v-model="checkOccupation">
          <option v-for="(occupation, i) of occupationList" :value=i>{{ occupation }}</option>
        </select>
      </div>
      <div class="isStaff">
        <label for="isStaff_T">staff=T</label>
        <input id="isStaff_T" v-model="checkIsStaff" :value="true" type="radio">
        <label for="isStaff_F">staff=F</label>
        <input id="isStaff_F" v-model="checkIsStaff" :value="false" type="radio">
      </div>
    </div>
    <div class="data-controller">
      <i v-if="user === idx" class="fas fa-check" @click="editInfo"></i> | <i class="fas fa-edit" @click="editUser"></i> | <i class="fas fa-trash-alt" @click="delUser"></i>
    </div>
  </div>
</template>

<script>
  import { mapState, mapActions } from "vuex"
  export default {
    props: {
      id: {
        type: Number,
        default: 0
      },
      idx: {
        type: Number,
        default: 0
      },
      username: {
        type: String,
        default: ""
      },
      gender: {
        type: String,
        default: ""
      },
      age: {
        type: Number,
        default: 0
      },
      occupation: {
        type: String,
        default: ""
      },
      isStaff: {
        type: Boolean,
        default: false
      },
      check: {
        type: Function,
        default: () => {}
      },
      user: {
        type: Number,
        default: 0
      },
      edited: {
        type: Function,
        default: () => {}
      }
    },
    computed: {
      ...mapState({getToken: state => state.user.token}),
      ...mapState({getUsername: state => state.user.username}),
      ...mapState({getEdit: state => state.user.editCom}),
      ...mapState({getDel: state => state.user.delCom})
    },
    mounted() {
      this.checkGender = this.gender;
    },
    data: () => ({
      checkGender: "",
      checkAge: 1,
      checkOccupation: 0,
      checkIsStaff: false,
      ages: [1, 18, 25, 35, 45, 50, 56],
      ageList: ["Under 18", "18-24", "25-34", "35-44", "45-49", "50-55", "56+"],
      occupationList: [
        "other", "academic/educator", "artist", "clerical/admin", "college/grad student", "customer service", "doctor/health care",
        "executive/managerial", "farmer", "homemaker", "K-12 student", "lawyer", "programmer", "retired", "sales/marketing",
        "scientist", "self-employed", "technician/engineer", "tradesman/craftsman", "unemployed", "writer"
      ],
    }),
    methods: {
      editUser() {
        this.check(this.idx)
      },
      ...mapActions("user", ["editUserInfo"]),
      async editInfo() {
        const params = {
          "name": this.username,
          "token": this.getToken,
          "username": this.getUsername,
          "changeInfo": {
            "age": this.checkAge,
            "gender": this.checkGender,
            "occupation": this.checkOccupation,
            "is_staff": this.checkIsStaff
          }
        };
        await this.editUserInfo(params);
        // console.log(this.getEdit);
        if (this.getEdit === "유저 정보가 변경되었습니다.") {
          const data = {
            "age": this.checkAge,
            "gender": this.checkGender,
            "occupation": this.occupationList[this.checkOccupation],
            "is_staff": this.checkIsStaff
          }
          this.edited(this.idx, data);
          this.editUser();
        } else if (this.getEdit === "token") {
          this.logout({"username": sessionStorage.getItem("adminName")})
        }
      },
      ...mapActions("user", ["logout"]),
      ...mapActions('user', ['getUserList']),
      ...mapActions("user", ["deleteUser"]),
      async delUser() {
        const params = {
          "name": this.username,
          "token": this.getToken,
          "username": this.getUsername
        };
        await this.deleteUser(params);
        // console.log(this.getDel);
        if (this.getDel === "유저가 삭제되었습니다.") {
          this.getUserList();
        } else if (this.getDel === "token") {
          this.logout({"username": sessionStorage.getItem("adminName")})
        }
      }
    }
  }
</script>

<style scoped lang="scss">
  .data-info-bar {
    border-radius: 5px;
    height: auto;
    min-height: 5vh;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 1px 1px 3px;
    padding: {
      top: 10px;
      bottom: 10px;
    }

    .data-info {
      padding: 0 1vw;
      font-family: 'Lato', sans-serif;
      color: #535353;
      height: 23px;
    }

    .data-controller {
      display: flex;
      justify-content: space-between;
      padding: 0 1vw;
      color: #535353;
      .fa-edit:hover {
        color: #41B883;
      }
      .fa-trash-alt:hover {
        color: #FE1A1A;
      }
      i {
        margin: {
          left: 3px;
          right: 3px;
        }
      }
    }
  }
  .data-edit {
    display: flex;
    justify-content: space-between;
    padding-left: 14px;
    width: 100%;
    overflow: hidden;
  }
  .gender, .isStaff {
    margin-left: 15px;
    input {
      margin-left: 10px;
      margin-right: 15px;
    }
  }
  .age, .occupation {
    margin-left: 15px;

    select {
      border-bottom: rgba(255, 183, 0, 1.0) 2px solid;
      outline: none;
    }
  }
  .fa-check:hover {
    color: rgba(0, 76, 255, 0.96);
  }
</style>
