import api from "../../api";

// initial state
const state = {
  movieSearchList: [],
  movie: {},
  audience: [],
  recAge: [],
  recOccupation: [],
  recGender: []
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

  // Recommendation
  async getRecByAge({ commit }, age) {
    const resp = await api.searchMovies({
      age,
      start: state.recAge.length
    });
    if (state.recAge.length <= resp.data.start) {
      const movies = [
        ...state.recAge,
        ...resp.data.data.map(item => getMovieStucture(item))
      ];
      commit("setRecAge", movies);
    }
  },
  async getRecByOccupation({ commit }, occupation) {
    const resp = await api.searchMovies({
      occupation,
      start: state.recOccupation.length
    });
    if (state.recOccupation.length <= resp.data.start) {
      const movies = [
        ...state.recOccupation,
        ...resp.data.data.map(item => getMovieStucture(item))
      ];
      commit("setRecOccupation", movies);
    }
  },
  async getRecByGender({ commit }, gender) {
    const resp = await api.searchMovies({
      gender,
      start: state.recGender.length
    });
    if (state.recGender.length <= resp.data.start) {
      const movies = [
        ...state.recGender,
        ...resp.data.data.map(item => getMovieStucture(item))
      ];
      commit("setRecGender", movies);
    }
  }
};

// mutations
const mutations = {
  setMovieSearchList: (state, payload) => (state.movieSearchList = payload),
  setMovie: (state, payload) => (state.movie = payload),
  setAudience: (state, payload) => (state.audience = payload),
  setRecAge: (state, payload) => (state.recAge = payload),
  setRecOccupation: (state, payload) => (state.recOccupation = payload),
  setRecGender: (state, payload) => (state.recGender = payload)
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
};
