<template>
  <div 
    class="image-item--box"
    :style="{'backgroundImage':'url('+img+')'}"
    @mouseenter="handleMouseOver"
    @mouseleave="handleMouseOver">
    <div class="image-item--title">
      <span>{{ title }}</span>
    </div>
    <div 
      v-if="showDescription"
    >
      <div class="image-item--description">
        <p>{{description}}</p>
      </div>
      <div class="image-item--under-expand">
        <span>아래</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ImageItem",
  props: ["id", "title", "img", "description"],
  methods: {
    handleMouseOver: function(){
      this.showDescription = !this.showDescription
    }
  },
  data(){
    return {
      showDescription: false
    }
  }
}
</script>

<style lang="scss" scoped>
.image-item--box {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  min-width: 20%;
  height: 140px;
  background-size: cover;
  cursor: pointer;
  transition: all 0.4s ease-out;
  transition-delay: 0.1s;
  &:hover {
    transform: scale(1.4);
    margin-left: 50px;
    margin-right: 50px;
  }
}

.image-item--title {
  span {
    color: #fff;
    font-weight: 500;
    font-size: 18px;
  }
}

.image-item--description {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;

  height: 55px;
  padding: 10px;
  background-color: rgba(33, 33, 33, 0.7);

  color: #ddd;
  font-weight: 400;
  font-size: 13px;
  line-height: 1.2;
}

.image-item--under-expand {
  color: #fff;
  font-size: 24px;
  font-weight: 700;
  display: flex;
  justify-content: center;
  span {
    margin: auto;
    text-align: center;
    &:hover {
      color: #F1AC1E;
    }
  }
}
</style>