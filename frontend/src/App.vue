<template>
  <v-app id="app">
    <v-app-bar app clipped-left color="indigo">
      <v-app-bar-nav-icon class="white--text" @click="drawer = !drawer" />
      <span class="title ml-3 mr-5 white--text">영화 추천 서비스</span>

      <v-spacer />
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" app clipped color="grey lighten-4">
      <v-list dense class="grey lighten-4">
        <template v-for="(choice, i) in choices">
          <v-list-item
            :key="i"
            @click="() => {
              if (choice.path) {
                goTo(choice.path)
              }
            }"
          >
            <v-list-item-action>
              <v-icon>{{ choice.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="subtitle-2 font-weight-bold black--text">{{ choice.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>

    <v-content>
      <v-container fluid fill-height class="grey lighten-4">
        <v-layout justify-center align-center>
          <!-- each pages will be placed here -->
          <router-view />
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import router from "./router";

export default {
  data: () => ({
    drawer: null,
    choices: [
      {
        icon: "mdi-movie",
        text: "영화 검색",
        path: "movie-search"
      },
      {
        icon: "people",
        text: "유저 검색",
        path: "user-search"
      }
    ]
  }),
  methods: {
    goTo: function(path) {
      router.push({ name: path });
    }
  }
};
</script>

<style>
#keep .v-navigation-drawer__border {
  display: none;
}
.obj-center {
  display: flex;
  justify-content: center;
}
.headline {
  white-space: normal;
}
</style>