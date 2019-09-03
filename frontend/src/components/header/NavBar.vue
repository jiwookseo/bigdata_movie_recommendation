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
        <font-awesome-icon icon="search" size="2x"/>
      </span>
      <span>
        <font-awesome-icon icon="user" size="2x" @click="sign"/>
      </span>
    </div>
  </nav>  
</template>

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
    }
  })
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
  }

  .nav__title {
    padding-left: 30px;
    font-size: 24px;
    font-weight: 700;
    cursor: pointer;

    a {
      text-decoration: none;
    }
  }
  
  .nav__icon-bar {
    padding-right: 30px;

    span {
      cursor: pointer;
      color: rgba(255, 177, 1, 0.7);

      &:hover {
        color: rgb(255, 177, 1);
      }
    }
    span + span {
      margin-left: 50px;
      margin-right: 30px;
    }
  }
</style>