import axios from "axios";

const BASE_URL = "/api";

export default {
  // Movies
  searchMovies(params) {
    return axios.get(`${BASE_URL}/movies/`, { params });
  },
  getMovie(id) {
    return axios.get(`${BASE_URL}/movies/${id}/`);
  },
  getAudience(id, params) {
    return axios.get(`${BASE_URL}/movies/${id}/ratings/`, { params });
  },
  getFollowers(id) {
    return axios.get(`${BASE_URL}/movies/${id}/followers/`);
  },
  getRecommendations(id) {
    return axios.get(`${BASE_URL}/movies/${id}/recommendations/`);
  },
  follow(id, params) {
    return axios.post(`${BASE_URL}/movies/${id}/followers/`, params);
  },

  // Users
  searchUsers(params) {
    return axios.get(`${BASE_URL}/users/`, {
      params
    });
  },
  getUser(username) {
    return axios.get(`${BASE_URL}/users/${username}`);
  },
  getRating(username, id) {
    return axios.get(`${BASE_URL}/users/${username}/ratings/?movieId=${id}`);
  },
  getRatings(username) {
    return axios.get(`${BASE_URL}/users/${username}/ratings/`);
  },
  setRating(username, id, params) {
    return axios.post(`${BASE_URL}/ratings/${username}/${id}/`, params);
  },
  getFollowings(username) {
    return axios.get(`${BASE_URL}/users/${username}/followings/`);
  },
  setProfile(username, formData) {
    return axios.post(`${BASE_URL}/users/${username}/profile/`, formData);
  },
  getRecommendedMovies(username) {
    return axios.get(`${BASE_URL}/users/${username}/recm_movies/`);
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
  subscribe(params) {
    return axios.post(`${BASE_URL}/subscribe/`, params);
  },

  // Clustering 결과
  getRelatedMovies(params) {
    return axios.post(`${BASE_URL}/movies/related_movies/`, params);
  },
  getRelatedUsers(params) {
    return axios.get(`${BASE_URL}/users/related_users/${params}`);
  }
};
