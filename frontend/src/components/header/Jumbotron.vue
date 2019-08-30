<template>
  <div class="jumbotron">
    <div 
      class="jumbotron__box-locator"
      ref="jumbotronSlider"
      :style="{ transform: 'translateX(' + slideNum*100 +'vw)' }"
      >
      <div 
        class="jumbotron-box--movie"
        v-for="movie in movies"
        :key="movie.id"
      >
        <div class="jumbotron__box-img">
          <img :src="movie.img">
        </div>
        <div class="jumbotron__box-wrapper">
          <div class="jumbotron__box-title">
            <h2 
              class="jumbotron__text-title"
            >
              {{ movie.title}}
            </h2>
          </div>
          <div class="jumbotron__box-score">
            <div class="jumbotron__box__score-text"><span>평점</span></div>
            <div class="jumbotron__box__score-number"><span>{{ movie.score }}</span></div>
          </div>
          <div class="jumbotron__box-description">
            <p>{{ movie.description }}</p>
          </div>
          <div class="jumbotron__box-detail-info">
            <div class="jumbotron-detail-info--genre">
              <span>개요</span>
              <span 
                v-for="(name,idx) in movie.genre"
                :key="movie.id+idx"
              >
              {{ name }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div 
        class="arrow arrow-left"
        @click="handleClick(1)"
      ><span>&#60;</span></div>
      <div 
        class="arrow arrow-right"
        @click="handleClick(-1)"><span>&#62;</span></div>
  </div>
</template>

<script>
export default {
  name: 'Jumbotron',
  methods: {
    handleClick: function (n){
      const s = this.slideNum + n
      if (s <= -2){
        this.slideNum = 0
      } else if (s > 0){
        this.slideNum = -1
      } else {
        this.slideNum = s
      }
    },
  },
  data(){
    return {
      slideNum: 0,
      movies: [
        {
          id: 0,
          title: '주먹왕 랄프 2',
          score: 3.3,
          description: "겨레의 늠름한 아들로 태어나 조국을 지키는 보람찬 길에서 우리는 젊음을 함께 사르며 깨끗이 피고 질 무궁화 꽃이다",
          img: "https://i.ytimg.com/vi/cjOAKfu0eTA/maxresdefault.jpg",
          genre: ["액션", "공포", "스릴러"]
        },
        {
          id: 1,
          title: '주먹왕 랄프 2',
          score: 3.9,
          description: "그래 그리 쉽지는 않겠지 나를 허락해준 세상이란 손쉽게 다가오는 편하고도 감미로운 공간은 아냐 그래도 날아 오를거야",
          img: "data:image/jpeg;base64,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",
          genre: ["액션", "공포", "스릴러"]
        }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
.jumbotron {
  top: 0;
  width: 100vw;
  height: calc(100vh - 64px);
}

.jumbotron__box-locator {
  position: absolute;
  margin-top: -64px;
  min-width: 100vw;
  overflow-x: hidden;
  height: 100vh;
  display: flex;
  transition: all 0.4s ease-in;
  z-index: -1;
}

.jumbotron-box--movie {
  width: 100vw;
  position: relative;
}

.jumbotron__box-img {
  z-index: -1;
  width: 100%;
  height: 100%;
  background-color: #333;
  overflow-y: hidden;
  img {
    width: 100%;
    height: 100%;
    object-fit:cover;
    filter: opacity(70%);
  }
}

.jumbotron__box-wrapper {
  position: absolute;

  padding-left: 200px;
  padding-top: 200px;
  top: 0;
  height: 100%;
  width: 100vw;
  
  display: flex;
  flex-direction: column;
}

.jumbotron__box-title {
  display: flex;
  margin-bottom: 50px;
}

.jumbotron__text-title {
  font-size: 48px;
  font-weight: 700;
  color: #fff;
  letter-spacing: 5px;
}

.jumbotron__box-score {
  display: flex;
  width: 250px;
  height: 60px;

  margin-bottom: 50px;

  div {
    width: 50%;
    font-size: 28px;
    font-weight: 700;
    box-sizing: border-box;
    display: flex;
    justify-content: cneter;
    align-items: center;
    
    &:first-child {
      background-color: #111;
      color: #fff;
      border: 2px solid #fff;
    }
    &:nth-child(2) {
      background-color: #fff;
      color: #111;
    }
    span {
      text-align: center;
      width: 100%;
    }
  }
}

.jumbotron__box-description {
  width: 40%;
  p {
    color: #fff;
    font-size: 24px;
    font-weight: 600;
    line-height: 1.6;
  }
}

.jumbotron-detail-info--genre {
  padding-top: 20px;
  font-size: 18px;
  font-weight: 500;
  span {
    color: #aaa;
    &:first-child {
      margin-right: 20px;
      font-weight: 700;
    }
  }
}

.arrow {
  position: absolute;
  top: 0;
  margin-top: calc(50vh - 30px);
  width: 60px;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  span {
    font-size: 70px;
    font-weight: 700;
    color: white;
    cursor: pointer;
  }
}

.arrow-left {
  left: 0;
}
.arrow-right {
  right: 20px;
}
</style>