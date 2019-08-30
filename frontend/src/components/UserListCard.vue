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
                  <UserDetailCard :username="username" :visible="dialog"></UserDetailCard>
                </v-dialog>

                <v-list-item class="list-item">
                  <v-list-item-content>
                    <v-list-item-title class="headline user-title">{{ username }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </div>
              <v-card-text>
                <v-layout justify-center>
                  <div class="grey--text point">
                    성별 : {{ gender === "M" ? "남" : "여" }}
                    <br />
                    나이 : {{ age }}
                    <br />
                    직업 : {{ occupation }}
                    <br />
                  </div>
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
import UserDetailCard from "./UserDetailCard";

export default {
  props: {
    id: {
      type: Number,
      default: 0
    },
    username: {
      type: String,
      default: ""
    },
    is_staff: {
      type: Boolean,
      default: false
    },
    gender: {
      type: String,
      default: ""
    },
    age: {
      type: Number,
      default: 0
    },
    occupation: {
      type: String,
      default: ""
    }
  },
  components: {
    UserDetailCard
  },
  data: () => ({
    dialog: false
  })
};
</script>

<style>
.user-title {
  display: flex;
  justify-content: center;
}
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