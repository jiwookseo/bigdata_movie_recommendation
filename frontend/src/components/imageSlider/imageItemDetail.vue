<template>
  <div class="image-item-detail">
    <div class="image-item--img-canvas">
      <img :src="movie.img" />
    </div>
    <div class="detail--close-box">
      <span @click="handleToggle">&times;</span>
    </div>
    <div class="detail--content-box">
      <h2 class="detail--title">{{ movie.title }} </h2>
      <div class="detail--score">
        <span>평균별점</span>
        <span>4.0</span>
      </div>
      <div class="detail--description">
        <p>{{ movie.description }}</p>
      </div>
      <div class="detail--info">
        <div class="detail--info-genre">
          <span> 개요 </span>
          <span
            v-for="(name, idx) in movie.genre"
            :key="movie.id+idx"
          >{{ name }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ImageItemDetail",
  methods: {
    handleToggle: function(){
      this.$emit("closeDetail")
    }
  },
  computed: {
    movie: function(){
      return this.$store.state.mvUi.activateMovie
    }
  }
}
</script>

<style lang="scss" scoped>
.image-item-detail {
  margin-top: 20px;
  width: 100vw;
  height: 100vh;
  background-color: red;
}
.image-item--img-canvas {
  width: 100vw;
  height: 100vh;
  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
  }
}


.detail--close-box {
  display: flex;
  justify-content: flex-end;
  width: 100vw;
  height: 30px;
  padding-right: 20px;
  margin-top: -100vh;
  span {
    background-color: rgba(33, 33, 33, 0.5);
    color: #fff;
    font-size: 36px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.4s ease-in;
    &:hover {
      transform: rotateY('90deg');
    }
  }
}

.detail--content-box {
  position: relative;
  
  display: flex;
  flex-direction: column;
  
  width: 40vw;
  height: 100vh;

  margin-top: -30px;
  padding: 50px;
  background-color: #333;

  h2 {
    color: #fff;
    font-weight: 700;
    font-size: 36px;
  }
}

.detail--score {
  padding-top: 30px;
  span {
    font-weight: 700;
    font-size: 18px;
    padding: 5px;

    &:first-child {
      border: 1px solid #fff;
      background-color: #111;
      color: #fff;
    }

    &:nth-child(2) {
      background-color: #fff;
      color: #111;
      border: 1px solid #fff;
    }
  }
}


.detail--description {
  padding-top: 30px;
  p {
    font-size: 18px;
    color: #ddd;
    font-weight: 700;
    line-height: 1.4;
  }
}

.detail--info-genre {
  margin-top: 20px;
  span {
    color: #aaa;
    font-size: 18px;
    font-weight: 500;
    &:first-child {
      font-weight: 700;
      margin-right: 20px;
    }
  }
  span + span {
    margin-right: 10px;
  }
}

</style>