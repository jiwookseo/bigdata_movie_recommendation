import api from "../../api";

// initial state
const state = {
  movieSearchList: [],
  movie: {},
  audience: [],
  userSearchList: [],
  user: {},
  followings: [],
  ratings: [],
  recAge: [],
  recOccupation: [],
  recGender: [],
  isLogin: false,
  username: "",
  userFollowings: [],
  register: "register"
};

// movie shape
const getMovieStucture = item => ({
  id: item.id,
  title: item.title,
  genres: item.genres_array,
  viewCnt: item.rating_count,
  rating: item.avg_rating,
  story: item.story,
  poster: item.poster,
  stillCut: item.still_cut
});

// getters
const getters = {
  movieSearchList: state => state.movieSearchList,
  movie: state => state.movie,
  audience: state => state.audience,
  userSearchList: state => state.userSearchList,
  user: state => state.user,
  ratings: state => state.ratings,
  recAge: state => state.recAge,
  recOccupation: state => state.recOccupation,
  recGender: state => state.recGender
};

// actions
const actions = {
  // Movie
  async searchMovies({ commit }, params) {
    const resp = await api.searchMovies(params);
    const movies = resp.data.map(d => getMovieStucture(d));
    commit("setMovieSearchList", movies);
  },
  async getMovieById({ commit }, id) {
    const resp = await api.getMovie(id);
    const movie = getMovieStucture(resp.data);
    commit("setMovie", movie);
    const res = await api.getAudience(id);
    commit("setAudience", res.data);
  },
  setEmptyMovieList({ commit }) {
    commit("setMovieSearchList", []);
  },

  // Login, Register
  async setLogin({ commit }, params) {
    const res = await api.login(params);
    if (res.status === 200) {
      commit("setIsLogin", true);
      const data = JSON.parse(res.config.data);
      commit("setUsername", data.login.username);
      const res = await api.getFollowings(state.username);
      commit("setUserFollowings", res.data);
    } else {
      commit("setIsLogin", false);
    }
  },
  async logout({ commit }) {
    commit('setIsLogin', false);
    commit("setId", null);
  },
  async setRegister({ commit }, params) {
    const res = await api.register(params);
    if (res.status === 201) {
      commit("setRegister", "sign");
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

  // Recommendation
  async getRecByAge({ commit }, age) {
    const resp = await api.searchMovies({ age });
    const movies = resp.data.map(item => getMovieStucture(item));
    commit("setRecAge", movies);
  },
  async getRecByOccupation({ commit }, occupation) {
    const resp = await api.searchMovies({ occupation });
    const movies = resp.data.map(item => getMovieStucture(item));
    commit("setRecOccupation", movies);
  },
  async getRecByGender({ commit }, gender) {
    const resp = await api.searchMovies({ gender });
    const movies = resp.data.map(item => getMovieStucture(item));
    commit("setRecGender", movies);
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
  setMovieSearchList: (state, payload) => (state.movieSearchList = payload),
  setMovie: (state, payload) => (state.movie = payload),
  setUserSearchList: (state, payload) => (state.userSearchList = payload),
  setUser: (state, payload) => (state.user = payload),
  setRatings: (state, payload) => (state.ratings = payload),
  setAudience: (state, payload) => (state.audience = payload),
  setFollowings: (state, payload) => (state.followings = payload),
  setUserFollowings: (state, payload) => (state.userFollowings = payload),
  setRecAge: (state, payload) => (state.recAge = payload),
  setRecOccupation: (state, payload) => (state.recOccupation = payload),
  setRecGender: (state, payload) => (state.recGender = payload),
  setIsLogin: (state, payload) => (state.isLogin = payload),
  setUsername: (state, payload) => (state.username = payload),
  setRegister: (state, payload) => (state.register = payload)
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
};
