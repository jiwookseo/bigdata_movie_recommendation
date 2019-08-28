<template>
  <div class="app">
    <header class="header">
      <nav class="nav txt-orange">
        <div class="nav__title">
          <span>
            HONEY BEE
          </span>
        </div>
        <div class="nav__icon-bar">
          <span>
            <font-awesome-icon icon="search" />
          </span>
          <span>
            <font-awesome-icon icon="user" />
          </span>
        </div>
      </nav>
    </header>
  </div>
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
import router from "./router";
import './reset.css';

library.add(faSearch, faUser)
export default {
  components: {
    FontAwesomeIcon,
  }
};
</script>

<style lang="scss" scoped>
  .app {
    width: 100vw;
    overflow-x: hidden;
  }

  .nav {
    height: 64px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: rgba(33, 33, 33, 0.8)
  }

  .nav__title {
    padding-left: 30px;
    font-size: 24px;
    font-weight: 700;
    cursor: pointer;
  }
  
  .nav__icon-bar {
    padding-right: 30px;
    span {
      cursor: pointer;
    }
    span + span {
      margin-left: 15px;
      margin-right: 15px;
    }
  }
</style>