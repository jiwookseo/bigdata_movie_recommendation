import api from "../../api";

// initial state
const state = {
  userSearchList: [],
  user: {},
  followings: [],
  ratings: [],
  isLogin: false,
  username: "",
  userFollowings: [],
  register: "register",
  regErrors: {},
  logErrors: {},
  checkStaff: false,
  token: ""
};

// getters
const getters = {
  userSearchList: state => state.userSearchList,
  user: state => state.user,
  ratings: state => state.ratings,
  username: state => state.username,
  isLogin: state => state.isLogin,
  register: state => state.register,
  logErrors: state => state.logErrors
};

// actions
const actions = {
  // Login, Register
  async setLogin({ commit }, params) {
    const res = await api.login(params);
    if (res.status === 200) {
      commit("setIsLogin", true);
      commit("setUsername", res.data.username);
      commit("setStaff", res.data.is_staff);
      commit("setToken", res.data.token);
      sessionStorage.setItem("username", res.data.username);
      sessionStorage.setItem("isStaff", res.data.is_staff);
      sessionStorage.setItem("jwt", res.data.token);
      sessionStorage.setItem("isLogin", true);
      const res2 = await api.getFollowings(state.username);
      commit("setUserFollowings", res2.data);
    } else {
      commit("setIsLogin", false);
      commit("setLogError", res.data);
    }
  },
  async logout({ commit }, params) {
    const res = await api.logout(params);
    if (res.status === 200) {
      commit("setIsLogin", false);
      commit("setUsername", "");
      commit("setStaff", false);
      commit("setToken", "");
      sessionStorage.clear();
    }
  },
  async setRegister({ commit }, params) {
    const res = await api.register(params);
    if (res.status === 201) {
      commit("setRegister", "sign");
    } else if (res.status === 203) {
      commit("setRegError", res.data);
    }
  },

  // User
  async searchUsers({ commit }, params) {
    const resp = await api.searchUsers(params);
    const users = resp.data;
    commit("setUserSearchList", users);
  },
  async getUserByUsername({ commit }, username) {
    const res1 = await api.getUser(username);
    const user = res1.data;
    commit("setUser", user);
    const res2 = await api.getRatings(username);
    commit("setRatings", res2.data);
    const res3 = await api.getFollowings(username);
    commit("setFollowings", res3.data);
  },
  setEmptyUserList({ commit }) {
    commit("setUserSearchList", []);
  },

  // Follow
  async follow({ commit }, id) {
    if (state.isLogin) {
      await api.follow(id);
      const res = await api.getFollowings(state.username);
      commit("setUserFollowings", res.data);
    }
  }
};

// mutations
const mutations = {
  setUserSearchList: (state, payload) => (state.userSearchList = payload),
  setUser: (state, payload) => (state.user = payload),
  setRatings: (state, payload) => (state.ratings = payload),
  setFollowings: (state, payload) => (state.followings = payload),
  setUserFollowings: (state, payload) => (state.userFollowings = payload),
  setIsLogin: (state, payload) => (state.isLogin = payload),
  setUsername: (state, payload) => (state.username = payload),
  setStaff: (state, payload) => (state.checkStaff = payload),
  setToken: (state, payload) => (state.token = payload),
  setRegister: (state, payload) => (state.register = payload),
  setRegError: (state, payload) => (state.regErrors = payload),
  setLogError: (state, payload) => (state.logErrors = payload)
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
};
