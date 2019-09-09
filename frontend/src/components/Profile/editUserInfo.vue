<template>
    <div class="edit-user-div">
        <div class="edit_title_div">
            <button class="back_button">
                <i aria-hidden="true" class="v-icon mdi mdi-arrow-left hb-color" @click="backTo"/>
            </button>
            <p class="edit_title">Register</p>
        </div>
        <div class="edit_form">
            <div class="gender mt-30">
                <p class="gender_title">gender</p>
                <label for="gender_F">Female</label>
                <input id="gender_F" v-model="user_gender" value="F" type="radio" required>
                <label for="gender_M">Male</label>
                <input id="gender_M" v-model="user_gender" value="M" type="radio" required>
            </div>
            <span>{{ err_gender }}</span>
            <div class="age mt-30">
                <label for="age">age</label>
                <select id="age" v-model="user_age" required>
                    <option v-for="(age, i) of ageList" :key="age + i" :value="i">{{ age }}</option>
                </select>
            </div>
            <span>{{ err_age }}</span>
            <div class="occupation mt-30">
                <label for="occupation">occupation</label>
                <select id="occupation" v-model="user_occupation" required>
                    <option v-for="(occupation, i) of occupationList" :key="occupation + i" :value="i">{{ occupation
                        }}
                    </option>
                </select>
            </div>
            <span>{{ err_occupation }}</span>
        </div>
        <span>{{ err_edit }}</span>
        <div class="buttons">
            <button v-if="checkEdit" class="edit_button" @click="editInfo">Edit Info</button>
            <button v-else class="disabled_button" disabled>Register</button>
        </div>
    </div>
</template>
​
<script>
import {mapGetters, mapState, mapActions} from "vuex";

export default {
    name: "editUserInfo",
    props: {
        user: {
            type: Object
        },
        back: {
            type: Function,
            default: () => {
            }
        }
    },
    watch: {
        user_age: function () {
            this.chkAge();
        },
        user_gender: function () {
            this.chkGender();
        },
        user_occupation: function () {
            this.chkOccupation();
        }
    },
    computed: {
        ...mapGetters('data', ['token', 'username']),
        ...mapState({
            getEdit: state => state.data.editCom,
            getBool: state => state.data.edit,
        }),
    },
    mounted() {
        this.user_gender = this.user.gender;
        this.user_age = this.user.age;
        this.user_occupation = this.occupationList.indexOf(this.user.occupation);
    },
    data: () => ({
        user_gender: "",
        user_age: 0,
        user_occupation: 0,
        err_gender: "",
        err_age: "",
        err_occupation: "",
        err_edit: "",
        ageList: ["Under 18", "18-24", "25-34", "35-44", "45-49", "50-55", "56+"],
        ages: ["1", "18", "25", "35", "45", "50", "56"],
        occupationList: [
            "other", "academic/educator", "artist", "clerical/admin", "college/grad student", "customer service", "doctor/health care",
            "executive/managerial", "farmer", "homemaker", "K-12 student", "lawyer", "programmer", "retired", "sales/marketing",
            "scientist", "self-employed", "technician/engineer", "tradesman/craftsman", "unemployed", "writer"
        ],
        checkEdit: false,
    }),
    methods: {
        ...mapActions('data', ['editUserInfo']),
        backTo() {
            this.back();
        },
        chkAge() {
            if (typeof (this.user_age) === "number" && this.ages[this.user_age] !== undefined) {
                this.err_age = "";
            } else {
                this.err_age = "age를 선택해주세요.";
            }
            this.chkEdit();
        },
        chkGender() {
            if (this.user_gender === "M" || this.user_gender === "F") {
                this.err_gender = "";
            } else {
                this.err_gender = "gender를 선택해주세요.";
            }
            this.chkEdit();
        },
        chkOccupation() {
            if (typeof (this.user_occupation) === "number" && this.occupationList[this.user_occupation] !== undefined) {
                this.err_occupation = "";
            } else {
                this.err_occupation = "occupation을 선택해주세요.";
            }
            this.chkEdit();
        },
        chkEdit() {
            if (this.ages[this.user_age] !== undefined && this.user_gender && this.occupationList[this.user_occupation] !== undefined && !this.err_age && !this.err_gender && !this.err_occupation) {
                this.checkEdit = true;
            } else {
                this.checkEdit = false;
            }
        },
    async editInfo() {
    const params = {
        "token": this.token,
        "username": this.username,
        "changeInfo": {
            "age": this.ages[this.user_age],
            "gender": this.user_gender,
            "occupation": this.occupationList[this.occupation]
        }
    };
    await this.editUserInfo(params);
    const s = this.getBool;
    if (s === true) {
        this.backTo();
    } else {
        this.err_edit = this.getEdit;
    }
}
}
}
</script>

