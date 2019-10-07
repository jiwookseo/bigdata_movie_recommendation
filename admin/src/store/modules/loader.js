const state = {
  isActive: false
};

const mutations = {
  toggleLoader(state) {
    state.isActive = !state.isActive
  }
}

export default {
  namespaced: true,
  state,
  mutations,
}