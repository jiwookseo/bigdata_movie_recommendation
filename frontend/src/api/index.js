import axios from "axios";

const BASE_URL = "http://localhost:8000/api";

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
  getRating(username, id) {
    return axios.get(`${BASE_URL}/users/${username}/ratings/?movieId=${id}`)
  },
  getRatings(username) {
    return axios.get(`${BASE_URL}/users/${username}/ratings/`);
  },
  getFollowings(username) {
    return axios.get(`${BASE_URL}/users/${username}/followings/`);
  },
  setProfile(username, formData) {
    return axios.post(`${BASE_URL}/users/${username}/profile/`, formData);
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
  editUserInfo(username, params) {
    return axios.put(`${BASE_URL}/users/${username}/`, params);
  },

// Clustering 결과
  getRelatedMovies(params) {
    return axios.post(`${BASE_URL}/movies/related_movies/`, params);
  },
  getRelatedUsers(params) {
    return axios.get(`${BASE_URL}/users/related_users/${params}`);
  }
};
