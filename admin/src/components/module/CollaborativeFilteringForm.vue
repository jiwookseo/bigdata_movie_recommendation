<template>
  <div class="collaborative-filtering-form-container">
    <div>
      <select ref="method">
        <option value="" disabled selected>Method</option>
        <option value="ub">KNN - User Based</option>
        <option value="mb">KNN - Movie Based</option>
        <option value="mf">Matrix Factorization</option>
      </select>
    </div>
    <div>
      <v-btn @click="filtering">CF</v-btn>
    </div>
  </div>
</template>

<script>
import { mapMutations, mapActions } from 'vuex';

export default {
  methods: {
    ...mapActions('user', ['collaborativeFiltering']),
    ...mapMutations('loader', ['toggleLoader']),

    async filtering() {
      const params = {
        method: this.$refs.method.value
      }
      if (params.method) {
        this.toggleLoader()
        await this.collaborativeFiltering(params);
        this.toggleLoader()
      } else {
        alert('메소드를 선택해주세요')
      }
    }
  }
}

</script>

<style scoped lang="scss">

</style>