const state = {
  detailToggler: false,
  detailType: "",
  activateMovie: {}
};

const getters = {
  movie: state => state.activateMovie,
  detailToggler: state => state.detailToggler,
  detailType: state => state.detailType
};

const actions = {
  setDetailToggler({ commit }, type = "") {
    if (state.detailToggler && state.detailType !== type) {
      commit("setDetailType", type);
    } else {
      commit("setDetailType", type);
      commit("setDetailToggler");
    }
  }
};

const mutations = {
  setDetailToggler: state => (state.detailToggler = !state.detailToggler),
  setActivateMovie: (state, payload) => (state.activateMovie = payload),
  setDetailType: (state, payload) => (state.detailType = payload)
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
};
