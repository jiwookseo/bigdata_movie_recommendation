<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs8>
        <div class="display-2 pa-10">유저 검색</div>
        <UserSearchForm :submit="get_usersKey" />
      </v-flex>
      <!-- 검색 결과 -->
      <v-flex xs8>
        <UserList :user-list-cards="userList" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import UserSearchForm from "../UserSearchForm";
import UserList from "../UserList";

export default {
  components: {
    UserList,
    UserSearchForm
  },
  data: () => ({}),
  computed: {
    ...mapState({
    userList: state => state.data.userSearchList
    })
  },
  methods: {
    ...mapActions("data", ["get_usersKey"]),
  }
};
</script>

<style>

</style>