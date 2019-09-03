import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieList: [],
}

// mutations
const mutations = {
  setMovieList(state, movies) {
    state.movieList = movies.map(m => m)
  },
}

// actions
const actions = {
  async getMovieList({ commit }) {
    const response = await api.getMovieList()
    const movies = response.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCnt: d.view_cnt,
      rating: d.average_rating,
    }))
    console.log("check")
    commit('setMovieList', movies)
  },

  async clusteringMovies({ commit }, params) {
    try {
      const response = await api.clusteringMovies(params);
      console.log(response.status);
    } catch(error) {
      console.log(error);
    }
  },
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}