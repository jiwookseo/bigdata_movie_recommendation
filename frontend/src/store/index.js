import Vue from 'vue'
import Vuex from 'vuex'
import data from './modules/data'
import mvUi from './modules/mv_ui'
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    data,
    mvUi
  },
})