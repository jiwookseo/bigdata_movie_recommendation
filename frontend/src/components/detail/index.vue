<template>
  <div class="detail">
    <div class="detail--img">
      <img :src="imgUrl" />
    </div>
    <div class="detail--info">
      <h1>{{movie.title}}</h1>
      <p class="detail--info-genre">
        <span>장르</span>
        <span v-for="genre in movie.genres" :key="genre + movie.id">
          {{genre}}
        </span>
      </p>
      <p class="detail--info-rating">
        <span>평가자수</span> 
        <span>{{ movie.viewCnt }}</span>
      </p>
      <p class="detail--info-score">
        <span>평균 평점</span>
        <span>{{ movie.rating }}</span>
      </p>
    </div>
    <div class="detail--story">
      <span>줄거리</span>
      <div class="detail--story-text">
        <p>{{ movie.story }}</p>
      </div>
    </div>
    <div class="detail--user">
      <p class="detail--user-title">
        이 영화를 본 사용자
      </p>
      <div class="detail--user-list">
        <div class="detail--user-a" v-for="person in audience" :key="person.username">
          <div class="detail--user-a-img">
          이미지
          </div>
          <div class="detail--user-info">
            <router-link :to="{name: 'profile', params: { username: person.username } }">
              {{person.username}}
            </router-link>
          </div>
        </div>
      </div>
      <div class="detail--related-movie">
        <ImageSlider />
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import ImageSlider from '../imageSlider'
export default {
  name: "Detail",
  components: { ImageSlider },
  computed: {
    ...mapGetters("movie", ["movie"]),
    imgUrl(){
      const detailMovie = this.$store.getters["movie/movie"]
      return detailMovie.stillCut || detailMovie.poster || "https://files.slack.com/files-pri/TMJ2GPC23-FMF2L2DQA/599637c326f7d273826d.jpg"
    },
    audience(){
      return this.$store.getters["movie/audience"].slice(0, 10)
    }
  },
  watch: {
    "$route.params.id": function(id){
      console.log("시계는 왓치")
      this.$store.dispatch("movie/getMovieById", id)
    }
  },
  created() {
    this.$store.commit("mvUi/setSliderType", "profile");
  },
  mounted(){
    this.$store.dispatch("movie/getMovieById", this.$route.params.id)
  }
  
}
</script>
<style lang="scss" scoped>
.detail {
  display: relative;
  color: #333;
  min-height: calc( 100vh - 64px );
}

.detail--img {
  margin-top: -64px;
  height: 100vh;
  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
  }
}

.detail--info {
  position: absolute;
  top: 40vh;
  left: 6vw;

  width: 40vw;
  height: 40vh;

  padding-top: 20px;
  padding-left: 20px;

  background-color: rgba(11, 11, 11, 0.8);

  p {
    display: flex;
    align-items: center;
    padding: 10px 0;
    font-size: 24px;
    font-weight: 550;
    span{
      &:first-child {
        margin-right: 20px;
        color: rgb(255, 177, 1);
      }
    }
  }
  h1, p {
    color: #fff;
  }
  h1 {
    font-family: ubuntu;
    font-size: 36px;
    font-weight: 700;
  }
  h1 + p {
    margin-top: 30px;
  }
  p + p {
    margin-top: 20px;
  }
}

.detail--story {
  width: 70%;
  padding: 40px 20px;
  margin: 0 auto;
  span {
    font-size: 30px;
    font-weight: 700;
  }
}

.detail--story-text {
  margin-top: 30px;  
  p{
    font-family: ubuntu;
    font-size: 20px;
    letter-spacing: 1.2px;
    line-height: 1.4;
  }
}

.detail--user {
  display: flex;
  flex-direction: column;

  background-color: #111;
  color: #fff;
  font-weight: 700;
}

.detail--user-title {
  padding: 40px 30px;
  color: #fff;
  font-size: 36px;
  font-weight: 500;
  font-family: 'Jua';
}

.detail--user-list {
  display: flex;
  width: 250vw;
  overflow-x: hidden;
}

.detail--user-a {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;

  width: 25vh;
  height: 25vh;
  margin-bottom: 100px;

  border-radius: 15%;
  background-color: #fff;
  color: #111;

  & + & {
    margin-left: 50px;
  }
}

.detail--user-a-img {
  width: 80%;
  height: 50%;
  background-color: green;
  color: #111;
}

.detail--user-info {
  a {
    text-decoration: none;
    color: #111;
  }
}

.detail--related-movie {
  height: 40vw;
  background-color: orange;
}
</style>
