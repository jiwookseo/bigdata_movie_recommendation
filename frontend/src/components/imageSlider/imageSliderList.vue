<template>
  <div 
    class="image-slider__box"
    :style="{ transform: 'translateX(' + slideNum*16 +'vw)' }"
  >
    <ImageItem
      v-for="movie in movieList"
      :key="movie.id"
      :id="movie.id"
      :title="movie.title"
      :img="movie.img"
      :description="movie.description"
    />
    <div 
      v-if="slideNum>0"
      class="image-slider__arrow-left"
      @click="handleClick(1)"
      :style="{ left: 'calc('-30 + slideNum*16+'vw)' }"
    >
      <span>&#60;</span>
    </div>
    <div 
      v-if="slideNum<10"
      class="image-slider__arrow-right"
      @click="handleClick(-1)"
      :style="{ right: 'calc(0px'+ slideNum*16+'vw)' }"
    >
      <span>&#62;</span>
    </div>
  </div>
</template>

<script>
import ImageItem from './imageItem'
export default {
  name: "ImageSliderList",
  components: {
    ImageItem
  },
  methods: {
    handleClick: function (n){
      const s = this.slideNum + n
      this.slideNum = s
    }
  },
  data(){
    return {
      slideNum: 0,
      movieList: [
        {
          id: 1,
          title: "분노의 질주8: 더익스트림",
          img: "https://i.ytimg.com/vi/Qe486AfK3JE/maxresdefault.jpg",
          description: "겨레의 늠름한 아들로 태어나 조국을 지키는 보람찬 길에서 우리는 젊음을 함께 사르며 깨끗이 피고 질 무궁화 꽃이다",
        },
        {
          id: 2,
          title: "매드맥스",
          img: "http://writting.co.kr/wp/wp-content/uploads/2015/06/10915079_626643490774509_8086276782217440593_o.jpg",
          description: "겨레의 늠름한 아들로 태어나 조국을 지키는 보람찬 길에서 우리는 젊음을 함께 사르며 깨끗이 피고 질 무궁화 꽃이다",
        },
        {
          id: 3,
          title: "대부",
          img: "http://writting.co.kr/wp/wp-content/uploads/2015/06/10915079_626643490774509_8086276782217440593_o.jpg",
          description: "겨레의 늠름한 아들로 태어나 조국을 지키는 보람찬 길에서 우리는 젊음을 함께 사르며 깨끗이 피고 질 무궁화 꽃이다",
        },
        {
          id: 4,
          title: "영웅본색",
          img: "https://i.ytimg.com/vi/QWxZdjICrtc/maxresdefault.jpg",
          description: "겨레의 늠름한 아들로 태어나 조국을 지키는 보람찬 길에서 우리는 젊음을 함께 사르며 깨끗이 피고 질 무궁화 꽃이다",
        },
        {
          id: 5,
          title: "무간도",
          img: "data:image/jpeg;base64,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",
          description: "겨레의 늠름한 아들로 태어나 조국을 지키는 보람찬 길에서 우리는 젊음을 함께 사르며 깨끗이 피고 질 무궁화 꽃이다",
        },
        {
          id: 6,
          title: "신세계",
          img: "https://i.ytimg.com/vi/DxvZhKAz1NQ/maxresdefault.jpg",
          description: "겨레의 늠름한 아들로 태어나 조국을 지키는 보람찬 길에서 우리는 젊음을 함께 사르며 깨끗이 피고 질 무궁화 꽃이다",
        },
        {
          id: 7,
          title: "겨울왕국",
          img: "https://t1.daumcdn.net/cfile/tistory/99A73D3359F980EA27",
          description: "겨레의 늠름한 아들로 태어나 조국을 지키는 보람찬 길에서 우리는 젊음을 함께 사르며 깨끗이 피고 질 무궁화 꽃이다",
        },
        {
          id: 8,
          title: "마녀",
          img: "https://i.ytimg.com/vi/1D4HUv7SsZo/maxresdefault.jpg",
          description: "겨레의 늠름한 아들로 태어나 조국을 지키는 보람찬 길에서 우리는 젊음을 함께 사르며 깨끗이 피고 질 무궁화 꽃이다",
        },
        {
          id: 9,
          title: "센과 치히로의 행방불명",
          img: "https://i.ytimg.com/vi/t03OjGSWj5M/maxresdefault.jpg",
          description: "겨레의 늠름한 아들로 태어나 조국을 지키는 보람찬 길에서 우리는 젊음을 함께 사르며 깨끗이 피고 질 무궁화 꽃이다",
        },
        {
          id: 10,
          title: "라라랜드",
          img: "https://i.ytimg.com/vi/P0lUx_CDVgE/maxresdefault.jpg",
          description: "겨레의 늠름한 아들로 태어나 조국을 지키는 보람찬 길에서 우리는 젊음을 함께 사르며 깨끗이 피고 질 무궁화 꽃이다",
        }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
.image-slider__box {
  width: 80vw;
  margin-left: 30px;
  display: flex;
  align-items: center;
  & .image-item--box {
    min-width: 16vw;
  }
  div + div {
    margin-left: 2vw;
  }
}

.image-slider__arrow-left {
  position: absolute;
  left: -33px;
  width: 30px;
  height: 80px;
  display: flex;
  align-items: center;
  span {
    font-size: 40px;
    font-weight: 700;
    color: #aaa;
    cursor: pointer;
  }
}

.image-slider__arrow-right {
  position: absolute;
  right: 0;
  width: 30px;
  height: 80px;
  display: flex;
  align-items: center;
  span {
    font-size: 40px;
    font-weight: 700;
    color: #aaa;
    cursor: pointer;
  }
}
</style>