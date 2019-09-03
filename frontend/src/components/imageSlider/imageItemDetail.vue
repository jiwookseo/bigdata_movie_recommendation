<template>
  <div class="image-item-detail">
    <div class="image-item--img-canvas" :class="classChanger">
      <img :src="movie.img" />
    </div>
    <div class="detail--content-box" :class="classChanger">
      <div class="detail--close-box">
        <span @click="handleToggle">&times;</span>
      </div>
      <h2 class="detail--title">{{ movie.title }}</h2>
      <div class="detail--score">
        <span>평균별점</span>
        <span>4.0</span>
      </div>
      <div class="detail--description" v-if="active.base">
        <p>{{ ellipsisDescription }}</p>
      </div>
      <div class="detail--info">
        <div class="detail--info-genre">
          <span>개요</span>
          <span v-for="(name, idx) in movie.genres" :key="movie.id+idx">{{ name }}</span>
        </div>
      </div>
    </div>
    <div class="detail--movie-menu">
      <span :class="{ active: active.base }" @click="handleActive('base')">기본 정보</span>
      <span :class="{ active: active.cluster }" @click="handleActive('cluster')">비슷한 작품</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "ImageItemDetail",
  data() {
    return {
      active: {
        base: true,
        cluster: false
      }
    };
  },
  computed: {
    movie: function() {
      return this.$store.state.mvUi.activateMovie;
    },
    classChanger: function() {
      return {
        base: this.active.base,
        cluster: this.active.cluster
      };
    },
    ellipsisDescription() {
      const temp = this.movie.description.split(" ");
      temp.splice(temp.length - 1, temp.length);
      return temp.join(" ") + "...";
    }
  },
  methods: {
    handleToggle: function() {
      this.$store.dispatch("mvUi/setDetailToggler");
    },
    handleActive: function(state) {
      if (state === "base") {
        this.active.base = true;
        this.active.cluster = false;
      } else {
        this.active.cluster = true;
        this.active.base = false;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.image-item-detail {
  margin-top: 30px;
  width: 100vw;
  height: 100vh;
  background-color: red;
  transition: all 0.4s ease-in-out;
}

.image-item--img-canvas {
  position: absolute;
  width: 100vw;
  height: 100vh;
  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
    &.cluster {
      filter: blur(8px);
    }
  }
}

.detail--close-box {
  position: absolute;
  display: flex;
  justify-content: flex-end;
  width: 100vw;
  padding-right: 40px;

  span {
    color: #fff;
    font-size: 36px;
    font-weight: 700;
    cursor: pointer;
  }
}

.detail--content-box {
  position: relative;
  display: flex;
  flex-direction: column;

  width: 30vw;

  height: 100vh;

  background-color: rgba(33, 33, 33, 0.6);

  &.cluster {
    width: 100vw;
  }

  h2 {
    color: #fff;
    font-weight: 700;
    font-size: 36px;
  }
}

.detail--title {
  padding: 30px 0 0 40px;
}

.detail--score {
  padding-top: 30px;
  padding-left: 40px;

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
  padding: 30px 20px 0 40px;
  p {
    font-size: 18px;
    color: #ddd;
    font-weight: 700;
    line-height: 1.4;
  }
}

.detail--info-genre {
  margin-top: 20px;
  padding-left: 40px;
  span {
    color: #aaa;
    font-size: 18px;
    font-weight: 700;
    &:first-child {
      font-weight: 700;
      margin-right: 20px;
    }
  }
  span + span {
    margin-right: 10px;
  }
}

.detail--movie-menu {
  position: absolute;
  margin-top: -70px;
  padding-bottom: 20px;
  color: white;
  width: 100%;
  display: flex;
  justify-content: center;
  z-index: 12;

  span {
    font-size: 18px;
    color: #aaa;
    font-size: 20px;
    font-weight: 700;
    line-height: 2.5;
    margin-bottom: 10px;
    cursor: pointer;
    &:hover {
      border-bottom: 5px solid #aaa;
    }
    &.active {
      color: #fff;
      border-bottom: 5px solid #fff;
    }
  }
  span + span {
    margin-left: 50px;
  }
}
</style>