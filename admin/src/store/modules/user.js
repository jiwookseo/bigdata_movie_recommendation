import api from '../../api'


// state
const state = {

}


// mutations
const mutations = {

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