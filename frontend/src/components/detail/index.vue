<template>
  <div class="detail">
    <div class="detail--img">
      <img :src="imgUrl" />
    </div>
    <div class="detail--info">
      <h1>{{movie.title}}</h1>
      <p class="detail--info-genre">
        <span>장르</span>
        <span class="detail--info-genre-span" v-for="genre in movie.genres" :key="genre + movie.id">{{genre}}</span>
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
    <div v-if="recommendations.length">
      <div class="detail--recommendations">
        <p class="detail--recommendations-title">이런 분들께 추천합니다</p>
        <div v-if="recAge.length">
          <p class="detail--recommendations-subtitle">연령대</p>
          <div class="detail--recommendations-list">
            <v-chip
              v-for="recommendation in recAge"
              :key="recommendation"
              class="detail--recommendations-a"
              color="indigo"
              text-color="white"
            >
              <v-avatar left>
                <v-icon>mdi-account-circle</v-icon>
              </v-avatar>
              {{ recommendation }}
            </v-chip>
          </div>
        </div>
        <div v-if="recOccupation.length">
          <p class="detail--recommendations-subtitle">직업</p>
          <div class="detail--recommendations-list">
            <v-chip
              v-for="recommendation in recOccupation"
              :key="recommendation"
              class="detail--recommendations-a"
              color="indigo"
              text-color="white"
            >
              <v-avatar left>
                <v-icon>mdi-account-circle</v-icon>
              </v-avatar>
              {{ recommendation }}
            </v-chip>
          </div>
        </div>
        <div v-if="recGender.length">
          <p class="detail--recommendations-subtitle">성별</p>
          <div class="detail--recommendations-list">
            <v-chip
              v-for="recommendation in recGender"
              :key="recommendation"
              class="detail--recommendations-a"
              color="indigo"
              text-color="white"
            >
              <v-avatar left>
                <v-icon>mdi-account-circle</v-icon>
              </v-avatar>
              {{ recommendation }}
            </v-chip>
          </div>
        </div>
      </div>
    </div>
    <div class="detail--user">
      <p class="detail--user-title">이 영화를 본 사용자</p>
      <div class="detail--user-list">
        <div class="detail--user-a" v-for="person in audience" :key="person.username">
          <div class="detail--user-a-img">
            <img
              :src="person.user_image||'data:image/jpeg;base64,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'"
            />
          </div>
          <div class="detail--user-info">
            <router-link
              :to="{name: 'profile', params: { username: person.username } }"
            >{{person.username}}</router-link>
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
import { mapGetters } from "vuex";
import ImageSlider from "../imageSlider";
export default {
  name: "Detail",
  components: { ImageSlider },
  computed: {
    ...mapGetters("movie", ["movie", "recommendations"]),
    ...mapGetters("mvUi", { recommendationData: "sliderBoardData" }),
    imgUrl() {
      return (
        this.movie.stillCut ||
        this.movie.poster ||
        "https://files.slack.com/files-pri/TMJ2GPC23-FMF2L2DQA/599637c326f7d273826d.jpg"
      );
    },
    audience() {
      return this.$store.getters["movie/audience"].slice(0, 6);
    },
    recAge() {
      const rec = this.recommendations.filter(r => r.type === "age");
      return rec.map(r =>
        this.recommendationData[0].selectObject[r.value].slice(0, -1)
      );
    },
    recOccupation() {
      const rec = this.recommendations.filter(r => r.type === "occupation");
      return rec.map(r =>
        this.recommendationData[1].selectObject[r.value].slice(0, -1)
      );
    },
    recGender() {
      const rec = this.recommendations.filter(r => r.type === "gender");
      return rec.map(r =>
        this.recommendationData[2].selectObject[r.value].slice(0, -1)
      );
    }
  },
  watch: {
    "$route.params.id": function(id) {
      this.$store.dispatch("movie/getMovieById", id);
    }
  },
  created() {
    this.$store.commit("mvUi/setSliderType", "profile");
  },
  mounted() {
    this.$store.dispatch("movie/getMovieById", this.$route.params.id);
  },
  methods: {}
};
</script>
<style lang="scss" scoped>
.detail {
  display: relative;
  color: #333;
  min-height: calc(100vh - 64px);
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
    span {
      &:first-child {
        margin-right: 20px;
        color: rgb(255, 177, 1);
      }
    }
  }
  h1,
  p {
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

.detail--info-genre-span {
  margin-left: 15px;
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
  p {
    font-family: ubuntu;
    font-size: 20px;
    letter-spacing: 1.2px;
    line-height: 1.4;
  }
}

.detail--user,
.detail--recommendations {
  display: flex;
  flex-direction: column;

  background-color: #111;
  color: #fff;
  font-weight: 700;
}

.detail--user-title,
.detail--recommendations-title {
  padding: 40px 30px;
  color: #fff;
  font-size: 36px;
  font-weight: 500;
  font-family: "Jua";
}

.detail--user-list{
  display: flex;
  width: 250vw;
  overflow-x: hidden;
}

.detail--recommendataion-list {
  width: 100vw;
}

.detail--recommendations-subtitle {
  margin-left: 25px;
}

.detail--user-list {
  margin-left: 25px;
}
.detail--recommendations-a {
  padding: 25px 15px;
  margin: 10px 0px 30px 25px;
  font-size: 20px !important;
  font-weight: 500;
  font-family: "Jua";
}

.detail--user-a {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;

  width: 20vh;
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
  width: 100%;
  height: 60%;
  color: #111;
  img {
    height: 100%;
    width: 100%;
    object-fit: cover;
  }
}

.detail--user-info {
  margin-top: 15px;
  justify-content: center;
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
