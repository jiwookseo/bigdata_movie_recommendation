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
    const movies = response.data.map(movie => ({
      id: movie.id,
      title: movie.title,
      genres: movie.genres_array,
      viewCnt: movie.view_cnt,
      rating: movie.average_rating,
    }))
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