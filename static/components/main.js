import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.esm.browser.js'
import Vuetify from 'https://cdn.jsdelivr.net/npm/vuetify@2.6.14/dist/vuetify.min.js'
import App from './App.vue'

Vue.use(Vuetify)

const vuetify = new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#1976D2',
        secondary: '#424242',
        accent: '#82B1FF',
        error: '#FF5252',
        info: '#2196F3',
        success: '#4CAF50',
        warning: '#FFC107'
      }
    }
  }
})

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app') 