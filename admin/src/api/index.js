import axios from "axios";

const apiUrl =
  process.env.NODE_ENV === "production"
    ? "http://52.78.81.59:8000/api"
    : "http://localhost:8000/api";
const clusterUrl = 
  process.env.NODE_ENV === 'production'
    ? "http://52.78.81.59:8000/cluster"
    : "http://localhost:8000/cluster";


export default {
  // Movies
  getMovieList() {
    return axios.get(`${apiUrl}/admin/movies/`);
  },

  getRelatedMovies(params) {
    return axios.get(`${apiUrl}/movies/related_movies/`, {
      params
    });
  },

  editMovie(id, params) {
    return axios.put(`${apiUrl}/movies/${id}/`, params);
  },

  deleteMovie(id, params) {
    return axios.delete(`${apiUrl}/movies/${id}/`, { data: params });
  },

  // Users
  getUserList() {
    return axios.get(`${apiUrl}/admin/users/`);
  },

  getRelatedUsers(params) {
    return axios.get(`${apiUrl}/users/related_users/${params.userId}`);
  },

  editUser(username, params) {
    return axios.put(`${apiUrl}/users/${username}/`, params);
  },

  deleteUser(username, params) {
    return axios.delete(`${apiUrl}/users/${username}/`, { data: params });
  },

  // login, logout
  login(params) {
    return axios.post(`${apiUrl}/login/`, params);
  },
  logout(params) {
    return axios.post(`${apiUrl}/logout/`, params);
  },

  // Clustering
  clusteringMovies(params) {
    return axios.post(`${clusterUrl}/movies/`, params);
  },

  clusteringUsers(params) {
    return axios.post(`${clusterUrl}/users/`, params);
  },

  // Collaborative Filtering
  collaborativeFiltering(params) {
    // console.log("check")
    return axios.post(`${clusterUrl}/users/recommended_movies/`, params);
  },

  // Recommendation Refreshing
  async recommendation() {
    await axios.post(`${apiUrl}/movies/recommendations/`);
  }
};
