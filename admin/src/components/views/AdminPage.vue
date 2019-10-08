<template>
  <div class="content-container">
    <div v-if="isLoading" class="loader-container">
      <loader />
    </div>
    <div class="data-controller-container">
      <!-- Collaborative Filtering -->
      <collaborative-filtering-form />
      <!-- Recommendations -->
      <refresh-recommendations />
      <!-- Clustering -->
      <clustering-form :data="data" />
      <!-- Search Form -->
      <!-- <search-form :submit="searchMovies" /> -->
    </div>

    <div class="data-list-container">
      <div class="data-list-header">
        <div
          class="list-header-table"
          :class="[ data === 'movie'? 'selected' : '' ]"
          @click="selectTable"
        >Movie</div>
        <div
          class="list-header-table"
          :class="[ data === 'user'? 'selected' : '' ]"
          @click="selectTable"
        >User</div>
      </div>
      <div class="data-list-content">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import SearchForm from "../module/SearchForm";
import ClusteringForm from "../module/ClusteringForm";
import RefreshRecommendations from "../module/RefreshRecommendations";
import CollaborativeFilteringForm from '../module/CollaborativeFilteringForm';
import Loader from '../module/Loader';

export default {
  components: {
    SearchForm,
    ClusteringForm,
    RefreshRecommendations,
    CollaborativeFilteringForm,
    Loader,
  },
  data() {
    return {
      data: "movie"
    };
  },
  computed: {
    ...mapState("loader", ["isLoading"]),
  },
  methods: {
    ...mapActions("movie", ["searchMovies", "clusteringMovies"]),
    ...mapActions("user", ["clusteringUsers", "getRelatedUsers"]),
    selectTable(e) {
      const keyword = e.target.innerHTML.toLowerCase();
      this.data = keyword;
      this.$router.push({
        name: `${keyword}-list`
      });
    },
    clustering() {
      const params = {
        method: "em",
        k: 5
      };
      if (this.$route.path === "/admin/movies") {
        this.clusteringMovies(params);
      } else {
        this.clusteringUsers(params);
      }
    }
  }
};
</script>

<style scoped lang="scss">
.content-container {
  padding: 30px;
}

.loader-container {
  height: 100%;
  width: 100%;
  z-index: 100;
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
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
  background-color: #1867c0;
  transition: all 1s;

  &:hover {
    color: #1867c0;
    background-color: white;
  }
}

.selected {
  color: #1867c0;
  background-color: white;
  box-shadow: 1px -1px 3px gray;
  &:hover {
    background-color: #1867c0;
    color: white;
  }
}
</style>