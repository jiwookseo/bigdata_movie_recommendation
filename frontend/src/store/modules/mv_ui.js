const state = {
  detailToggler: false,
  activateMovie: {},
  isLogin: false,
  id:null,
}

const getters = {
  movie: state => state.activateMovie,
  getIsLogin: state => {
    return state.isLogin;
  },
  getId: state => {
    return state.id;
  }
}

const mutations = {
  setDetailToggler: state => (state.detailToggler = !state.detailToggler),
  setActivateMovie: (state, payload) => (state.activateMovie = payload),

  // 추가
  setIsLogin(state, isLogin) {
  state.isLogin = isLogin;
},
  setId(state, id) {
    state.id = id;
  },
}


export default {
  namespaced: true,
  state,
  mutations,
  getters
}
