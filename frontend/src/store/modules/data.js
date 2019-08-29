import api from "../../api";

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  movie: {},
  audience: [],
  userSearchList: [],
  user: {},
  ratings: []
};

// getters
const getters = {
  movieSearchList: state => state.movieSearchList,
  movie: state => state.movie,
  audience: state => state.audience,
  userSearchList: state => state.userSearchList,
  user: state => state.user,
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
      rating: resp.data.avg_rating,
      story: resp.data.story
    };
    commit("setMovie", movie);
    const res = await api.getAudience(id);
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
      rating: d.avg_rating,
      story: resp.data.story
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
    commit("setUser", user);
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
  setMovie: (state, payload) => (state.movie = payload),
  setUserSearchList: (state, payload) => (state.userSearchList = payload),
  setUser: (state, payload) => (state.user = payload),
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
