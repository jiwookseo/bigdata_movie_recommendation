import api from "../../api";
import User from "./user";

const state = {
  relatedStatus: false,
  detailToggler: false,
  detailType: "",
  activateMovie: { id: 0 },
  relatedMovies: {},
  sliderType: "",
  similarUser: [],
  sliderProfileData: [
    {
      type: "평가한 영화",
      selectObject: {}
    }
  ],
  sliderBoardData: [
    {
      type: "연령대",
      selectObject: {
        1: "18세 미만이",
        18: "18-24세가",
        25: "25-34세가",
        35: "35-44세가",
        45: "45-49세가",
        50: "50-55세가",
        56: "56세 이상이"
      }
    },
    {
      type: "직업",
      selectObject: {
        "academic/educator": "교육인이",
        artist: "예술가가",
        "clerical/admin": "사무직이",
        "college/grad student": "대학생이",
        "K-12 student": "학생이",
        "customer service": "서비스직이",
        "doctor/health care": "의료인이",
        "executive/managerial": "관리직이",
        farmer: "농업인이",
        homemaker: "가정주부가",
        lawyer: "법조인이",
        programmer: "프로그래머가",
        "sales/marketing": "마케터가",
        scientist: "과학자가",
        "self-employed": "자영업자가",
        "technician/engineer": "기술자가",
        "tradesman/craftsman": "수공업자가",
        writer: "작가가"
      }
    },
    {
      type: "성별",
      selectObject: {
        M: "남성이",
        F: "여성이"
      }
    }
  ]
};

const getters = {
  movie: state => state.activateMovie,
  detailToggler: state => state.detailToggler,
  detailType: state => state.detailType,
  relatedMovie: state => state.relatedMovies,
  sliderType: state => state.sliderType,
  sliderBoardData: state => state.sliderBoardData,
  sliderProfileData: state => state.sliderProfileData,
  similarUser: state => state.similarUser,
  activateMovie: state => state.activateMovie
};

const actions = {
  setDetailToggler({ commit }, type = "") {
    if (state.detailToggler && state.detailType !== type) {
      commit("setDetailType", type);
    } else {
      commit("setDetailType", type);
      commit("setDetailToggler");
    }
  },

  async setRelatedMovies({ commit }, param) {
    console.log(param)
    const data = await api.getRelatedMovies(param);
      if (data.status === 202) {
        commit("setRelatedMovie", data.data);
        commit("setRelatedStatus", true);
      } else if (data.status === 203 && data.data.error === "token") {
        User.state.isLogin = false;
        User.state.username = "";
        User.state.is_staff = false;
        User.state.token = "";
        User.state.subscribe = false;
        sessionStorage.clear();
        this.$router.push("/");
    }
  },

  async setSimilarUser({ commit }, param) {
    const data = await api.getRelatedUsers(param);
    commit("setSimilarUser", data.data);
  }
};

const mutations = {
  setDetailToggler: state => (state.detailToggler = !state.detailToggler),
  setActivateMovie: (state, payload) => (state.activateMovie = payload),
  setDetailType: (state, payload) => (state.detailType = payload),
  setRelatedMovie: (state, payload) => (state.relatedMovies = payload),
  setRelatedStatus: (state, payload) => (state.relatedStatus = payload),
  setSliderType: (state, payload) => (state.sliderType = payload),
  setSimilarUser: (state, payload) => (state.similarUser = payload)
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
};
