import api from "../../api";
import User from "./user";

const state = {
  detailToggler: false,
  detailType: "",
  activateMovie: {},
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
  similarUser: state => state.similarUser
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
    const data = await api.getRelatedMovies(param);
    console.log(data)
    console.log(1)
    if (data.status === 203 && data.data.error === "token") {
      const req = {
        "username": param.username
      }
      await api.logout(req)
    }

    commit("setRelatedMovie", data.data);
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
