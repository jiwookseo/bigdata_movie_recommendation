<template>
  <div class="input-form-container">
    <span class="input-form">
      <select ref="method">
        <option value="" disabled selected>Select Method</option>
        <option value="ub">KNN - User Based</option>
        <option value="mb">KNN - Movie Based</option>
        <option value="mf">Matrix Factorization</option>
      </select>
    </span>
    <span class="input-form">
      <v-btn class="refresh-button" @click="filtering">
        <span v-if="!isProceeding"><i class="fas fa-redo"></i></span>
        <span v-else><i class="fas fa-ellipsis-h"></i></span>
      </v-btn>
    </span>
  </div>
</template>

<script>
import { mapMutations, mapActions } from 'vuex';

export default {
  data() {
    return {
      isProceeding: false
    }
  },
  methods: {
    ...mapActions('user', ['collaborativeFiltering']),
    ...mapMutations('loader', ['toggleLoader']),

    async filtering() {
      const params = {
        method: this.$refs.method.value
      }
      if (params.method) {
        this.toggleLoader()
        this.isProceeding = !this.isProceeding;
        await this.collaborativeFiltering(params);
        this.isProceeding = !this.isProceeding;
        this.toggleLoader()
      } else {
        alert('메소드를 선택해주세요')
      }
    }
  }
}

</script>

<style scoped lang="scss">
@import "@/mixin/style/_dataControllerForm";
</style>