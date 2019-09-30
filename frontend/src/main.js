import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import store from './store'
import axios from "axios"


Vue.config.productionTip = false


new Vue({
  vuetify,
  router,
  store,
  axios,
  render: h => h(App)
}).$mount('#app')