<style lang="scss" scoped>
    option {
        background-color: black;
        border: transparent;
    }

    .edit-user-div {
        margin-top: 50px;
        flex-direction: column !important;
    }

    .edit--input {
        position: relative;
        z-index: 2;
        top: 20px;
        border-bottom: rgb(194, 194, 194) 1.5px solid;
        min-height: 16px;
        max-height: 16px;

        & + label {
            transition: all .5s ease;
            position: relative;
            top: 0px;
            z-index: 1;
            white-space: nowrap;
            color: rgba(255, 221, 0, 0.98);
            font-size: 16px;
            min-height: 16px;
            max-height: 16px;
            user: {
                select: none;
            }
        }

        &:focus + label {
            top: -20px;
            font-size: 12px;
            text-align: left;
            min-height: 16px;
            max-height: 16px;
            user-select: none;
            color: rgb(194, 194, 194);
        }

        &:valid + label {
            top: -20px;
            font-size: 12px;
            text-align: left;
        }

        &:focus {
            border-bottom: rgba(255, 183, 0, 1.0) 2px solid;
            transition: all .5s ease;
            outline: none;
            min-height: 16px;
            max-height: 16px;
        }
    }

    label + span {
        margin-top: 10px;
        color: red;
        font-size: 12px;
        user-select: none;
    }

    .mt-30 {
        margin-top: 30px;
    }

    ;
    .edit_title {
        text-align: center;
        margin: 0;
        font: {
            family: Consolas;
            size: 24px;
            weight: bold;
        }
        color: rgba(255, 183, 0, 1.0);
    }

    .edit_button {
        background-color: rgba(255, 183, 0, 1.0);
        font: {
            family: Consolas;
            size: 24px;
            weight: bold;
        }
        color: rgb(255, 255, 255);
        padding: 5px 10px 10px 10px;
        line-height: 1.2em;
        border-radius: 15px;
        margin-bottom: 30px;
        outline: none;
    }

    .disabled_button {
        background-color: rgba(117, 117, 117, 0.4);
        font: {
            family: Consolas;
            size: 24px;
            weight: bold;
        };
        padding: 5px 10px 10px 10px;
        line-height: 1.2em;
        border-radius: 15px;
        margin-bottom: 30px;
    }

    .edit_form {
        margin: 30px 0;
        display: flex;
        flex-direction: column;
    }


    .age, .gender {
        display: flex;
        justify-content: space-between;
        color: rgba(255, 221, 0, 0.98);
    }

    #age {
        width: 100%;
        margin-left: 10px;
        border-bottom: rgb(194, 194, 194) 1.5px solid;
        outline: none;
    }

    .occupation {
        display: flex;
        justify-content: space-between;
        color: rgba(255, 221, 0, 0.98);
    }

    #occupation {
        width: 100%;
        margin-left: 10px;
        border-bottom: rgb(194, 194, 194) 1.5px solid;
        outline: none;
    }

    .back_button {
        position: absolute;
        margin-right: 100%;
        background-color: rgba(255, 247, 142, 0.56);
        border-radius: 15px;
        width: 30px;
        height: 30px;
    }

    .buttons {
        margin: 0 auto;
    }

</style>
