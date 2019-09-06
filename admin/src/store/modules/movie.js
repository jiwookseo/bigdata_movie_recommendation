import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieList: [],
  editCom: "",
  delCom: "",
}

// mutations
const mutations = {
  setMovieList(state, movies) {
    state.movieList = movies.map(m => m)
  },
  editComment: (state, comment) => (state.editCom = comment),
  deleteComment: (state, comment) => (state.delCom = comment),
}

// actions
const actions = {
  async getMovieList({ commit }) {
    const response = await api.getMovieList()
    const movies = response.data.map(movie => ({
      id: movie.id,
      title: movie.title,
      genres: movie.genres_array,
      viewCnt: movie.rating_count,
      rating: movie.avg_rating,
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

  async editMovie({ commit }, params) {
  const id = params.id;
  const res = await api.editMovie(id, params);
  if (res.status === 202) {
    commit("editComment", "영화 정보가 변경되었습니다.")
  } else {
    if (res.data.error) {
      commit("editComment", res.data.error)
    } else {
      commit("editComment", "정보 수정을 실패했습니다.")
    }
  }
},

  async deleteMovie({ commit }, params) {
  const id = params.id;
  const res = await api.deleteMovie(id, params);
  if (res.status === 200) {
    commit("deleteComment", "영화가 삭제되었습니다.")
  } else {
    if (res.data.error) {
      commit("deleteComment", res.data.error)
    } else {
      commit("deleteComment", "영화 삭제를 실패했습니다.")
    }
  }
}
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}
