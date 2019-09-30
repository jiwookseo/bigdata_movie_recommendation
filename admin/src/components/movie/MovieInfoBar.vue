<template>
  <div class="data-info-bar">
    <div
      v-if="onTarget !== idx"
      class="data-info"
    >{{ title }} | {{ genresStr }} | {{ rating }} | {{ viewCnt }}</div>
    <div v-else class="data-edit">
      <label for="title"></label>
      <input v-model="movieTitle" id="title" type="text" />
      <div class="genres">
        <button
          v-for="(genre, idx) of inputGenres"
          class="genre_button"
          @click="disGenre(idx)"
        >{{ genre }}</button>
      </div>
    </div>
    <div class="data-controller">
      <i v-if="onTarget === idx" class="fas fa-check" @click="editInfo"></i> |
      <i class="fas fa-edit" @click="checkEdit"></i> |
      <i class="fas fa-trash-alt" @click="delMovie"></i>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  props: {
    id: {
      type: Number,
      default: 0
    },
    title: {
      type: String,
      default: ""
    },
    genres: {
      type: Array,
      default: () => new Array()
    },
    img: {
      type: String,
      default: ""
    },
    rating: {
      type: Number,
      default: 0.0
    },
    viewCnt: {
      type: Number,
      default: 0
    },
    idx: {
      type: Number,
      default: 0
    },
    target: {
      type: Function,
      default: () => {}
    },
    onTarget: {
      type: Number,
      default: 0
    },
    inputGenres: {
      type: Array,
      default: () => new Array()
    },
    resetGenre: {
      type: Function,
      default: () => {}
    },
    checkGenre: {
      type: Function,
      default: () => {}
    },
    insertGenre: {
      type: Function,
      default: () => {}
    },
    edited: {
      type: Function,
      default: () => {}
    },
    deleted: {
      type: Function,
      default: () => {}
    }
  },
  computed: {
    genresStr: function() {
      return this.genres.join(" / ");
    },
    ...mapState({ getToken: state => state.user.token }),
    ...mapState({ getUsername: state => state.user.username }),
    ...mapState({ getEdit: state => state.movie.editCom }),
    ...mapState({ getDel: state => state.movie.delCom })
  },
  mounted() {
    this.movieTitle = this.title;
  },
  data: () => ({
    check: false,
    movieTitle: ""
  }),
  methods: {
    checkEdit() {
      this.target(this.idx, this.genres);
      this.check = !this.check;
    },
    ...mapActions("movie", ["editMovie"]),
    disGenre(idx) {
      this.insertGenre(this.inputGenres.splice(idx, 1)[0]);
    },
    ...mapActions("user", ["logout"]),
    async editInfo() {
      const params = {
        id: this.id,
        token: this.getToken,
        username: this.getUsername,
        movie: {
          title: this.movieTitle,
          genres: this.inputGenres
        }
      };
      await this.editMovie(params);
      if (this.getEdit === "영화 정보가 수정되었습니다.") {
        this.edited(this.idx, params["movie"]);
        this.checkEdit();
      } else if (this.getEdit === "token") {
        this.logout({ username: sessionStorage.getItem("adminName") });
      }
    },
    ...mapActions("movie", ["getMovieList"]),
    ...mapActions("movie", ["deleteMovie"]),
    async delMovie() {
      const params = {
        id: this.id,
        token: this.getToken,
        username: this.getUsername
      };
      await this.deleteMovie(params);
      if (this.getDel === "영화가 삭제되었습니다.") {
        this.getMovieList();
      } else if (this.getDel === "token") {
        this.logout({ username: sessionStorage.getItem("adminName") });
      }
    }
  }
};
</script>

<style scoped lang="scss">
.data-info-bar {
  border-radius: 5px;
  height: auto;
  min-height: 5vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 1px 1px 3px;
  padding: {
    top: 10px;
    bottom: 10px;
  }

  .data-info {
    padding: 0 1vw;
    font-family: "Lato", sans-serif;
    color: #535353;
  }

  .data-controller {
    padding: 0 1vw;
    color: #535353;
    .fa-edit:hover {
      color: #41b883;
    }
    .fa-trash-alt:hover {
      color: #fe1a1a;
    }
  }
}
.data-edit {
  padding: {
    left: 14px;
  }
  display: flex;
  justify: {
    content: space-between;
  }
  button {
    margin: {
      left: 10px;
    }
  }
}
.check_button {
  display: inline-flex;
  padding: 0.5vw !important;
}
.genre_button {
  background: {
    color: rgba(254, 255, 0, 0.37);
  }
  padding: 5px;
  border: rgba(255, 183, 0, 1) solid 2px;
  border-radius: 10px;
}
.genre_button:hover {
  background: {
    color: rgba(255, 221, 0, 0.5);
  }
}
.fa-check:hover {
  color: rgba(0, 76, 255, 0.96);
}
</style>
