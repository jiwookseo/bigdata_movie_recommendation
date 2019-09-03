<template>
  <div class="content-container">
    <div class="data-controller-container">
      <search-form :submit="searchMovies" />
      <v-btn @click="clustering">clustering</v-btn>
    </div>
   
    <div class="data-list-container">
      <div class="data-list-header">
        <div class="list-header-table" :class="{ 'selected': !directory }" @click="selectTable">Movie</div>
        <div class="list-header-table" :class="{ 'selected': directory }" @click="selectTable">User</div>
      </div>
      <div class="data-list-content">
        <router-view />
      </div>
    </div> 
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import SearchForm from '../common/SearchForm'

export default {
  components: {
    SearchForm,
  },
  data() {
    return {
      directory: true
    }
  },
  methods: {
    ...mapActions('movie', ['searchMovies', 'clusteringMovies']),
    ...mapActions('user', ['clusteringUsers', 'getRelatedUsers']),
    selectTable(e) {
      const keyword = e.target.innerHTML.toLowerCase();
      this.directory = !this.directory
      this.$router.push({
        name: `${keyword}-list`
      })
    },
    clustering() {
      const params = {
        method: 'em',
        k: 5
      }
      if (this.$route.path === '/admin/movies') {
        this.clusteringMovies(params)
      } else {
        this.clusteringUsers(params)
      }
    },
    test() {
      const params = {
        userId: 1
      }
      this.getRelatedUsers(params);
    } 
  }
}
</script>

<style scoped lang="scss">

.data-controller-container {
  display: flex;
  height: 15vh;
  padding-bottom: 2vh;
}


.data-list-header {
  display: flex;
  height: 10vh;
  justify-content: left;
  align-items: flex-end;
}

.list-header-table {
  width: 15vw;
  margin: 0 0 0 2vw;
  padding: 0 1vw;
  color: white;
  font-size: 3vh;
  text-align: center;
  border-radius: 10px 10px 0 0;
  background-color: #1867C0;
  transition: all 1s;

  &:hover {
    color: #1867C0;
    background-color: white;
  }
}

.selected {
  color: #1867C0;
  background-color: white;
  box-shadow: 1px -1px 1px gray;
  &:hover {
    background-color: #1867C0;
    color: white;
  }
}
</style>