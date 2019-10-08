const state = {
  isLoading: false
};

const mutations = {
  toggleLoader(state) {
    state.isLoading = !state.isLoading
  }
}

export default {
  namespaced: true,
  state,
  mutations,
}