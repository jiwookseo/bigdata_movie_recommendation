<template>
  <div
    class="image-item--box"
    :style="{'backgroundImage':`url('${movie.img}')`}"
    @mouseenter="handleMouseOver"
    @mouseleave="handleMouseLeave"
    @click="openDetail"
  >
    <div class="image-item--title">
      <span>{{ movie.title }}</span>
    </div>
    <div v-if="showDescription">
      <div class="image-item--description">
        <p>{{ movie.description }}</p>
      </div>
      <!-- 아래 화살표 -->
      <div v-if="expand" class="image-item--under-expand">
        <span v-show="!toggle" @click="handleToggleOpen">
          <font-awesome-icon icon="sort-down" size="2x" />
        </span>
        <span v-show="toggle" @click="handleToggleClose">
          <font-awesome-icon icon="sort-up" size="2x" />
        </span>
      </div>
    </div>
  </div>
</template>

<script>
// font-awesome
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faSortDown, faSortUp } from "@fortawesome/free-solid-svg-icons";
import { mapGetters, mapState, mapActions } from "vuex";

library.add(faSortDown, faSortUp);

export default {
  name: "ImageItem",
  components: {
    FontAwesomeIcon,
  },
  props: {
    movie: {
      type: Object,
      default: () => ({ id: 0, title: "", img: "", description: "", genre: "" })
    },
    type: { type: String, default: "Age" },
    expand: { type: Boolean, default: true },
    related: {type: String, default: ""}
  },
  data() {
    return {
      showDescription: false
    };
  },
  computed: {
    ...mapGetters("mvUi", ["detailToggler", "detailType", "activateMovie"]),
    ...mapState({
      getSubscribe: state => state.user.subscribe,
      username: state => state.user.username,
      getToken: state => state.user.token
    }),
    toggle() {
      return this.detailToggler && this.detailType === this.type;
    }
  },
  methods: {
    ...mapActions("user", ["setUserRating"]),
    handleMouseOver: function() {
      this.getRating();
      this.showDescription = !this.showDescription;
      if (this.detailType === this.type && this.activateMovie !== this.movie) {
        this.$store.commit("mvUi/setActivateMovie", this.movie);
        const data = {"movieId": this.movie.id};
        if (this.related === "profile") {
          data["username"] = this.username;
          data["token"] = this.getToken;
          data["name"] = this.$route.params.username
        }
        if (this.related === "board" || this.related === "profile") {
          this.$store.dispatch("mvUi/setRelatedMovies", data);
        }
      }
    },
    handleMouseLeave: function() {
      this.getRating();
      this.showDescription = !this.showDescription;
    },

    handleToggleOpen: function() {
      this.getRating();
      this.$store.dispatch("mvUi/setDetailToggler", this.type);
      this.$store.commit("mvUi/setActivateMovie", this.movie);
      const data = {
        "movieId": this.movie.id,
      };
      if (this.related === "profile") {
        data["username"] = this.username;
        data["token"] = this.getToken;
        data["name"] = this.$route.params.username
      }
      if (this.related === "board" || this.related === "profile") {
        this.$store.dispatch("mvUi/setRelatedMovies", data);
      }
    },
    handleToggleClose: function() {
      this.$store.dispatch("mvUi/setDetailToggler", this.type);
    },
    openDetail() {
      if (!this.expand) {
        const popup = document.getElementById(`detail${this.movie.id}`);
        popup.style.display = "flex";
      }
    },
    async getRating() {
      if (this.username) {
        const data = {
          "username": this.username,
          "movieId": this.movie.id
        };
        await this.setUserRating(data);
      }
    },
  }
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css?family=Jua|Ubuntu&display=swap");

.image-item--box {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  min-width: 20%;
  max-width: 20%;
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
    font-family: "Ubuntu", sans-serif;
  }
}

.image-item--description {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;

  max-height: 55px;
  padding: 10px;
  margin-bottom: -20px;
  background-color: rgba(33, 33, 33, 0.7);

  color: #ddd;
  font-family: "Ubuntu", sans-serif;
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
  align-items: flex-end;

  span {
    text-align: center;
    bottom: 0;
    &:hover {
      color: #f1ac1e;
    }
    &:nth-child(2) {
      padding-top: 20px;
      margin-bottom: -20px;
    }
  }
}
</style>
