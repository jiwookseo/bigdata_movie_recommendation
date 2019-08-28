import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  movieSelected: [],
  userSearchList: [],
  userSelected: [],
}

// actions
const actions = {
  async get_moviesKey({ commit }, params) {
    const resp = await api.get_moviesKey(params);
    const movies = resp.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCnt: d.rating_count,
      rating: d.avg_rating,
    }));
    commit('setMovieSearchList', movies)
  },

  async get_movieKey({ commit }, params) {
    const resp = await api.get_moviesKey(params);
    const movie = resp.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCnt: d.rating_count,
      rating: d.avg_rating,
      story: d.story,
      ratings: d.ratings
    }));
    commit("setMovieSelected", movie)
  },
  async get_usersKey({ commit }, params) {
    const resp = await api.get_usersKey(params);
    const users = resp.data.map(d => ({
      id: d.id,
      username: d.username,
      is_staff: d.is_staff,
      gender: d.gender,
      age: d.age,
      occupation: d.occupation,
    }));
    commit('setUserSearchList', users)
  },

  async get_userKey({ commit }, params) {
    const resp = await api.get_usersKey(params);
    const user = resp.data.map(d => ({
      id: d.id,
      username: d.username,
      is_staff: d.is_staff,
      gender: d.gender,
      age: d.age,
      occupation: d.occupation,
      ratings: d.ratings
    }));
    commit("setUserSelected", user)
  }
};

// mutations
const mutations = {
  setMovieSearchList(state, movies) {
    state.movieSearchList = movies.map(m => m)
  },
  setMovieSelected(state, movie) {
    state.movieSelected = movie.map(m => m)
  },
  setUserSearchList(state, users) {
    state.userSearchList = users.map(m => m)
  },
  setUserSelected(state, user) {
    state.userSelected = user.map(m => m)
  }
};

export default {
  namespaced: true,
  state,
  actions,
  mutations
}