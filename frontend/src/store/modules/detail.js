import api from "../../api";

const state = {
  detailMovie: {}
}

const getters = {
  detailMovie: state => state.detailMovie
}

const actions = {
  async setDetailMovie({ commit }, param){
    const data = await api.getMovie(param)
    commit("setDetailMovie", data.data)
  }
}

const mutations = {
  setDetailMovie: (state, payload) => { state.detailMovie = payload }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
};
