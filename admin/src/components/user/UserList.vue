<template>
  <div class="item-list-container">

    <!-- Data List -->
    <div v-for="(user, idx) in dataList" v-if="idx+1 <= currentPage*10 && idx+1 > (currentPage-1)*10" :key="`user${user.id}`">
      <user-info-bar
              :id="user.id"
              :username="user.username"
              :gender="user.gender"
              :age="user.age"
              :occupation="user.occupation"
              :isStaff="user.isStaff"
              :idx="idx"
              :check="checkUser"
              :user="userIdx"
              :edited="edited"
      >
      </user-info-bar>
    </div>

    <!-- Page Buttons -->
    <div class="page-buttons-container">
      <div v-show="index > 1" @click="showFirstPageList" class="page-button">
        <i class="fas fa-backward"></i>
      </div>

      <div v-show="index > 1" @click="showPrevPageList" class="page-button">
        <i class="fas fa-caret-left"></i>
      </div>

      <div class="page-button"
           v-for="pageNumber in pageArray"
           :key="`page${pageNumber}`"
           v-show="pageNumber <= lastPage"
           @click="changeCurrentPage(pageNumber)"
           :class="{ 'current-page' : pageNumber === currentPage}"
      >
        {{ pageNumber }}
      </div>

      <div v-show="index + 10 <= lastIndex" @click="showNextPageList" class="page-button">
        <i class="fas fa-caret-right"></i>
      </div>

      <div v-show="index + 10 <= lastIndex" @click="showLastPageList" class="page-button">
        <i class="fas fa-forward"></i>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapState } from "vuex";
  import UserInfoBar from './UserInfoBar'
  import DataList from '../../mixin/components/DataList'

export default {
  components: {
    UserInfoBar,
  },
  data() {
    return {
      currentView: 'user',
      userIdx: -1,
    }
  },
  computed: {
    ...mapState('user', { dataList: 'userList' }),
  },
  methods: {
    checkUser(idx) {
      if (this.userIdx === idx) {
        this.userIdx = -1;
      } else {
        this.userIdx = idx;
      }
    },
    edited(idx, info) {
      this.dataList[idx]["age"] = info["age"];
      this.dataList[idx]["gender"] = info["gender"];
      this.dataList[idx]["occupation"] = info["occupation"];
      this.dataList[idx]["is_staff"] = info["is_staff"];
    }
  },
  mixins: [ DataList ]
};
</script>

<style scoped lang="scss">
  @import "@/mixin/style/_datalist";
</style>
