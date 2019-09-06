import axios from 'axios'

const apiUrl = '/api'
const clusterUrl = '/cluster'

export default {
  // Movies
  getMovieList() {
    return axios.get(`${apiUrl}/admin/movies/`)
  },

  clusteringMovies(params) {
    return axios.post(`http://localhost:8000/cluster/movies/`,
        params,
    )
  },

  getRelatedMovies(params) {
    return axios.get(`${apiUrl}/movies/related_movies/`, {
      params,
    })
  },

  editMovie(id, params) {
    return axios.put(`${apiUrl}/movies/${id}/`, params)
  },

  deleteMovie(id, params) {
    return axios.delete(`${apiUrl}/movies/${id}/`, {data: params})
  },


  // Users
  getUserList() {
    return axios.get(`${apiUrl}/admin/users/`)
  },

  clusteringUsers(params) {
    return axios.post("http://localhost:8000/cluster/users/",
        params,
    )
  },

  getRelatedUsers(params) {
    return axios.get(`${apiUrl}/users/related_users/${params.userId}`)
  },

  editUser(username, params) {
    return axios.put(`${apiUrl}/users/${username}/`, params)
  },

  deleteUser(username, params) {
    return axios.delete(`${apiUrl}/users/${username}/`, {data: params})
  },

  // login, logout
  login(params) {
    return axios.post(`${apiUrl}/login/`, params);
  },
  logout(params) {
    return axios.post(`${apiUrl}/logout/`, params);
  },
}
