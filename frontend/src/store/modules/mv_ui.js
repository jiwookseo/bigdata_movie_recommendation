const state = {
  detailToggler: false,
  activateMovie: {},
}

const getters = {
  movie: state => state.activateMovie,
}

const mutations = {
  setDetailToggler: state => (state.detailToggler = !state.detailToggler),
  setActivateMovie: (state, payload) => (state.activateMovie = payload),
}


export default {
  namespaced: true,
  state,
  mutations,
  getters
}
