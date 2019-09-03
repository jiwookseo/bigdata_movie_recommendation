<template>
  <v-app id="app">
    <v-app-bar app clipped-left color="indigo">
      <!-- <v-app-bar-nav-icon class="white--text" @click="drawer = !drawer" /> -->
      <span class="title ml-3 mr-5 white--text"><i class="fas fa-user-shield"></i> | Admin Page</span>
      <v-spacer />
    </v-app-bar>

    <v-content>
      <v-container fluid fill-height class="grey lighten-4">
        <v-layout justify-center align-center>
          <router-view />
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import router from "./router";

export default {
  methods: {
  
  }
};
</script>

<style>


</style>