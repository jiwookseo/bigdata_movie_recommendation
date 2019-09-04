import axios from 'axios'

const apiUrl = '/api'

export default {
  // Movies
  getMovieList() {
    return axios.get(`${apiUrl}/admin/movies/`)
  },

  clusteringMovies(params) {
    return axios.post(`${apiUrl}/clustering/movies/`, 
      params,
    )
  },

  getRelatedMovies(params) {
    return axios.get(`${apiUrl}/movies/related_movies/`, {
      params,
    })
  },


  // Users
  clusteringUsers(params) {
    return axios.post(`${apiUrl}/clustering/users/`, 
      params,
    )
  }
}