<template>
  <div>
    <div>
      this is UserList
    </div>
    <ul>
      <li v-for="user in userList">
        <user-info-bar :username="user"></user-info-bar>
      </li>
    </ul>
  </div>
</template>

<script>
import UserInfoBar from './UserInfoBar'

export default {
  data() {
    return {
      userList: ['user1', 'user2', 'user3']
    }
  },
  components: {
    UserInfoBar
  }
}
</script>

<style scoped>

</style>