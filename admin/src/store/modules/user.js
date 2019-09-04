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
  async getUserList({ commit }) {
    try {
      const response = await api.getUserList();
      const users = response.data.map(user => ({
        id: user.id,
        username: user.username,
        gender: user.gender,
        age: user.age,
        occupation: user.occupation,
        isStaff: user.is_staff
      }))
      commit('setUserList', users)
    } catch(error) {
      console.log(error);
    }
  },

  async clusteringUsers({ commit }, params) {
    try {
      const response = await api.clusteringUsers(params);
      console.log(response.status);
    } catch(error) {
      console.log(error);
    }
  },

  async getRelatedUsers({ commit }, params) {
    try {
      const response = await api.getRelatedUsers(params);
      console.log(response.data);
    } catch(error) {
      console.log(error);
    }
  }
}


export default {
  namespaced: true,
  state,
  mutations,
  actions
}