<template>
  <div class="profile">
    <div class="profile--info">
      <div class="profile--info-image">
        <div>
          <img
            :src="user.image || 'data:image/jpeg;base64,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'"
            @click="pickFile"
          />
        </div>
        <div class="img--picker">
          <input type="file" ref="image" accept="image/*" @change="onFilePicked" />
        </div>
        <div class="profile--div">
          <p class="profile--info-username">
            {{ user.username }}
            <button v-if="loginUsername === $route.params.username"
                    class="material-icons edit-button"
                    @click="editInfo = true"
            >create</button>
          </p>
          <p class="profile--info-description">여기에 간단한 소개글이 들어갑니다.</p>
        </div>
      </div>
      <div class="profile--info-data">
        <div class="profile--info-data-bar">
          <div class="profile-info-data-num">
            <span>22</span>
            <span>33</span>
            <span>{{ user.rating_cnt }}</span>
          </div>
          <div class="profile-info-data-text">
            <span>보고 싶어요</span>
            <span>시청한 영화</span>
            <span>평가한 영화</span>
          </div>
          <div v-if="editInfo">
            <editUserInfo :user="user" :back="editChange" />
          </div>
        </div>
      </div>
    </div>

    <div class="profile--detail">
      <div>
        <ImageSlider v-if="ratings.length" :sliderList="sliderList" :expand="true" :related="getSubscribe" />
        <div v-else class="profile--rating--empty">
          <h2>아직 평가한 영화가 없습니다.</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ImageSlider from "../imageSlider";
import SimilarUserList from "./similarUserList";
import editUserInfo from "./editUserInfo";
import { mapGetters, mapState } from "vuex";

export default {
  name: "Profile",
  components: {ImageSlider, SimilarUserList, editUserInfo },
  data: () => ({
    editInfo: false,
  }),
  computed: {
    ...mapGetters("user", ["user", "ratings"]),
    ...mapState({
      getSubscribe: state => Boolean(state.user.subscribe),
      loginUsername: state => state.user.username
    }),
    sliderList() {
      return [
        {
          type: "평가한 영화",
          selectedObject: ""
        }
      ];
    }
  },
  watch: {
    "$route.params.username": function(username) {
      this.$store.dispatch("user/getUserByUsername", username);
      this.$store.dispatch("mvUi/setSimilarUser", username);
    }
  },
  created() {
    this.$store.commit("mvUi/setSliderType", "profile");
  },
  mounted() {
    const username = this.$route.params.username;
    // this.$store.commit("user/setUsername", username);
    this.$store.dispatch("user/getUserByUsername", username);
    this.$store.dispatch("mvUi/setSimilarUser", username);
    console.log(this.$route.params.username, this.loginUsername)
  },
  methods: {
    editChange() {
      this.editInfo = false;
    },
    pickFile() {
      this.$refs.image.click();
    },
    onFilePicked() {
      const file = this.$refs.image.files[0];
      const data = new FormData();
      data.append("image", file, file.name);
      // this.$store.dispatch("setSpinner", {
      //   loading: true,
      //   message: "Uploading..."
      // });
      this.$store.dispatch("user/setUserProfileByUsername", {
        username: this.user.username,
        data
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.profile {
  display: flex;

  padding-top: 64px;
  background-color: #111;
  min-height: 100vh;
  height: auto;
}

.profile--info {
  display: flex;
  flex-direction: column;
  align-items: space-between;

  width: 25%;
  min-height: calc(100vh - 64px);
  height: auto;
}

.profile--info-image {
  display: flex;
  flex-direction: column;
  align-items: center;

  width: 100%;
  border-radius: 50%;

  .img--picker {
    display: none;
  }

  div {
    margin-top: 30px;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-top: 20px;
    padding-left: 20px;

    img {
      width: 60%;
      object-fit: contain;
      border-radius: 50%;
    }
    p {
      font-weight: 700;
      &.profile--info-username {
        color: #fff;

        font-size: 20px;
        letter-spacing: 2px;
      }
      &.profile--info-description {
        color: #aaa;
        font-size: 16px;
        letter-spacing: 1.6px;
      }
    }
    p + p {
      margin-top: 20px;
    }
  }
}

.profile--info-data {
  margin-top: 40px;
  width: 100%;
}

.profile--info-data-bar {
  display: flex;
  flex-direction: column;

  div {
    display: flex;
    justify-content: space-around;
    padding: 10px 20px 5px;

    &.profile-info-data-num {
      span {
        font-size: 20px;
        font-weight: 700;
        color: #fff;
      }
    }
    &.profile-info-data-text {
      span {
        font-size: 14px;
        color: #ccc;
        font-weight: 700;
      }
    }
  }
}

.profile--detail {
  width: 80%;
  min-height: calc(100vh - 64px);
  overflow-x: hidden;

  .profile--rating--empty {
    padding: 60px 0 20px 30px;
    display: flex;
    h2 {
      display: inline-block;
      margin-right: 14px;
      color: #fff;
      font-size: 28px;
      font-weight: 700;
    }
  }
}
</style>
