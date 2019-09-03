import axios from "axios";

const BASE_URL = "/api";

export default {
  searchMovies(params) {
    return axios.get(`${BASE_URL}/movies/`, {
      params
    });
  },
  getMovie(id) {
    return axios.get(`${BASE_URL}/movies/${id}/`);
  },
  getAudience(id) {
    return axios.get(`${BASE_URL}/movies/${id}/ratings/`);
  },
  searchUsers(params) {
    return axios.get(`${BASE_URL}/users/`, {
      params
    });
  },
  getUser(username) {
    return axios.get(`${BASE_URL}/users/${username}`);
  },
  getRatings(username) {
    return axios.get(`${BASE_URL}/users/${username}/ratings/`);
  },
  login(params) {
    return axios.post("http://localhost:8000/api/login/", params);
  },
  register(params) {
    return axios.post("http://localhost:8000/api/signup/", params);
  }
};
