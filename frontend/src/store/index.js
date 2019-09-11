import Vue from "vue";
import Vuex from "vuex";
import user from "./modules/user";
import movie from "./modules/movie";
import mvUi from "./modules/mv_ui";
import snackbar from "./modules/snackbar";
import detail from "./modules/detail"
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    movie,
    mvUi,
    snackbar,
    detail,
  }
});
