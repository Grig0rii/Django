<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>Мой сайт</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text>Главная</v-btn>
      <v-btn text>О нас</v-btn>
      <v-btn text>Контакты</v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <v-row>
          <v-col cols="12">
            <v-card>
              <v-card-title>Добро пожаловать</v-card-title>
              <v-card-text>
                Это базовый компонент с использованием Vuetify
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>

    <v-footer app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    //
  }),
}
</script>

<style>
@import 'https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css';
@import 'https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css';
</style> 