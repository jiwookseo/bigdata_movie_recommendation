<template>
  <div class="similar-user-list">
    <h2><span>{{ username }}</span>님과 유사한 사람들</h2>
    <div class="similar-user-list-wrapper">
      <div class="similar-user-list-item" v-for="user in similarUser" :key="user.id">
        <router-link :to="{name: 'profile', params: {username: user.username}}">
        <p>
          {{ user.username }}
        </p>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'SimilarUserList',
  computed: {
    ...mapGetters('data',['username']),
    ...mapGetters('mvUi', ['similarUser'])
  }
}
</script>

<style lang="scss" scoepd>
.similar-user-list {
  width: 80%;
  margin: 30px 0 0 30px;
  height: 80px;
  display: flex;
  flex-direction: column;

  h2 {
    font-size: 30px;
    color: #fff;
    font-weight: 700;
    letter-spacing: 1.8px;
    span {
      color: rgba(255, 177, 1)
    }
  }
  p {
    color: white;
  }
}

.similar-user-list-wrapper {
  width: 90%;
  display: flex;
  padding: 20px;
}

.similar-user-list-item {
  margin-right: 40px;
  min-width: 10%;
  max-width: 10%;
  height: 100px;
  border-radius: 25%;
  background-color: blue;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}
</style>