<template>
  <div class="sign_modal">
    <div class="sign_contents">
      <div class="sign">
        <div class="signin_div">
          <p class="signin_title">Member Login</p>
          <div class="signin">
            <input type="text" id="insert_id" v-model="insertId" required>
            <label for="insert_id" class="label_id">User Name</label>
            <input type="password" id="insert_pw" class="insert_pw" v-model="insertPw" required>
            <label for="insert_pw" class="label_pw">Password</label>
          </div>
          <button class="signin_button">Login</button>
          <div class="pw_reg">
            <button class="password">Forget password?</button>
            <button class="register">Register</button>
          </div>
        </div>
      </div>
      <div class="sign_image"></div>
    </div>
  </div>
</template>

<script>

export default {
  name: "Sign",
  data: () => ({
    insertId: "",
    insertPw: "",
  })
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
  background-color: rgba(0, 0, 0, 0.5);
  justify-content: center;
  align-items: center;
}

.sign_contents {
  background-color: rgb(255, 255, 255);
  width: 70%;
  height: 60%;
  display: flex;
}

.sign {
  margin-top: auto;
  margin-bottom: auto;
}

.signin_div {
  min-width: 380px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.sign_image {
  overflow: hidden;
  width: 100%;
  height: 100%;
  background-image: url("../../../public/modalImg.jpg");
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
}

#insert_id {
  position: relative;
  z-index: 2;
  top: 20px;
  border-bottom: rgba(117, 117, 117, 0.68) 1.5px solid;
  min-height: 16px;
  max-height: 16px;
}

#insert_id ~ .label_id {
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

#insert_id:focus ~ .label_id {
  top: -20px;
  font-size: 12px;
  text-align: left;
  min-height: 16px;
  max-height: 16px;
}

#insert_id:valid ~ .label_id {
  top: -20px;
  font-size: 12px;
  text-align: left;
}

#insert_id:focus {
  border-bottom: rgba(255, 183, 0, 1.0) 2px solid;
  transition: all .5s ease;
  outline: none;
  min-height: 16px;
  max-height: 16px;
}

.insert_pw {
  margin-top: 30px;
}

#insert_pw {
  position: relative;
  z-index: 2;
  top: 20px;
  border-bottom: rgba(117, 117, 117, 0.68) 1.5px solid;
  min-height: 16px;
  max-height: 16px;
}

#insert_pw ~ .label_pw {
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

#insert_pw:focus ~ .label_pw {
  top: -20px;
  font-size: 12px;
  text-align: left;
  min-height: 16px;
  max-height: 16px;
}

#insert_pw:valid ~ .label_pw {
  top: -20px;
  font-size: 12px;
  text-align: left;
}

#insert_pw:focus {
  border-bottom: rgba(255, 183, 0, 1.0) 2px solid;
  transition: all .5s ease;
  outline: none;
  min-height: 16px;
  max-height: 16px;
}

@media screen and (max-width: 600px) {
  .sign_image {
    display: none;
  }
  .sign_contents {
    width: 380px;
  }
}

.signin_title {
  margin: 0;
  font-size: 24px;
  font-weight: bold;
  color: rgba(255, 183, 0, 1.0);
}

.signin {
  width: 70%;
  margin-top: 30px;
  margin-bottom: 30px;
  display: flex;
  flex-direction: column;
}

.signin_button {
  background-color: rgba(255, 183, 0, 1.0);
  font-size: 25px;
  font-weight: bold;
  color: rgb(255, 255, 255);
  padding: 5px 10px 10px 10px;
  line-height: 1.2em;
  border-radius: 15px;
  margin-bottom: 30px;
}

.pw_reg {
  display: flex;
  flex-direction: column;
}

.password, .register {
  color: rgba(255, 183, 0, 1.0);
  font-size: 20px;
  text-align: center;
  margin-top: 20px;
}

</style>