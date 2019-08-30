<template>
  <v-container class="pa-2" fluid>
    <v-layout row class="layout">
      <v-flex v-for="card in userListCardsSliced" :key="card.id" pa-2 md6 lg6 xl6>
        <UserListCard
          :id="card.id"
          :username="card.username"
          :is-staff="card.is_staff"
          :gender="card.gender"
          :age="card.age"
          :occupation="card.occupation"
        />
      </v-flex>
      <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
    </v-layout>
  </v-container>
</template>

<script>
import UserListCard from "./UserListCard";

export default {
  components: {
    UserListCard
  },
  props: {
    userListCards: {
      type: Array,
      default: () => new Array()
    }
  },
  data: () => ({
    cardsPerPage: 12,
    page: 1
  }),
  computed: {
    // pagination related variables
    userListEmpty: function() {
      return this.userListCards.length === 0;
    },
    maxPages: function() {
      return Math.floor(
        (this.userListCards.length + this.cardsPerPage - 1) / this.cardsPerPage
      );
    },
    userListCardsSliced: function() {
      return this.userListCards.slice(
        this.cardsPerPage * (this.page - 1),
        this.cardsPerPage * this.page
      );
    }
  }
};
</script>