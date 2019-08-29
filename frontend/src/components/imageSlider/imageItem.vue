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
      class="image-item--description"
      v-if="showDescription"
    >
      <p>{{description}}</p>
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
  width: 15.5vw;
  height: 140px;
  background-size: cover;
  cursor: pointer;
  transition: all 0.4s ease-out;
  transition-delay: 0.3s;
  &:hover {
    transform: scale(1.2);
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
  font-size: 14px;
  line-height: 1.6;
  letter-spacing: 1px;
  
}
</style>