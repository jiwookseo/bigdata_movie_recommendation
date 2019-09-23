import api from "../../api";

// initial state
const state = {
  movieSearchList: [],
  movie: {},
  audience: [],
  recAge: { value: "", data: [] },
  selectedAge: "25",
  recOccupation: { value: "", data: [] },
  selectedOccupation: "programmer",
  recGender: { value: "", data: [] },
  selectedGender: "M"
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
  recAge: state => state.recAge.data,
  selectedAge: state => state.selectedAge,
  recOccupation: state => state.recOccupation.data,
  selectedOccupation: state => state.selectedOccupation,
  recGender: state => state.recGender.data,
  selectedGender: state => state.selectedGender
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
  async getRecByAge({ commit }) {
    console.log(state.recAge.value, state.selectedAge);
    const age = state.selectedAge;
    if (age == state.recAge.value) {
      const resp = await api.searchMovies({
        age,
        start: state.recAge.data.length
      });
      const movies = {
        value: age,
        data: [
          ...state.recAge.data,
          ...resp.data.data.map(item => getMovieStucture(item))
        ]
      };
      commit("setRecAge", movies);
    } else {
      const resp = await api.searchMovies({ age });
      const movies = {
        value: age,
        data: resp.data.data.map(item => getMovieStucture(item))
      };
      commit("setRecAge", movies);
    }
    commit("setSelectedAge", age);
  },
  async getRecByOccupation({ commit }) {
    const occupation = state.selectedOccupation;
    if (occupation == state.recOccupation.value) {
      const resp = await api.searchMovies({
        occupation,
        start: state.recOccupation.data.length
      });
      const movies = {
        value: occupation,
        data: [
          ...state.recOccupation.data,
          ...resp.data.data.map(item => getMovieStucture(item))
        ]
      };
      commit("setRecOccupation", movies);
    } else {
      const resp = await api.searchMovies({ occupation });
      const movies = {
        value: occupation,
        data: resp.data.data.map(item => getMovieStucture(item))
      };
      commit("setRecOccupation", movies);
    }
    commit("setSelectedOccupation", occupation);
  },
  async getRecByGender({ commit }) {
    const gender = state.selectedGender;
    if (gender == state.recGender.value) {
      const resp = await api.searchMovies({
        gender,
        start: state.recGender.data.length
      });
      const movies = {
        value: gender,
        data: [
          ...state.recGender.data,
          ...resp.data.data.map(item => getMovieStucture(item))
        ]
      };
      commit("setRecGender", movies);
    } else {
      const resp = await api.searchMovies({ gender });
      const movies = {
        value: gender,
        data: resp.data.data.map(item => getMovieStucture(item))
      };
      commit("setRecGender", movies);
    }
    commit("setSelectedGender", gender);
  }
};

// mutations
const mutations = {
  setMovieSearchList: (state, payload) => (state.movieSearchList = payload),
  setMovie: (state, payload) => (state.movie = payload),
  setAudience: (state, payload) => (state.audience = payload),
  setRecAge: (state, payload) => (state.recAge = payload),
  setSelectedAge: (state, payload) => (state.selectedAge = payload),
  setRecOccupation: (state, payload) => (state.recOccupation = payload),
  setSelectedOccupation: (state, payload) =>
    (state.selectedOccupation = payload),
  setRecGender: (state, payload) => (state.recGender = payload),
  setSelectedGender: (state, payload) => (state.selectedGender = payload)
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
};
