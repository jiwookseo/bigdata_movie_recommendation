import api from "../../api";

const state = {
  detailToggler: false,
  detailType: "",
  activateMovie: {},
  relatedMovies: {}
};

const getters = {
  movie: state => state.activateMovie,
  detailToggler: state => state.detailToggler,
  detailType: state => state.detailType,
  relatedMovie: state => state.relatedMovies
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
  async setRelatedMovies({ commit }, param){
    const data = await api.getRelatedMovies(param)
    commit("setRelatedMovie", data.data)
  }
};

const mutations = {
  setDetailToggler: state => (state.detailToggler = !state.detailToggler),
  setActivateMovie: (state, payload) => (state.activateMovie = payload),
  setDetailType: (state, payload) => (state.detailType = payload),
  setRelatedMovie: (state, payload) => (state.relatedMovies = payload)
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
};
