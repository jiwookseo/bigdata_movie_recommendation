<template>
  <div class="search--wrapper">
    <div class="search--input-div">
      <input 
        type="text" 
        placeholder="영화 제목을 입력하세요."
        v-model="input_text" 
        @input="handleClick"
      />
    </div>
    <div class="search--movie-wrapper">
      <div 
        class="search--movie-item"
        v-for="movie in searchMovieList" 
        :key="movie.title">
        <router-link :to="{name: 'detail', params: { id: movie.id } }">
          <img :src=" movie.poster || movie.still_cut || 'data:image/jpeg;base64,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' "/>
          <p>{{ movie.title }}</p>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../../api"
export default {
  name: "Search",
  data: () => ({
    input_text: "",
    movieList: []
  }),
  methods: {
    async handleClick(){
      if (this.input_text.length >= 3){
        // console.log(this.input_text)
        const data = await api.searchMovies({regex: this.input_text})
        this.movieList = data.data.data
      } else {
        this.movieList = []
      }
    }
  },
  computed: {
    searchMovieList(){
      return this.movieList
    }
  }
}
</script>

<style lang="scss" scoped>
.search--wrapper {
  padding-top: 64px;
  max-width: 100vw;
  min-height: 100vh;
  background-color: rgb(11, 11, 11);

  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}

.search--input-div {
  margin-top: 20vh;
  width: 60%;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  span {
    position: absolute;
    right: 20%;
    color: #757575;
    cursor: pointer;
  }
  input {
    width: 100%;
    box-sizing: border-box;
    border-bottom: 4px solid #CE9003;
    padding-bottom: 10px;
    color: white;
    font-size: 24px;
    &:focus {
      outline: none;
      &::placeholder {
        margin-bottom: 15px;
      }
    }
  }
}

.search--movie-wrapper {
  margin-top: 10vh;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  color: white;
  width: 100vw;
}

.search--movie-item {
  width: 17vw;
  height: 40vh;
  a {
    padding-top: 10px;
    text-decoration: none;
    color: white;
    font-size: 18px;
    cursor: pointer;
  }
  img {
    object-fit: cover;
    width: 100%;
    height: 100%;
  }
  p {
    text-align: center;
    font-family: 'Jua'
  }
}
</style>