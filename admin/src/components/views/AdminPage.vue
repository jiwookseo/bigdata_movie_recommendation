<template>
  <div class="content-container">
    <div class="data-controller-container">
      <!-- Search Form -->
      <search-form :submit="searchMovies" />

      <!-- Clustering -->
      <clustering-form :data="data" />
    </div>

    <div class="data-list-container">
      <div class="data-list-header">
        <div class="list-header-table" :class="[ data === 'movie'? 'selected' : '' ]" @click="selectTable">Movie</div>
        <div class="list-header-table" :class="[ data === 'user'? 'selected' : '' ]" @click="selectTable">User</div>
      </div>
      <div class="data-list-content">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import SearchForm from '../module/SearchForm'
import ClusteringForm from '../module/ClusteringForm'

export default {
  components: {
    SearchForm,
    ClusteringForm
  },
  data() {
    return {
      data: 'movie',
    }
  },
  methods: {
    ...mapActions('movie', ['searchMovies', 'clusteringMovies']),
    ...mapActions('user', ['clusteringUsers', 'getRelatedUsers']),
    selectTable(e) {
      const keyword = e.target.innerHTML.toLowerCase();
      this.data = keyword
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
  }
}
</script>

<style scoped lang="scss">

.content-container {
  padding: 30px;
}

.clustering_button {
  height: 40px !important;
}

.data-controller-container {
  display: flex;
  height: 10vh;
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
  box-shadow: 1px -1px 3px gray;
  &:hover {
    background-color: #1867C0;
    color: white;
  }
}
</style>