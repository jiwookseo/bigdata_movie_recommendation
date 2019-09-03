const state = {
  snackbar: false,
  usage: "ask",
  target: "",
  confirm: false,
  text: "Hello, I'm a snackbar"
};

const getters = {
  snackbar: state => state.snackbar,
  usage: state => state.usage,
  target: state => state.target,
  confirm: state => state.confirm,
  text: state => state.text
};

const actions = {
  setSnackbar({ commit }, payload = { usage: "", text: "", target: "" }) {
    // 끌 때 => deafult value
    commit("setSnackbar", payload.usage === "" ? false : true);
    commit("setusage", payload.usage);
    commit("setTarget", payload.target);
    commit("setConfirm", false);
    commit("setText", payload.text);
  },
  confirmSnackbar({ commit }) {
    commit("setConfirm", true);
    commit("setSnackbar", false);
  }
};

const mutations = {
  setSnackbar: (state, payload) => (state.snackbar = payload),
  setConfirm: (state, payload) => (state.confirm = payload),
  setusage: (state, payload) => (state.usage = payload),
  setTarget: (state, payload) => (state.target = payload),
  setConfirmMessage: (state, payload) => (state.confirmMessage = payload),
  setText: (state, payload) => (state.text = payload)
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
};
