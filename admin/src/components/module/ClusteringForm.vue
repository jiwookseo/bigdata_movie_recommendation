<template>
  <div class="clustering-form-container">
    <div class="clustering-form-method">
      <select ref="method">
        <option value="" disabled selected>Method</option>
        <option value="km">K-Means</option>
        <option value="hr">Hierarchy</option>
        <option value="em">EM</option>
        <option value="kmc">K-Means (Cutomized)</option>
      </select>
    </div>
    <div class="clustering-form-k">
      <input ref="k" type="number" step="1" min="2" max="10">
    </div>
    <div class="clustering-form-button">
      <v-btn class="clustering_button" @click="clustering">clustering</v-btn>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  props: ['data'],
  methods: {
    ...mapActions('movie', ['clusteringMovies']),
    ...mapActions('user', ['clusteringUsers']),

    clustering() {
      const params = {
        method: this.$refs.method.value,
        k: parseInt(this.$refs.k.value)
      }

      if (params.method && params.k) {
        if (this.data === 'movie') {
          this.clusteringMovies(params)
        }
        if (this.data === 'user') {
          this.clusteringUsers(params)
        } 

      } else {
        alert("인자를 설정해주세요. (Method / K)")
      }
    },
  }
}
</script>

<style scoped lang="scss">
.clustering-form-container {
  width: 50%;
  display: flex;
  padding: 0 5%;
  justify-content: space-around;
  align-items: center;
}

.clustering-form-method, .clustering-form-k {
  font-size: 20px;
}

select, input {
  border-bottom: 1px solid grey;
  padding: 0 0 3px 0;
}

input {
  text-align: center;
}

select {
  text-align-last: center;
}
</style>
