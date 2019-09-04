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
  getFollowers(id) {
    return axios.get(`${BASE_URL}/movies/${id}/followers/`);
  },
  follow(id) {
    return axios.post(`${BASE_URL}/movies/${id}/followers/`);
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
  getFollowings(username) {
    return axios.get(`${BASE_URL}/users/${username}/followings/`);
  },
  login(params) {
    return axios.post(`${BASE_URL}/login/`, params);
  },
  logout(params) {
    return axios.post(`${BASE_URL}/logout/`, params);
  },
  register(params) {
    return axios.post(`${BASE_URL}/signup/`, params);
  },
  getRelatedMovies(params) {
    return axios.get(`${BASE_URL}/movies/related_movies/`, { params});
  },
};
