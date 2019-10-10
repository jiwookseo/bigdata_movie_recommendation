<template>
  <div class="input-form-container">
    <span class="input-form">
      <select ref="method">
        <option value="" disabled selected>Select Method</option>
        <option value="km">K-Means</option>
        <option value="hr">Hierarchy</option>
        <option value="em">EM</option>
        <option value="kmc">K-Means (Cutomized)</option>
      </select>
    </span>
      
    <span class="input-form">
      <input ref="k" type="number" step="1" min="2" max="10" placeholder="k">
    </span>
      
    <span class="input-form">
      <v-btn class="refresh-button" @click="clustering">
        <span v-if="!isProceeding"><i class="fas fa-redo"></i></span>
        <span v-else><i class="fas fa-ellipsis-h"></i></span>
      </v-btn>
    </span>
  </div>
</template>

<script>
import { mapMutations, mapActions } from 'vuex';

export default {
  props: ['data'],
  data() {
    return {
      isProceeding: false,
    }
  },
  methods: {
    ...mapActions('movie', ['clusteringMovies']),
    ...mapActions('user', ['clusteringUsers']),
    ...mapMutations('loader', ['toggleLoader']),

    async clustering() {
      const params = {
        method: this.$refs.method.value,
        k: parseInt(this.$refs.k.value)
      }

      if (params.method && params.k) {
        this.toggleLoader();
        this.isProceeding = !this.isProceeding;
        if (this.data === 'movie') {
          await this.clusteringMovies(params)
        }
        if (this.data === 'user') {
          await this.clusteringUsers(params)
        } 
        this.isProceeding = !this.isProceeding;
        this.toggleLoader();
      } else {
        alert("인자를 설정해주세요. (Method / K)")
      }
    },
  }
}
</script>

<style scoped lang="scss">
@import "@/mixin/style/_dataControllerForm";
</style>
