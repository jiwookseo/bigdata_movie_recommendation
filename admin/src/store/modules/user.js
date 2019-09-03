import api from '../../api'


// state
const state = {
  userList : []
}


// mutations
const mutations = {
  setUserList(state, users) {
    state.userList = users
  }
}


// actions
const actions = {
  async clusteringUsers({ commit }, params) {
    try {
      const response = await api.clusteringUsers(params);
      console.log(response.status);
    } catch(error) {
      console.log(error);
    }
  },
}


export default {
  namespaced: true,
  state,
  mutations,
  actions
}