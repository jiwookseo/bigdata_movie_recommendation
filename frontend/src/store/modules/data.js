import api from "../../api";

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  movieSelected: [],
  audience: [],
  userSearchList: [],
  userSelected: [],
  ratings: []
};

// getters
const getters = {
  movieSearchList: state => state.movieSearchList,
  movieSelected: state => state.movieSelected,
  audience: state => state.audience,
  userSearchList: state => state.userSearchList,
  userSelected: state => state.userSelected,
  ratings: state => state.ratings
};

// actions
const actions = {
  // Movie
  async getMovieById({ commit }, id) {
    const resp = await api.getMovie(id);
    const movie = {
      id: resp.data.id,
      title: resp.data.title,
      genres: resp.data.genres_array,
      viewCnt: resp.data.rating_count,
      rating: resp.data.avg_rating
    };
    commit("setMovie", movie);
    const res = await api.getPeople(id);
    const audience = res.data.map(d => d.username);
    commit("setAudience", audience);
  },
  async searchMovies({ commit }, params) {
    const resp = await api.searchMovies(params);
    const movies = resp.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCnt: d.rating_count,
      rating: d.avg_rating
    }));

    commit("setMovieSearchList", movies);
  },
  setEmptyMovieList({ commit }) {
    commit("setMovieSearchList", []);
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
    commit("setUserSelected", user);
    const res2 = await api.getRatings(username);
    commit("setRatings", res2.data);
  },
  setEmptyUserList({ commit }) {
    commit("setUserSearchList", []);
  }
};

// mutations
const mutations = {
  setMovieSearchList: (state, payload) => (state.movieSearchList = payload),
  setMovieSelected: (state, payload) => (state.movieSelected = payload),
  setUserSearchList: (state, payload) => (state.userSearchList = payload),
  setUserSelected: (state, payload) => (state.userSelected = payload),
  setRatings: (state, payload) => (state.ratings = payload),
  setAudience: (state, payload) => (state.audience = payload)
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
};
