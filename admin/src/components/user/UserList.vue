<template>
  <div class="item-list-container">
    <div v-for="(user, idx) in userList" :key="user.id">
      <user-info-bar 
        :username="user.username"
        :age="user.age"
        :gender="user.gender"
        :isStaff="user.isStaff"
      >  
      </user-info-bar>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import UserInfoBar from './UserInfoBar'

export default {
  computed: {
    ...mapState('user', ['userList'])
  },
  components: {
    UserInfoBar
  }
}
</script>

<style scoped>
.item-list-container {
  padding: 3vh 2vw;
}
</style>