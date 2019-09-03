import axios from 'axios'

const apiUrl = '/api'

export default {
  searchMovies(params) {
    return axios.get(`${apiUrl}/movies/`, {
      params,
    })
  },
  clusteringMovies(params) {
    return axios.post(`${apiUrl}/clustering/movies/`, {
      params,
    })
  }
}