<template>
  <v-hover v-slot:default="{ hover }">
    <v-card :elevation="hover ? 8 : 2">
      <v-layout align-center py-4 px-4>
        <v-flex text-center>
          <v-container grid-list-lg pa-0>
            <v-layout column>
              <div class="icon-title">
                <v-dialog v-model="dialog" width="40%">
                  <template v-slot:activator="{ on }">
                    <v-btn icon v-on="on" class="modal-button">
                      <v-icon large>pageview</v-icon>
                    </v-btn>
                  </template>
                  <MovieDetailCard :id="id"></MovieDetailCard>
                </v-dialog>

                <v-list-item class="list-item">
                  <v-list-item-content>
                    <v-list-item-title class="headline">{{ title }}</v-list-item-title>
                    <v-list-item-subtitle>{{ genresStr }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </div>
              <v-card-text>
                <v-layout justify-center>
                  <v-rating
                    :value="rating"
                    color="indigo"
                    background-color="indigo"
                    half-increments
                    dense
                    readonly
                  />
                  <div class="grey--text ml-3 point">{{ rating.toFixed(1) }}</div>
                  <v-icon color="black" class="ml-4">mdi-eye</v-icon>
                  <div class="grey--text ml-3 point">{{ viewCnt }}</div>
                </v-layout>
              </v-card-text>
            </v-layout>
          </v-container>
        </v-flex>
      </v-layout>
    </v-card>
  </v-hover>
</template>

<script>
import MovieDetailCard from "./MovieDetailCard";

export default {
  props: {
    id: {
      type: Number,
      default: 0
    },
    title: {
      type: String,
      default: ""
    },
    genres: {
      type: Array,
      default: () => new Array()
    },
    img: {
      type: String,
      default: ""
    },
    rating: {
      type: Number,
      default: 0.0
    },
    viewCnt: {
      type: Number,
      default: 0
    }
  },
  components: {
    MovieDetailCard
  },
  computed: {
    genresStr: function() {
      return this.genres.join(" / ");
    }
  },
  data: () => ({
    dialog: false
  })
};
</script>

<style>
.point {
  margin-top: 4px;
}
.icon-title {
  display: flex;
}
.list-item {
  padding: 0;
}
</style>