import axios from 'axios'

const apiUrl = '/api';
const BASE_URL = "/api";


export default {
  searchMovies(params) {
    return axios.get(`${apiUrl}/movies/?title=`, {
      params,
    })
  },

  get_moviesKey(params) {
    return axios.get(BASE_URL + "/movies/?", {params})
  },

  get_usersKey(params) {
    return axios.get(BASE_URL + "/auth/signup-many/?", {params})
  }
}