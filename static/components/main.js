import App from './App.vue'

new Vue({
  el: '#app',
  vuetify: new Vuetify({
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
  }),
  components: { App },
  template: '<App><template v-slot:messages><div class="messages" v-if="messages.length"><v-alert v-for="message in messages" :key="message.id" :type="message.type" dismissible>{{ message.text }}</v-alert></div></template><template v-slot:default><slot></slot></template></App>',
  data: {
    messages: []
  },
  mounted() {
    // Конвертируем Django сообщения в формат Vue
    const djangoMessages = document.querySelectorAll('.messages .alert');
    djangoMessages.forEach((message, index) => {
      const type = message.classList.contains('alert-success') ? 'success' :
                  message.classList.contains('alert-error') ? 'error' :
                  message.classList.contains('alert-warning') ? 'warning' : 'info';
      this.messages.push({
        id: index,
        type: type,
        text: message.textContent.trim()
      });
    });
  }
}); 