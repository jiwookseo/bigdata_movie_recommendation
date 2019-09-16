import api from '../../api'


// state
const state = {
  userList : [],
  isLogin: false,
  username: "",
  checkStaff: false,
  token: "",
  logErrors: "",
  editCom: "",
  delCom: "",
}


// mutations
const mutations = {
  setUserList(state, users) {
    state.userList = users
  },
  setIsLogin: (state, payload) => (state.isLogin = payload),
  setUsername: (state, payload) => (state.username = payload),
  setStaff: (state, payload) => (state.checkStaff = payload),
  setToken: (state, payload) => (state.token = payload),
  setLogError: (state, payload) => (state.logErrors = payload),
  editComment: (state, comment) => (state.editCom = comment),
  delComment: (state, comment) => (state.delCom = comment),
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
},

  async editUserInfo({ commit }, params) {
  const username = params.name;
  const res = await api.editUser(username, params);
  if (res.status === 202) {
    commit("editComment", "유저 정보가 변경되었습니다.")
  } else {
    if (res.data.error) {
      commit("editComment", res.data.error)
    } else {
      commit("editComment", "정보 수정을 실패했습니다.")
    }
  }
},

  async deleteUser({ commit }, params) {
  const username = params.name;
  const res = await api.deleteUser(username, params);
  if (res.status === 202) {
    commit("delComment", "유저가 삭제되었습니다.")
  } else {
    if (res.data.error) {
      commit("delComment", res.data.error)
    } else {
      commit("delComment", "유저 삭제를 실패했습니다.")
    }
  }
},

// login
  async setLogin({ commit }, params) {
    const res = await api.login(params);
    if (res.status === 202 && res.data.is_staff) {
      commit("setIsLogin", true);
      commit("setUsername", res.data.username);
      commit("setStaff", res.data.is_staff);
      commit("setToken", res.data.token);
      sessionStorage.setItem("adminLogin", true);
      sessionStorage.setItem("adminName", res.data.username);
      sessionStorage.setItem("adminCheck", res.data.is_staff);
      sessionStorage.setItem("adminToken", res.data.token);
    } else if (res.status === 203) {
      if (res.data["__all__"]) {
        commit("setLogError", res.data["__all__"][0]["message"])
      } else if (res.data.username) {
        commit("setLogError", res.data.username[0]["message"])
      } else if (res.data.error) {
        commit("setLogError", "관리자만 로그인이 가능합니다. 권한을 확인해주세요.");
      }
    }
  },
  async logout({ commit }, params) {
    commit('setIsLogin', false);
    commit("setUsername", "");
    commit("setStaff", false);
    commit("setToken", "");
    sessionStorage.clear();
    await api.logout(params);
  },
};


export default {
  namespaced: true,
  state,
  mutations,
  actions
}
