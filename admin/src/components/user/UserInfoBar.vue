<template>
  <div class="item-info-bar">
    <div class="item-info">
      {{ username }} | {{ gender }} | {{ age }} | {{ isStaff }}
    </div>
    <div class="data-controller">
      <i class="fas fa-edit"></i> | <i class="fas fa-trash-alt"></i>
    </div>
  </div>
</template>

<script>
export default {
  props: ['username', 'gender', 'age', 'isStaff']
}
</script>

<style scoped lang="scss">
.item-info-bar {
  border-radius: 5px;
  height: 5vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 1px 1px 3px;

  .item-info {
    padding: 0 1vw;
    font-family: 'Lato', sans-serif;
    color: #535353;
  }

  .data-controller {
    padding: 0 1vw;
    color: #535353;
    .fa-edit:hover {
      color: #41B883;
    }
    .fa-trash-alt:hover {
      color: #FE1A1A;
    }
  }
}
</style>