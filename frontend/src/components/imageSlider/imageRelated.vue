<template>
  <div class="cluster--movie">
    <div class="cluster--movie-img">
      <img :src="imgUrl" />
    </div>
    <div class="cluster--movie-info">
      <div class="cluster--movie-info-basic">
      <h4>{{movie.title}}</h4>
      <p>{{movie.description}}</p>
      </div>
      <div class="cluster--movie-info-description">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ImageRelated",
  props: { movie: { type: Object, default: () => {} } },
  computed: {
    imgUrl(){
      return this.movie.still_cut||
             this.movie.poster||
             'https://files.slack.com/files-pri/TMJ2GPC23-FMF2L2DQA/599637c326f7d273826d.jpg'
    }
  }
}
</script>

<style lang="scss" scoped>
.cluster--movie {
  display: flex;
  flex-direction: column;
  max-width: 20%;
  min-width: 20%;
  height: 100%;

  & + & {
    margin-left: 25px;
  }
}

.cluster--movie-img {
  width: 100%;
  height: 100%;
  cursor: pointer;
  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
}

.cluster--movie-info-basic {
  padding: 15px 10px;
  h4 {
    padding-left: 12px;
    color: #eee;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 2px;
  }
  p {
    padding: 0 10px;
    margin-top: 10px;
    color: #999;
    font-weight: 600;
    letter-spacing: 1.6px;
  }
}

</style>